import m from 'mithril/hyperscript';
//-
import { Node, modify_svg } from './base';

export class Button extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']
    NODE_PROPS = ['disabled', 'variant', 'field', 'small', 'icon_size']
    DEFAULT_TAG = 'button'

    CATCH_PROPS = ['button_props']

    prepare(vnode, values, context)
    {
        let variant = vnode.attrs.variant || 'primary';
        values['class'].push('bx--btn--' + variant);

        if (vnode.attrs.disabled)
        {
            values.props.push(['disabled', 'disabled']);
            if (context.button_set)
            {
                values['class'].push('bx--btn--disabled');
            }
        }

        if (vnode.attrs.field)
        {
            values['class'].push('bx--btn--field');
        }

        if (vnode.attrs.small)
        {
            values['class'].push('bx--btn--sm');
        }

        if (values.label)
        {
            values.props.push(['aria-label', values.label]);
        }
    }

    render_default(vnode, values, context)
    {
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
                    width: `${size}px`,
                    height: `${size}px`,
                },
                'aria-hidden': true,
                'class': `bx--btn__icon ${values['class']}`,
                ...values.props,
            });
    }
}


export class IconButton extends Button
{
    prepare(vnode, values, context)
    {
        super.prepare(vnode, values, context);
        values['class'].push('bx--btn--icon-only', 'bx--tooltip__trigger',
                'bx--tooltip--a11y', 'bx--tooltip--bottom',
                'bx--tooltip--align-center');
    }

    render_default(vnode, values, context)
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
}


export class ButtonSet extends Node
{
    WANT_CHILDREN = true

    prepare(vnode, values, context)
    {
        context.button_set = true;
    }

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
