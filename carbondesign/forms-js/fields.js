import { omit, pick } from 'lodash';
import { TextInput } from './widgets';

export class Field
{
    WIDGET = TextInput

    constructor(attrs)
    {
        Object.assign(this, omit(attrs, ['widget']));

        let widget_class = attrs.widget || this.WIDGET;
        let widget = this.widget = new widget_class();
        widget.setAttributes(this.widgetAttrs(widget));
    }

    boundData(data, initial)
    {
        return this.widget.attrs.disabled ? initial : data;
    }

    prepareValue(value)
    {
        return value;
    }

    widgetAttrs(widget)
    {
        return {}
    }
}

export class CharField extends Field
{
    widgetAttrs(widget)
    {
        let attrs = super.widgetAttrs(widget);
        if (this.max_length && !widget.isHidden())
        {
            attrs.maxlength = this.max_length.toString();
        }
        if (this.min_length && !widget.isHidden())
        {
            attrs.minlength = this.min_length.toString();
        }
        return attrs;
    }
}
