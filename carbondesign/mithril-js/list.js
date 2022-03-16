import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class List extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'ul'

    prepare(vnode, values, context)
    {
        if (values.tag === 'ul')
        {
            values['class'].push('bx--list--unordered');
        }
        else
        {
            values['class'].push('bx--list--ordered');
        }
        if (context.list_nested)
        {
            values['class'].push('bx--list--nested');
        }
        context.list_nested: true;
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag, {'class': values['class'], ...values.props}, values.child)
//##
        );
    }
}


export class Li extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('li',
  {
    'class': `bx--list__item ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}
