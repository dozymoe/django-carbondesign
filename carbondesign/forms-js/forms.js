import { startCase, uniqueId } from 'lodash';
//-
import { HiddenInput, Widget } from './widgets';

export class Form
{
    use_required_attribute = true

    constructor(schema, options)
    {
        for (let name in schema)
        {
            this[name] = new BoundField(this, schema[name], name);
        }
    }

    id()
    {
        if (this._id) return this._id;
        this._id = uniqueId('form_')
        return this._id;
    }

    set(initial, data, files)
    {
        this.initial = initial;
        this.data = data;
        this.files = files;

        for (let name in this)
        {
            let field = this[name];
            if (field instanceof BoundField)
            {
                field.reset();
            }
        }
        return this;
    }

    addPrefix(name)
    {
        return name;
    }

    autoId(name)
    {
        return `id_${name}`;
    }

    getInitialForField(field, field_name)
    {
        if (this.initial && this.initial[field_name])
        {
            return this.initial[field_name];
        }
        return field.initial;
    }

    getWidgetDataValue(widget, html_name)
    {
        return widget.valueFromDataDict(this.data, this.files, html_name);
    }

    validate(form)
    {
        if (form.checkValidity())
        {
            return true;
        }
        for (let name in this)
        {
            let field = this[name];
            if (field instanceof BoundField)
            {
                let input = form.elements[field.name];
                if (!input.validity.valid)
                {
                    field.errors = [input.validationMessage];
                }
            }
        }
        return false;
    }
}


export class BoundField
{
    constructor(form, field, name)
    {
        this.form = form;
        this.field = field;
        this.name = name;
        this.html_name = form.addPrefix(name);
        if (field.label)
        {
            this.label = field.label
        }
        else
        {
            this.label = startCase(name);
        }
        this.help_text = field.help_text || '';
        this.id_for_label = field.widget.id || form.autoId(this.html_name);
        this.reset();
    }

    reset()
    {
        this.initial = this.form.getInitialForField(this.field, this.name);
        this.data = this.form.getWidgetDataValue(this.field.widget,
                this.html_name);
        if (this.form.errors)
        {
            this.errors = this.form.errors[this.name];
        }
        else
        {
            this.errors = undefined;
        }
    }

    value()
    {
        let data = this.initial;
        if (this.form.data)
        {
            data = this.field.boundData(this.data, data);
        }
        return this.field.prepareValue(data);
    }

    asWidget(attrs, widget, renderer)
    {
        if (widget)
        {
            if (!(widget instanceof Widget))
            {
                widget = new widget();
                widget.setAttributes(this.field.widgetAttrs(widget));
            }
        }
        else
        {
            widget = this.field.widget;
        }
        attrs = attrs || {};
        attrs = this.buildWidgetAttrs(attrs, widget);
        if (!attrs.id)
        {
            attrs.id = this.id_for_label;
        }
        return widget.render(this.html_name, this.value(), attrs, renderer);
    }

    buildWidgetAttrs(attrs, widget)
    {
        widget = widget || this.field.widget;
        attrs = Object.assign({}, attrs);
        if (widget.useRequiredAttribute(this.initial) && this.field.required
                && this.form.use_required_attribute)
        {
            attrs.required = true;
        }
        if (this.field.disabled)
        {
            attrs.disabled = true;
        }
        return attrs;
    }
}
