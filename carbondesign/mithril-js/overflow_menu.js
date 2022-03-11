import m from 'mithril/hyperscript';
import DOMPurify from 'dompurify';
//-
import { Node } from './base';

export class OverflowMenu extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['flip', 'up']

    prepare(vnode, values, context)
    {
        values.txt_overflow = gettext("Overflow");

        if (vnode.attrs.flip)
        {
            values['class'].push('bx--overflow-menu--flip');
        }

        values.direction = vnode.attrs.up ? 'top' : 'bottom';
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--overflow-menu',
  {
    'data-overflow-menu': '',
  },
  [
    m('button',
      {
        'class': 'bx--overflow-menu__trigger bx--tooltip__trigger \
            bx--tooltip--a11y bx--tooltip-right bx--tooltip--align-start',
        'aria-haspopup': true,
        'aria-expanded': false,
        id: `trigger-${values.id}`,
        'aria-controls': values.id,
      },
      [
        m('span.bx--assistive-text', null, values.txt_overflow),
        this.tmpl('icon', vnode, values, context),
      ]),
    m('div',
      {
        'class': `bx--overflow-menu-options ${values['class']}`,
        tabindex: -1,
        role: 'menu',
        'aria-labelledby': `trigget-${values.id}`,
        'data-floating-menu-direction': values.direction,
        id: values.id,
      },
      [
        m('ul.bx--overflow-menu-options__content', null, values.child),
        m('span', {tabindex: 0}),
      ]),
  ])
//##
        );
    }

    render_tmpl_icon(vnode, values, context)
    {
        return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': 'bx--overflow-menu__icon',
    width: 16,
    height: 16,
    viewBox: '0 0 32 32',
    'aria-hidden': true,
  },
  [
    m('circle', {cx: 16, cy: 8, r: 2}),
    m('circle', {cx: 16, cy: 16, r: 2}),
    m('circle', {cx: 16, cy: 24, r: 2}),
  ])
//##
        );
    }
}


export class OverflowMenuItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['disabled', 'active', 'danger']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.disabled)
        {
            values['class'].push('bx--overflow-menu-options__option--disabled');
            values.props.push(['disabled', 'disabled']);
        }
        if (vnode.attrs.active)
        {
            values.props.push(['title', DOMPurify.sanitize(values.child)]);
            values.props.push(['data-floating-menu-primary-focus', '']);
        }
        if (vnode.attrs.danger)
        {
            values['class'].push('bx--overflow-menu-options__option--danger');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('li',
  {
    'class': `bx--overflow-menu-options__option ${values['class']}`,
  },
  m('button.bx--overflow-menu-options__btn',
    {
      role: 'menuitem',
      ...values.props,
    },
    m('span.bx--overflow-menu-options__option-content', null, values.child)))
//##
        );
    }
}
