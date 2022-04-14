import m from 'mithril/hyperscript';
//-
import { Node, modify_svg } from './base';

export class UiAction extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']
    REQUIRED_PROPS = ['label']
    DEFAULT_TAG = 'button'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--header__action ${values['class']}`,
    'aria-label': values.label,
    title: values.label,
    ...values.props,
  },
  this.slot('icon', ...arguments))
//##
        );
    }

    render_slot_icon(vnode, values, context)
    {
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                fill: 'currentColor',
                style: {
                    width: '20px',
                    height: '20px',
                },
                'aria-hidden': true,
                'class': 'bx--navigation-menu-panel-expand-icon',
            })
    }
}
