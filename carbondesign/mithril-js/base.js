import DOMPurify from 'dompurify';
import { fromPairs, isArray, isObject, map, uniqueId } from 'lodash';
import m from 'mithril/hyperscript';
import m_tostring from 'mithril-node-render';

export function modify_svg(xml, props)
{
    if (isObject(xml) && xml.tag === '[')
    {
        xml = xml.children[0].children;
    }
    let tmpl = document.createElement('template');
    tmpl.innerHTML = xml.trim();
    let svg = tmpl.content.firstChild;
    for (let attr in props)
    {
        let value = props[attr];
        if (attr === 'style')
        {
            value = Object.entries(value).map(x => x.join(':')).join(';');
        }
        svg.setAttribute(attr, value);
    }
    return m.trust(tmpl.innerHTML);
}

export function clean_attr_value(value)
{
    return DOMPurify.sanitize(value);
}

class DummyNodeList
{
    constructor(text)
    {
        this.text = text
        this.attrs = {}
    }

    render(vnode)
    {
        return vnode.text;
    }
}

export class Slot
{
    classList(vnode)
    {
        if (vnode.attrs['class'])
        {
            return vnode.attrs['class'].split(/\s+/);
        }
        return [];
    }

    label(vnode)
    {
        return vnode.attrs.label || '';
    }

    props(vnode)
    {
        let props = [];
        for (let key in vnode.attrs)
        {
            if ((vnode.attrs[key] === '' || vnode.attrs[key]) &&
                    ['name', 'class', 'label'].indexOf(key) === -1)
            {
                props.push([key, vnode.attrs[key]]);
            }
        }
        return props;
    }

    render(vnode)
    {
        return m.fragment(vnode.attrs._context, vnode.children);
    }
}


export class Node
{
    WANT_CHILDREN = false
    SLOTS = []
    MODES = []
    BASE_NODE_PROPS = ['_context', 'mode', 'tag', 'class', 'label']
    NODE_PROPS = []
    REQUIRED_PROPS = []
    DEFAULT_TAG = 'div'
    CLASS_AND_PROPS = []

    // Parent Tags can set the arguments of their children Tags, in effect
    // changing their appearance.
    CATCH_PROPS = []

    view(vnode)
    {
        this.slots = {};
        this.nodelist = [];
        if (this.WANT_CHILDREN)
        {
            for (let child of vnode.children)
            {
                if (child.tag === Slot &&
                        this.SLOTS.indexOf(child.attrs.name) !== -1)
                {
                    this.slots[child.attrs.name] = child;
                }
                else
                {
                    this.nodelist.push(child);
                }
            }
        }

        let context = vnode.attrs._context || {};

        // Parent Tags can set the arguments of their children Tags.
        // You can also set them to children Tags in specific slot.
        let myslot = context.slot;
        for (let drop of this.CATCH_PROPS)
        {
            if (context[drop])
            {
                Object.assign(vnode.attrs, context[drop]);
            }
            if (myslot && context[`${myslot}_${drop}`])
            {
                Object.assign(vnode.attrs, context[`${myslot}_${drop}`]);
            }
        }

        for (let prop of this.REQUIRED_PROPS)
        {
            if (!vnode.attrs[prop])
            {
                throw `Argument ${prop} for component is required.`
            }
        }

        let values = {};

        this.before_prepare(vnode, values, context);
        this.prepare(vnode, values, context);

        if (this.WANT_CHILDREN)
        {
            values.child = m.fragment({_context: Object.assign({}, context)},
                    this.nodelist);
        }

        this.after_prepare(vnode, values, context);

        let method = this['render_' + this.mode];
        if (!method)
        {
            throw "Method is missing: render_" + this.mode;
        }
        return method.bind(this)(vnode, values, context);
    }

    default_id(vnode)
    {
        return uniqueId('node-');
    }

    props(vnode)
    {
        let props = [];
        for (let key in vnode.attrs)
        {
            if ((vnode.attrs[key] === '' || vnode.attrs[key]) &&
                    this.BASE_NODE_PROPS.indexOf(key) === -1 &&
                    this.NODE_PROPS.indexOf(key) === -1)
            {
                props.push([key, vnode.attrs[key]]);
            }
        }
        return props;
    }

    tmpl(name, vnode, values, context)
    {
        return this['render_tmpl_' + name](vnode, values, context)
    }

