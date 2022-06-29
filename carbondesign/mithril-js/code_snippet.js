import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Code extends Node
{
    WANT_CHILDREN = true
    MODES = ['default', 'single', 'inline']

    prepare(vnode, values, context)
    {
        values.txt_copied = gettext("Copied!");
        values.txt_copy = gettext("Copy code");
        values.txt_show_more = gettext("Show more");
        values.txt_show_more_icon = gettext("Show more icon");
        values.txt_show_less = gettext("Show less");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.astag,
  {
    'class': `bx--snippet bx--snippet--multi ${values['class']}`,
    'data-code-snippet': '',
    ...values.props,
  },
  [
    m('div',
      {
        'class': `bx--snippet-container ${values.label_class}`,
        'aria-label': values.label,
        ...values.label_props,
      },
      m('pre', null,
        m('code', null,
          values.child))),
    m('button.bx--copy-btn',
      {
        'data-copy-btn': '',
        type: 'button',
        tabindex: 0,
      },
      [
        m('span.bx--assistive-text.bx--copy-btn__feedback', null,
            values.txt_copied),
        m('svg',
          {
            focusable: false,
            preserveAspectRatio: 'xMidYMid meet',
            xmlns: 'http://www.w3.org/2000/svg',
            fill: 'currentColor',
            'class': 'bx--snippet__icon',
            width: 16,
            height: 16,
            viewBox: '0 0 32 32',
            'aria-hidden': true,
          },
          [
            m('path',
              {
                d: 'M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,\
                    2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z',
              }),
            m('path', {d: 'M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z'}),
          ]),
      ]),
    m('button.bx--btn.bx--btn--ghost.bx--btn--sm.bx--snippet-btn--expand',
      {
        type: 'button',
      },
      [
        m('span.bx--snippet-btn--text',
          {
            'data-show-more-text': values.txt_show_more,
            'data-show-less-text': values.txt_show_less,
          },
          values.txt_show_more),
        m('svg',
          {
            focusable: false,
            preserveAspectRatio: 'xMidYMid meet',
            xmlns: 'http://www.w3.org/2000/svg',
            fill: 'currentColor',
            'aria-label': values.txt_show_more_icon,
            'class': 'bx--icon-chevron--down bx--snippet__icon',
            width: 16,
            height: 16,
            viewBox: '0 0 16 16',
            role: 'img',
          },
          m('path', {d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z'})),
      ]),
  ])
//##
        );
    }

    render_single(vnode, values, context)
    {
        return (
//##
m(values.astag,
  {
    'class': `bx--snippet bx--snippet--single ${values['class']}`,
    ...values.props,
  },
  [
    m('div',
      {
        tabindex: 0,
        'class': `bx--snippet-container ${values.label_class}`,
        'aria-label': values.label,
        ...values.label_props,
      },
      m('pre', null,
        m('code', null,
          values.child))),
    m('button.bx--copy-btn',
      {
        'data-copy-btn': '',
        type: 'button',
        tabindex: 0,
      },
      [
        m('span.bx--assistive-text.bx--copy-btn__feedback', null,
            values.txt_copied),
        m('svg',
          {
            focusable: false,
            preserveAspectRatio: 'xMidYMid meet',
            xmlns: 'http://www.w3.org/2000/svg',
            fill: 'currentColor',
            'class': 'bx--snippet__icon',
            width: 16,
            height: 16,
            viewBox: '0 0 32 32',
            'aria-hidden': true,
          },
          [
            m('path',
              {
                d: 'M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,\
                    2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z',
              }),
            m('path', {d: 'M5,18H2V4A2,2,0,0,1,4,2H18V4H4Z'}),
          ]),
      ]),
  ])
//##
        );
    }

    render_inline(vnode, values, context)
    {
        return (
//##
m('button',
  {
    'data-copy-btn': '',
    type: 'button',
    'class': `bx--snippet bx--snippet--inline ${values['class']}`,
    'aria-label', values.txt_copy,
    tabindex: 0,
    ...values.props,
  },
  [
    m('code', null, values.child),
    m('span.bx--assistive-text.bx--copy-btn__feedback', null, values.txt_copied),
  ])
//##
        );
    }
}
