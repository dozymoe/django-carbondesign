import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Tag extends Node
{
    WANT_CHILDREN = true
    MODES = ['default', 'filter']
    NODE_PROPS = ['variant']

    prepare(vnode, values, context)
    {
        values.txt_clear = gettext("Clear filter");

        let variant = vnode.attrs.variant;
        if (variant)
        {
            values['class'].push(`bx-tag--${variant}`);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('button',
  {
    type: 'button',
    'class': `bx--tag ${values['class']}`,
    ...values.props,
  },
  m('span.bx--tag__label', null, values.child))
//##
        );
    }

    render_filter(vnode, values, context)
    {
        return (
//##
m('div.bx--tag.bx--tag--filter',
  {
    title: values.txt_clear,
  },
  [
    m('span.bx--tag__label', null, values.child),
    m('button.bx--tag__close-icon', null,
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          width: 16,
          height: 16,
          viewBox: '0 0 32 32',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 \
                17.4 22.6 24 24 22.6 17.4 16 24 9.4z',
          }))),
  ])
//##
        );
    }
}
