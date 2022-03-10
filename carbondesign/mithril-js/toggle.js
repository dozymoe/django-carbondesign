import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class Toggle extends FormNode
{
    MODES = ['default', 'nolabel']

    prepare(vnode, values, context)
    {
        values.txt_off = gettext("Off");
        values.txt_on = gettext("on");

        if (vnode.attrs.disabled)
        {
            values.props.push(['disabled', '']);
        }
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--toggle-input');

        if (this.mode === 'nolabel')
        {
            props['class'].push('bx--toggle-input--small');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item', null,
  [
    values.element,
    m('label',
      {
        'class': `bx--toggle-input__label ${label_class}`,
        'for': values.id,
      },
      [
        values.label,
        m('span.bx--toggle__switch', null,
          [
            m('svg.bx--toggle__check',
              {
                width: 6,
                height: 5,
                viewBox: '1 0 6 5',
              },
              m('path',
                {
                  d: 'M2.2 2.7L5 0 6 1 3.2 5 0 2.7 1 1.5z',
                })),
            m('span.bx--toggle__text--off',
              {
                'aria-hidden': true,
              },
              values.txt_off),
            m('span.bx--toggle__text--on',
              {
                'aria-hidden': true,
              },
              values.txt_on),
          ]),
      ]),
    this.tmpl('help', vnode, values, context),
  ])
//##
        );
    }

    render_nolabel(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item', null,
  [
    values.element,
    m('label',
      {
        'class': `bx--toggle-input__label ${values['class']}`,
        'for': values.id,
        'aria-label': values.label,
      },
      m('span.bx--toggle__switch', null,
        [
          m('svg.bx--toggle__check',
            {
              width: 6,
              height: 5,
              viewBox: '0 0 6 5',
            },
            m('path',
              {
                d: 'M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z',
              })),
          m('span.bx--toggle__text--off',
            {
              'aria-hidden': true,
            },
            values.txt_off),
          m('span.bx--toggle__text--on',
            {
              'aria-hidden': true,
            },
            values.txt_on),
        ])),
    this.tmpl('help', vnode, values, context),
  ])
//##
        );
    }
}
