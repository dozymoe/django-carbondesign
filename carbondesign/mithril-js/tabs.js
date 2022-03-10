import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Tabs extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['header']
    NODE_PROPS = ['container']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.container)
        {
            values.wrapper_class.push('bx--tabs-container');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m.fragment(null,
  [
    m('div',
      {
        'data-tabs': '',
        'class': `bx--tabs ${values.wrapper_class}`,
      },
      [
        m('div.bx--tabs-trigger',
          {
            tabindex: 0,
          },
          [
            m('a.bx--tabs-trigger-text',
              {
                href='javascript:void(0)',
                tabindex: -1,
              }),
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                xmlns: 'http://www.w3.org/2000/svg',
                fill: 'currentColor',
                width: 16,
                height: 16,
                viewBox: '0 0 16 16',
                'aria-hidden': true,
              },
              m('path',
                {
                  d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
                })),
          ]),
        m('ul.bx--tabs__nav.bx--tabs__nav--hidden',
          {
            role: 'tablist',
          },
          this.slot('header', vnode, values, context)),
      ]),
    m('div.bx--tab-content', null, values.child),
  ])
//##
        );
    }
}


export class TabItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['active', 'target', 'disabled']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.active)
        {
            values.wrapper_class.push('bx--tabs__nav-item--selected');
            values.wrapper_props.push(['aria-selected', true]);
        }
        if (vnode.attrs.disabled)
        {
            values.wrapper_class.push('bx--tabs__nav-item--disabled');
            values.wrapper_props.push(['aria-disabled', true]);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('li',
  {
    'class': `bx--tabs__nav-item ${values.wrapper_class}`,
    'data-target': vnode.attrs.target,
    role: 'tab',
    ...values.wrapper_props,
  },
  m('a',
    {
      tabindex: 0,
      'class': `bx--tabs__nav-link ${values['class']}`,
      href: 'javascript:void(0)',
      role: 'tab',
      'aria-controls': vnode.attrs.target,
      ...values.props,
    },
    values.child))
//##
        );
    }
}


export class TabContent extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['active', 'target']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.active)
        {
            values.props.push(['aria-hidden', false]);
        }
        else
        {
            values.props.push(['aria-hidden', true]);
            values.props.push(['hidden', '']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    role: 'panel',
    'aria-labelledby': vnode.attrs.target,
    'aria-hidden': false,
    ...values.props,
  },
  m('div', null, values.child))
//##
        );
    }
}
