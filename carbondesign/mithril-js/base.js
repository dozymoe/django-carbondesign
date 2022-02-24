import { fromPairs, uniqueId } from 'lodash';

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
                    ['name', 'class'].indexOf(key) === -1)
            {
                props.push([key, vnode.attrs[key]]);
            }
        }
        return props;
    }

    render(vnode)
    {
        return vnode.children;
    }
}


export class Node
{
    WANT_CHILDREN = false
    SLOTS = []
    MODES = []
    BASE_NODE_PROPS = ['mode', 'tag', 'class', 'label', 'label_class']
    NODE_PROPS = []
    DEFAULT_TAG = 'div'
    TEMPLATES = []

    // Parent Tags can set html attributes on their childs.
    CATCH_CLASSNAMES = []
    CATCH_PROPERTIES = []

    constructor(app)
    {
        this.app = app;
    }

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

        let values = {}, context = {};

        this.before_prepare(vnode, values, context);
        this.prepare(vnode, values, context);
        this.after_prepare(vnode, values, context);

        let method = this['render_' + this.mode];
        if (!method)
        {
            throw "Method is missing: render_" + this.mode;
        }
        return method.bind(this)(vnode, values, context);
    }

    id(vnode)
    {
        if (!this._id)
        {
            this._id = vnode.attrs.id || uniqueId('node-');
        }
        return this._id
    }

    label(vnode)
    {
        return vnode.attrs.label;
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
            let method = this['render_slot_' + name];
            if (method)
            {
                return method(
                        vnode,
                        {
                            child: Slot.prototype.render(slot),
                            'class': values[name + '_class'],
                            props: values[name + '_props'],
                            id: values.id,
                            label: Slot.prototype.label(slot),
                        },
                        context);
            }
            return slot.children;
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
        values.id = this.id(vnode);
        values.tag = vnode.attrs.tag || this.DEFAULT_TAG;
        values.label = this.label(vnode);
        values.props = this.props(vnode);
        if (vnode.attrs['class'])
        {
            values['class'] = vnode.attrs['class'].split(/\s+/);
        }
        else
        {
            values['class'] = [];
        }
        values.label_props = [];
        if (vnode.attrs.label_class)
        {
            values.label_class = vnode.attrs.label_class.split(/\s+/);
        }
        else
        {
            values.label_class = [];
        }

        this.before_prepare_slots(vnode, values, context);

        // Parent Tags can set html attributes on their childs.
        for (let ext of this.CATCH_CLASSNAMES)
        {
            if (context[ext])
            {
                values['class'].push(...context[ext]);
            }
        }
        for (let ext of this.CATCH_PROPERTIES)
        {
            if (context[ext])
            {
                values.props.push(...context[ext]);
            }
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
        values.props = this.join_attributes(this.prune_attributes(
                values.props));

        values.child = this.WANT_CHILDREN ? this.nodelist : null;

        values['class'] = values['class'].join(' ');
        values.label_props = this.join_attributes(this.prune_attributes(
                values.label_props));
        values.label_class = values.label_class.join(' ');

        this.after_prepare_slots(vnode, values, context);
    }

    after_prepare_slots(vnode, values, context)
    {
        for (let name of this.SLOTS)
        {
            if (!this.slots[name]) continue;
            values[name + '_class'] = values[name + '_class'].join(' ');
            values[name + '_props'] = this.join_attributes(
                    this.prune_attributes(values[name + '_props']));
        }
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
}


export class FormNode extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['help', 'icon']
    BASE_NODE_PROPS = ['element', 'hidden', 'disabled', ...Node.BASE_NODE_PROPS]

    id(vnode)
    {
        return this.bound_field.id_for_label;
    }

    label(vnode)
    {
        return vnode.attrs.label || this.bound_field.label;
    }

    element(vnode, values)
    {
    }

    element_attributes(vnode)
    {
        return this.bound_field.widget.attrs;
    }

    before_prepare(vnode, values, context)
    {
        this.bound_field = vnode.attrs.element;
        if (!this.slots.help && this.bound_field.help_text)
        {
            this.slots.help = new DummyNodeList(this.bound_field.help_text);
        }
        super.before_prepare(vode, values, context);
    }

    after_prepare(vnode, values, context)
    {
        values.element = this.element(vnode, values);
        super.after_prepare(vnode, values, context);

        if (this.bound_field.errors)
        {
            values.form_errors = this.bound_field.errors.as_text()
        }
        else
        {
            values.form_errors = ''
        }
    }

    prepare_element_attributes(vnode, attrs, default_attrs, context)
    {
    }


    render_slot_help(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': 'bx--form__helper-text ' + values['class'],
    ...values.props,
  },
  values.child)
//##
        );
    }


    render_slot_icon(vnode, values, context)
    {
        return (
//##
m('svg',
  {
    'focusable': false,
    'preserveAspectRatio': 'xMidYMid meet',
    'style': {'will-change': 'transform'},
    'xmlns': 'http://www.w3.org/2000/svg',
    'class': 'bx--btn__icon ' + values['class'],
    'width': 16,
    'height': 16,
    'viewBox': '0 0 16 16',
    'aria-hidden': true,
    ...values.props,
  },
  values.child)
//##
        );
    }
}