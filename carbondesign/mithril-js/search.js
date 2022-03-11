import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Search extends Node
{
    NODE_PROPS = ['style', 'light']
    AVAILABLE_STYLES = ['sm', 'lg', 'xl']

    prepare(vnode, values, context)
    {
        values.txt_clear = gettext("Clear search input");
        if (!values.label)
        {
            values.label  = gettext("Search");
        }

        if (vnode.attrs.style)
        {
            values['class'].append(`bx--search--${vnode.attrs.style}`);
        }

        if (vnode.attrs.light)
        {
            values['class'].append('bx--search--light');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-search': '',
      role: 'search',
      'class': `bx--search ${values['class']}`,
    },
    [
      m('label',
        {
          id: `label-${values.id}`,
          'class': `bx--label ${values.label_class}`,
          'for': values.id,
          ...values.label_props,
        },
        values.label),
      m('input.bx--search-input',
        {
          type: 'text',
          id: values.id,
          placeholder: values.label,
        }),
      m('svg.bx--search-magnifier',
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
            d: 'M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,\
                8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5 C2,4,4,2,\
                6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z',
          })),
      m('button.bx--search-close.bx--search-close--hidden',
        {
          title: values.txt_clear,
          'aria-label': values.txt_clear,
        },
        m('svg.bx--search-clear',
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
    ]))
//##
        );
    }
}
