import m from 'mithril/hyperscript';
//-
import { Node } from './base';


export class Button extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']
    NODE_PROPS = ['disabled', 'variant', 'icon_only', 'field', 'small',
            'icon_size']
    DEFAULT_TAG = 'button'

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

        values.icon_size = vnode.attrs.icon_size || 16;
    }

    render_default(vnode, values, context)
    {
        if (vnode.attrs.icon_only)
        {
            return (
//##
m(values.tag,
  {
    'class': 'bx--btn ' + values['class'],
    ...values.props,
  },
  [
    m('span.bx--assistive-text', {}, values.child),
    this.slot('icon', vnode, values, context),
  ])
//##
            );
        }
        return (
//##
m(values.tag,
  {
    'class': 'bx--btn ' + values['class'],
    ...values.props,
  },
  [
    values.child,
    this.slot('icon', vnode, values, context),
  ])
//##
        );
    }

    render_slot_icon(values, context)
    {
        return (
//##
m('svg.bx--btn__icon',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    style: {'will-change': 'transform'},
    xmlns: 'http://www.w3.org/2000/svg',
    width: values.icon_size,
    height: values.icon_size,
    viewBox: '0 0 ' + values.icon_size + ' ' + values.icon_size,
    'aria-hidden': true,
    ...values.props,
  },
  values.child)
//##
        );
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
