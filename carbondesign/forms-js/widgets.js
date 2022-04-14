export class Widget
{
    attrs = {}

    setAttributes(attrs)
    {
        this.attrs = Object.assign({}, attrs);
    }

    valueFromDataDict(data, files, name)
    {
        if (data)
        {
            return data[name];
        }
    }

    useRequiredAttribute(initial)
    {
        return !this.isHidden();
    }

    isHidden()
    {
        return false;
    }

    render(name, value, attrs, renderer)
    {
        attrs = Object.assign({}, this.attrs, attrs);
        if (name)
        {
            attrs.name = name;
        }
        if (value)
        {
            attrs.value = value;
        }

        if (renderer)
        {
            return renderer(this.tag_name, attrs, null);
        }

        let element = document.createElement(this.tag_name);
        for (let key in attrs)
        {
            element.setAttribute(key, attrs[key]);
        }
        return element;
    }
}


export class Input extends Widget
{
    tag_name = 'input'
    input_type = 'text'

    setAttributes(attrs)
    {
        super.setAttributes(...arguments);
        if (!this.attrs.type)
        {
            this.attrs.type = this.input_type;
        }
    }

    isHidden()
    {
        return this.input_type === 'hidden';
    }
}


export class TextInput extends Input {}
export class HiddenInput extends Input { input_type = 'hidden' }
export class Textarea extends Widget { tag_name = 'textarea' }