    slot(name, vnode, values, context)
    {
        let slot = this.slots[name];
        if (slot)
        {
            slot.attrs._context = Object.assign({slot: name}, context);

            let method = this['render_slot_' + name];
            if (method)
            {
                return method(
                        vnode,
                        {
                            slot: name,
                            child: Slot.prototype.render(slot),
                            'class': values[name + '_class'],
                            props: values[name + '_props'],
                            id: values.id,
                            label: Slot.prototype.label(slot),
                        },
                        context);
            }
            return Slot.prototype.render(slot);
        }
    }

    before_prepare(vnode, values, context)
    {
        this.mode = vnode.attrs.mode;
        if (this.MODES.length)
        {
            if (!this.mode)
            {
                this.mode = this.MODES[0];
            }
            else if (this.MODES.indexOf(this.mode) === -1)
            {
                throw "Mode is not allowed: " + this.mode;
            }
        }
        else
        {
            this.mode = 'default';
        }
        values.mode = this.mode;
        values.tag = vnode.attrs.tag || this.DEFAULT_TAG;
        values.props = this.props(vnode);
        if (vnode.attrs['class'])
        {
            values['class'] = vnode.attrs['class'].split(/\s+/);
        }
        else
        {
            values['class'] = [];
        }
        this._id = vnode.attrs.id || this.default_id(vnode);
        values.id = this._id
        values.label = vnode.attrs.label;

        for (let name of this.CLASS_AND_PROPS)
        {
            if (this.SLOTS.indexOf(name) !== -1)
            {
                continue;
            }
            this.before_prepare_class_props(name, vnode, values, context);
        }
        this.before_prepare_slots(vnode, values, context);
    }

    before_prepare_class_props(name, vnode, values, context)
    {
        values[`${name}_props`] = [];
        if (vnode.attrs[`${name}_class`])
        {
            values[`${name}_class`] = vnode.attrs[`${name}_class`].split(/\s+/);
        }
        else
        {
            values[`${name}_class`] = [];
        }
    }

    before_prepare_slots(vnode, values, context)
    {
        for (let name of this.SLOTS)
        {
            let slot = this.slots[name];
            values[name + '_class'] = slot ? Slot.prototype.classList(slot) : [];
            values[name + '_props'] = slot ? Slot.prototype.props(slot) : [];
        }
    }

    after_prepare(vnode, values, context)
    {
        values.props_raw = this.prune_attributes(values.props);
        values.props = this.join_attributes(values.props_raw);
        values['class'] = values['class'].join(' ');

        for (let name of this.CLASS_AND_PROPS)
        {
            if (this.SLOTS.indexOf(name) !== -1)
            {
                continue;
            }
            this.after_prepare_class_props(name, vnode, values, context);
        }
    }

    after_prepare_class_props(name, vnode, values, context)
    {
        values[`${name}_props`] = this.join_attributes(this.prune_attributes(
                values[`${name}_props`]));
        values[`${name}_class`] = values[`${name}_class`].join(' ');
    }

    prune_attributes(attrs)
    {
        let added_props = [];
        let props = [];
        for (let ii = attrs.length - 1; ii >=0; ii--)
        {
            let prop_name = attrs[ii][0];
            if (added_props.indexOf(prop_name) !== -1) continue;
            added_props.push(prop_name);
            props.push(attrs[ii]);
        }
        return props;
    }

    join_attributes(attrs)
    {
        return fromPairs(attrs);
    }

    prepare(vnode, values, context)
    {
    }

    set_child_props(context, name, slot, keyval)
    {
        if (slot)
        {
            name = `${slot}_${name}`;
        }
        if (!context[name])
        {
            context[name] = {};
        }
        Object.assign(context[name], keyval);
    }
}


export class FormNode extends Node
{
    BASE_NODE_PROPS = ['field', 'widget', 'id', 'disabled',
            ...(new Node).BASE_NODE_PROPS]
    CLASS_AND_PROPS = ['label', 'help']

    default_id(vnode)
    {
        return this.bound_field.id_for_label;
    }

    label()
    {
        return this.bound_field.label;
    }

    before_prepare(vnode, values, context)
    {
        this.bound_field = vnode.attrs.field;
        this.bound_value = this.bound_field.value();
        super.before_prepare(vnode, values, context);
        if (!values.label)
        {
            values.label = this.label();
        }
    }

    prepare_element_props(vnode, props, context)
    {
    }

