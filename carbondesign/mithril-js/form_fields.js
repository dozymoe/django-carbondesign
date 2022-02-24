import { uniqueId } from 'lodash';
import m from 'mithril/hyperscript';


class Errors
{
    constructor(errors)
    {
        this.errors = errors;
    }

    as_text()
    {
        return m('ul');
    }
}


export class Field
{
    input_type = 'text'

    constructor(props)
    {
        this.id_for_label = props.id || uniqueId('field_');
        this.help_text = props.help_text;

        this.errors = {as_text() { }};
        this.widget = {attrs: {}};
    }

    set_errors(errors)
    {
        this.errors = new Errors(errors);
    }

    as_hidden(vnode)
    {
        return m('input', {type: 'hidden'});
    }

    as_widget(vnode)
    {
        return m('input', {type: this.input_type});
    }
}

export class CharField extends Field
{
}

export class TextField extends Field
{
    as_widget(vnode)
    {
        return m('textarea', {}, vnode.children);
    }
}
