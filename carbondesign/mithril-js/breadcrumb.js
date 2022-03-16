import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Breadcrumb extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['current']
    DEFAULT_TAG = 'nav'

    prepare(vnode, values, context)
    {
        values.txt_breadcrumb = gettext("breadcrumb");

        if (vnode.attrs.current)
        {
            values['class'].push('bx--breadcrumb--no-trailing-slash');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--breadcrumb ${values['class']}`,
    'aria-label': values.txt_breadcrumb,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class BreadcrumbItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['href', 'current']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.current)
        {
            values.props.push(['aria-current', 'page']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--breadcrumb-item ${values['class']}`,
    ...values.props,
  },
  m('a.bx--link',
    {
      href: vnode.attrs.href,
    },
    values.child))
//##
        );
    }
}
