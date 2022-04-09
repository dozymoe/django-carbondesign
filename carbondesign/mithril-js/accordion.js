import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Accordion extends Node
{
    WANT_CHILDREN = true
    DEFAULT_TAG = 'ul'

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'data-accordion': '',
    'class': `bx--accordion ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class AccordionItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['id', 'expanded']
    DEFAULT_TAG = 'li'

    prepare(vnode, values, context)
    {
        if (vnode.attrs.expanded)
        {
            values.expanded = 'true';
            values['class'].push('bx--accordion__item--active');
        }
        else
        {
            values.expanded = 'false';
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m(values.tag,
  {
    'data-accordion-item': '',
    'class': `bx--accordion__item ${values['class']}`,
    ...values.props,
  },
  [
    m('button.bx--accordion__heading',
      {
        'aria-expanded': values.expanded,
        'aria-controls': `${values.id}`,
      },
      [
        m('svg',
          {
            focusable: false,
            preserveAspectRatio: 'xMidYMid meet',
            xmlns: 'http://www.w3.org/2000/svg',
            fill: 'currentColor',
            'class': 'bx--accordion__arrow',
            width: 16,
            height: 16,
            viewBox: '0 0 16 16',
            'aria-hidden': true,
          },
          m('path', {d: 'M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z'})),
        this.tmpl('label', ...arguments),
      ]),
    m('div.bx--accordion__content',
      {
        id: `${values.id}`,
      },
      values.child),
  ])
//##
        );
    }

    render_tmpl_label(vnode, values, context)
    {
        if (values.label)
        {
            return (
//##
m('div',
  {
    'class': `bx--accordion__title ${values.label_class}`,
    ...values.label_props,
  },
  values.label)
//##
            );
        }
    }
}
