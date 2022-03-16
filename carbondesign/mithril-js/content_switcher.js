import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class ContentSwitcher extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-content-switcher': '',
    'class': `bx--content-switcher ${values['class']}`,
    role: 'tablist',
    'aria-label': values.label,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class ContentSwitcherItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['target', 'active', 'disabled']
    DEFAULT_TAG = 'button'

    prepare(vnode, values, context)
    {
        if (vnode.attrs.active)
        {
            values['class'].push('bx--content-switcher--selected');
            values.props.push(['aria-selected', 'true']);
        }
        if (vnode.attrs.disabled)
        {
            values.props.push(['disabled', 'disabled']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--content-switcher-btn ${values['class']}`,
    'data-target': vnode.attrs.target,
    role: 'tab',
    ...values.props,
  },
  m('span.bx--content-switcher__label', null, values.child))
//##
        );
    }
}
