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
m(values.astag,
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
            values.wrapper_class.push('bx--breadcrumb-item--current');
            values.props.push(['aria-current', 'page']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.astag,
  {
    'class': `bx--breadcrumb-item ${values.wrapper_class}`,
    ...values.wrapper_props,
  },
  m('a',
    {
      href: vnode.attrs.href,
      'class': `bx--link ${values['class']}`,
      ...values.props,
    },
    values.child))
//##
        );
    }
}
