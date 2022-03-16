import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class CopyButton extends Node
{
    prepare(vnode, values, context)
    {
        values.txt_copied = gettext("Copied!");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('button',
  {
    'data-copy-btn': '',
    'class': `bx--copy-btn ${values['class']}`,
    type: 'button',
    tabindex: 0,
    ...values.props,
  },
  [
    m('span.bx--assistive-text.bx--copy-btn__feedback', null, values.txt_copied),
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
            d: 'M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,\
                2,0,0,0,2-2V10a2,2,0,0,0-2-2Z',
          }),
        m('path', {d: 'M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z'}),
      ]),
  ])
//##
        );
    }
}
