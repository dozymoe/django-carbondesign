import m from 'mithril/hyperscript';
import { Node } from './base';
import { HiddenInput as HiddenWidget } from '../forms-js/widgets';

export class HiddenInput extends Node
{
    BASE_NODE_PROPS = ['field', 'id', 'disabled', ...(new Node).BASE_NODE_PROPS]
    CLASS_AND_PROPS = []

    default_id(vnode)
    {
        return this.bound_field.id_for_label;
    }

    before_prepare(vnode, values, context)
    {
        this.bound_field = vnode.attrs.field;
        super.before_prepare(vnode, values, context);
    }

    render_default(vnode, values, context)
    {
        let attrs = {id: this._id}
        if (vnode.attrs.disabled)
        {
            attrs.disabled = true;
        }
        return this.bound_field.asWidget(attrs, HiddenWidget, m);
    }
}
