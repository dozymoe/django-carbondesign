import m from 'mithril/hyperscript';
//-
import { Node, modify_svg } from './base';

export class Button extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']
    NODE_PROPS = ['disabled', 'variant', 'icon_only', 'field', 'small',
            'icon_size']
    DEFAULT_TAG = 'button'

    CATCH_PROPS = ['button_props']

    prepare(vnode, values, context)
    {
        let variant = vnode.attrs.variant || 'primary';
        values['class'].push('bx--btn--' + variant);

        if (vnode.attrs.disabled)
        {
            values.props.push(['disabled', 'disabled']);
        }

        if (vnode.attrs.icon_only)
        {
            values['class'].push('bx--btn--icon-only', 'bx--tooltip__trigger',
                    'bx--tooltip--a11y', 'bx--tooltip--bottom',
                    'bx--tooltip--align-center');
        }

        if (vnode.attrs.field)
        {
            values['class'].push('bx--btn--field');
        }

        if (vnode.attrs.small)
        {
            values['class'].push('bx--btn--sm');
        }
    }

    render_default(vnode, values, context)
    {
        if (vnode.attrs.icon_only)
        {
            return (
//##
m(values.tag,
  {
    'class': `bx--btn ${values['class']}`,
    ...values.props,
  },
  [
    m('span.bx--assistive-text', null, values.child),
    this.slot('icon', ...arguments),
  ])
//##
            );
        }

        return (
//##
m(values.tag,
  {
    'class': `bx--btn ${values['class']}`,
    ...values.props,
  },
  [
    values.child,
    this.slot('icon', ...arguments),
  ])
//##
        );
    }

    render_slot_icon(values, context)
    {
        let size = vnode.attrs.icon_size || 16;
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                style: {
                    'will-change': 'transform',
                    width: size,
                    height: size,
                },
                'aria-hidden': true,
                'class': `bx--btn__icon ${values['class']}`,
                ...values.props,
            });
    }
}


export class ButtonSet extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': 'bx--btn-set ' + values['class'],
    ...values.props,
  },
  values.child)
//##
        );
    }
}
