import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Tile extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['above']
    MODES = ['default', 'clickable', 'expandable', 'selectable']

    prepare(vnode, values, context)
    {
        values.txt_tile = gettext("tile");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--tile ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_clickable(vnode, values, context)
    {
        return (
//##
m('a',
  {
    'data-tile': 'clickable',
    'class': `bx--tile bx--tile--clickable ${values['class']}`,
    tabindex: 0,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_expandable(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'data-tile': 'expandable',
    'class': `bx--tile bx--tile--expandable ${values['class']}`,
    tabindex: 0,
    ...values.props,
  },
  [
    m('button.bx--tile__chevron',
      {
        'aria-label': values.txt_expand,
      },
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
          }))),
    m('div.bx--tile-content', null,
      [
        m('span.bx--tile-content__above-the-fold',
          {
            'data-tile-atf': '',
          },
          this.slot('above', vnode, values, context)),
        m('span.bx--tile-content__below-the-fold', null, values.child),
      ]),
  ])
//##
        );
    }

    render_selectable(vnode, values, context)
    {
        return (
//##
m.fragment(null,
  [
    m('input',
      {
        tabindex: -1,
        'data-tile-input': '',
        id: values.id,
        'class': `bx--tile-input ${values['class']}`,
        type: 'checkbox',
        ...values.props,
      }),
    m('label',
      {
        'for': values.id,
        'aria-label': values.label,
        'class': `bx--tile bx--tile--selectable ${values.label_class}`,
        'data-tile': 'selectable',
        tabindex: 0,
        ...values.label_props,
      },
      [
        m('div.bx--tile__checkmark', null,
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
            [
              m('path',
                {
                  d: 'M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,\
                      11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,\
                      11z',
                }),
              m('path',
                {
                  d: 'M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z',
                  'data-icon-path': 'inner-path',
                  opacity: 0,
                }),
            ])),
        m('div.bx--tile-content', null, values.child),
      ])
  ])
//##
        );
    }
}


export class TileGrid extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--grid ${values['class']}`,
    ...values.props,
  },
  m('div.bx--tile-container',
    {
      style: {width: '100%'},
    },
    values.child))
//##
        );
    }
}
