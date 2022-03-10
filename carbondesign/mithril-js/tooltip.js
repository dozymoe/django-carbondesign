import m from 'mithril/hyperscript';
//-
import { Node, modify_svg } from './base';

export class Tooltip extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon', 'footer']
    MODES = ['interactive', 'definition', 'icon']
    NODE_PROPS = ['align', 'position']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.align)
        {
            values['class'].push(`bx--tooltip--align-${vnode.attrs.align}`);
        }
        if (vnode.attrs.position)
        {
            values['class'].push(`bx--tooltip--${vnode.attrs.position}`);
        }
    }

    render_interactive(vnode, values, context)
    {
        return (
//##
m.fragment(null,
  [
    m('div',
      {
        id: `label-${values.id}`,
        'class': `bx--tooltip__label ${values['label_class']}`,
        ...values.props,
      },
      [
          values.label,
          m('button',
            {
              'aria-expanded': false,
              'aria-labelledby': `label-${values.id}`,
              'data-tooltip-trigger': '',
              'data-tooltip-target': `#${values.id}`,
              'class': `bx--tooltip__trigger ${values['class']}`,
              'aria-controls': values.id,
            },
            this.slot('icon', vnode, values, context)),
      ]),
    m('div.bx--tooltip',
      {
        id: values.id,
        'aria-hidden': true,
        'data-floating-menu-direction': 'bottom',
      },
      [
        m('span.bx--tooltip__caret'),
        m('div.bx--tooltip__content',
          {
            tabindex: -1,
            role: 'dialog',
            'aria-describedby': `body-${values.id}`,
            'aria-labelledby': `label-${values.id}`,
          },
          [
            m('div', {id: `body-${values.id}`}, values.child),
            this.slot('footer', vnode, values, context)),
          ]),
        m('span', {tabindex: 0}),
      ]),
  ])
//##
        );
    }

    render_definition(vnode, values, context)
    {
        return (
//##
m('div.bx--tooltip--definition.bx--tooltip--a11y',
  {
    'data-tooltip-definition': '',
  },
  [
    m('button',
      {
        'aria-describedby': values.id,
        'class': `bx--tooltip__trigger bx--tooltip--a11y bx--tooltip__trigger--definition ${values['class']}`,
      },
      values.label),
    m('div.bx--assistive-text',
      {
        id: values.id,
        role: 'tooltip',
      },
      values.child),
  ])
//##
        );
    }

    render_icon(vnode, values, context)
    {
        return (
//##
m('button',
  {
    'class': `bx--tooltip__trigger bx--tooltip--a11y ${values['class']}`,
    'data-tooltip-icon': '',
  },
  [
    m('span.bx--assistive-text', null, values.child),
    this.slot('icon', vnode, values, context),
  ])
//##
        ); 
    }

    render_slot_icon(vnode, values, context)
    {
        return modify_svg(values.child, {
            focusable: false,
            preserveAspectRatio: 'xMidYMid meet',
            fill: 'currentColor',
            style: 'width:16px; height:16px',
            'aria-hidden': true,
        })
    }

    render_slot_footer(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--tooltip__footer ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
}


export class TooltipHeading extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'h4'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'class': `bx--tooltip__heading ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}