    choices(vnode)
    {
        if (this._choices)
        {
            return this._choices;
        }
        this._choices = []

        let choices = this.bound_field.field.choices;
        if (!isArray(choices))
        {
            let default_truthy = this.bound_value || 'on';
            let label = this.bound_field.label
            choices = [['', label], [default_truthy, label]]
        }

        let group_name, subchoices;
        for (let [option_value, option_label] of choices)
        {
            if (option_value === null)
            {
                option_value = '';
            }
            if (isArray(option_label))
            {
                group_name = option_value;
                subchoices = option_label;
            }
            else
            {
                group_name = null;
                subchoices = [[option_value, option_label]];
            }

            for (let [subvalue, sublabel] of subchoices)
            {
                this._choices.push([group_name, subvalue, sublabel]);
            }
        }

        return this._choices;
    }

    render_tmpl_element(vnode, values, context)
    {
        let attrs = {};
        for (let pair of values.props_raw)
        {
            attrs[pair[0]] = pair[1];
        }
        attrs.id = this._id;
        attrs['class'] = this.bound_field.field.widget.attrs['class'] || ''
        attrs['class'] = attrs['class'].split(/\s+/);
        if (this.bound_field.help_text)
        {
            attrs['aria-controls'] = `hint-${values.id}`;
            attrs['aria-describedby'] = `hint-${values.id}`;
        }

        this.prepare_element_props(vnode, attrs, context);
        attrs['class'] = attrs['class'].join(' ');

        if (vnode.attrs.disabled)
        {
            attrs['disabled'] = true;
        }

        return this.bound_field.asWidget(attrs, this.widget_class, m);
    }

    render_tmpl_label(vnode, values, context)
    {
        if (values.label)
        {
            return (
//##
m('label',
  {
    'for': values.id,
    'class': `bx--label ${values.label_class}`,
    ...values.label_props,
  },
  values.label)
//##
            );
        }
    }

    render_tmpl_help(vnode, values, context)
    {
        if (this.bound_field.help_text)
        {
            return (
//##
m('div',
  {
    'id': `hint-${values.id}`,
    'class': `bx--form__helper-text ${values.help_class}`,
    ...values.help_props,
  },
  this.bound_field.help_text)
//##
            );
        }
    }

    render_tmpl_errors(vnode, values, context)
    {
        return _render_errors(this.bound_field);
    }
}


export function render_errors(bound_field)
{
    let errors = _render_errors(bound_field);
    if (errors)
    {
        return m('div.bx--form-requirement', errors);
    }
}

function _render_errors(bound_field)
{
    if (!bound_field.errors) return;

    let items = [];
    for (let error of bound_field.errors)
    {
        let pos = error.indexOf('\n');
        if (pos >= 0)
        {
            items.push(m('div.bx--form-requirement__title',
                    error.slice(0, pos)));
            items.push(m('p.bx--form-requirement__supplement',
                    error.slice(pos + 1)));
        }
        else
        {
            items.push(m('div.bx--form-requirement__title', error));
        }
    }
    if (items.length)
    {
        return m.fragment(items);
    }
}


export class FormNodes extends Node
{
    BASE_NODE_PROPS = ['fields', 'hidden', 'disabled',
            ...(new Node).BASE_NODE_PROPS]

    elements(vnode, values, context)
    {
    }

    before_prepare(vnode, values, context)
    {
        this.bound_fields = vnode.attrs.fields;
        for (let ii = 0; ii < this.bound_fields.length; ii++)
        {
            let field = this.bound_fields[ii];
            values[`id_${ii}`] = field.id_for_label;
            values[`label_${ii}`] = field.label;
        }
        super.before_prepare(vnode, values, context);
    }

    after_prepare(vnode, values, context)
    {
        let ii = 0;
        for (let element of this.elements(vnode, values, context))
        {
            values[`element_${ii}`] = element;
            ii++;
        }
        super.after_prepare(vnode, values, context);

        for (ii = 0; ii < this.bound_fields.length; ii++)
        {
            let field = this.bound_fields[ii];
            if (field.errors)
            {
                values[`form_errors_${ii}`] = field.errors.as_text();
            }
        }
    }

    prepare_element_props(vnode, field, props, default_props, context)
    {
    }
}


export function dom2mithril(dom)
{
    if (dom.tagName)
    {
        let attrs = {};
        for (let attr of dom.attributes)
        {
            attrs[attr.name] = attr.value;
        }
        return m(dom.tagName.toLowerCase(), attrs,
                map(dom.children, dom2mithril));
    }
    return dom;
}
