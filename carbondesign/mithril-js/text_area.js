import m from 'mithril/hyperscript';
//-
import { Textarea } from '../forms-js/widgets';
import { FormNode } from './base';

export class TextArea extends FormNode
{
    NODE_PROPS = ['light']

    widget_class = Textarea

    prepare(vnode, values, context)
    {
        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.help_class.push('bx--form__helper-text--disabled');
        }
    }

    prepare_element_props(vnode, props, context)
    {
        props['class'].push('bx--text-area');
        props['class'].push('bx--text-area--v2');

        if (vnode.attrs.light)
        {
            props['class'].push('bx--text-area--light');
        }

        if (this.bound_field.errors)
        {
            props['class'].push('bx--text-area--invalid');
        }
    }

    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  [
    this.tmpl('label', ...arguments),
    m('div.bx--text-area__wrapper',
      {
        'data-invalid': '',
      },
      [
        this.tmpl('icon_invalid', ...arguments),
        this.tmpl('element', ...arguments),
      ]),
    m('div.bx--form-requirement', null, this.tmpl('errors', ...arguments)),
    this.tmpl('help', ...arguments),
  ])
//##
            );
        }
        return (
//##
m('div.bx--form-item', null,
  [
    this.tmpl('label', ...arguments),
    m('div.bx--text-area__wrapper', null, this.tmpl('element', ...arguments)),
    this.tmpl('help', ...arguments),
  ])
//##
        );
    }

    render_tmpl_icon_invalid(vnode, values, context)
    {
        return (
//##
m('svg',
  {
    focusable: 'false',
    preserveAspectRatio: 'xMidYMid meet',
    fill: 'currentColor',
    xmlns: 'http://www.w3.org/2000/svg',
    'class': 'bx--text-area__invalid-icon',
    width: 16,
    height: 16,
    viewBox: '0 0 16 16',
    'aria-hidden': 'true',
  },
  [
    m('path',
      {
        d: "M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-\
            1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-\
            0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z",
      }),
    m('path',
      {
        d: "M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s\
            0.3-0.8,0.8-0.8  c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z",
        'data-icon-path': 'inner-path',
        opacity: 0,
      }),
  ])
//##
        );
    }
}
