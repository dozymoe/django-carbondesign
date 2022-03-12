import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Link extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['visited', 'disabled', 'inline']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.visited)
        {
            values['class'].push('bx--link--visited');
        }
        if (vnode.attrs.disabled)
        {
            values['class'].push('bx--link--disabled');
            values.props.push(['aria-disabled', 'true']);
        }
        if (vnode.attrs.inline)
        {
            values['class'].push('bx--link--inline');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('a',
  {
    'class': `bx--link ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}
