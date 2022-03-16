import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class TextArea extends FormNode
{
    NODE_PROPS = ['light']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.help_class.push('bx--form__helper-text--disabled');
            values.props.push(['disabled', 'disabled']);
        }
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--text-area');
        props['class'].push('bx--text-area--v2');

        if (vnode.attrs.light)
        {
            props['class'].push('bx--text-input--light');
        }

        if (this.bound_field.errors)
        {
            props['class'].push('bx--text-input--invalid');
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
    m('label',
      {
        'for': values.id,
        'class': 'bx--label ' + values.label_class,
        ...values.label_props,
      },
      values.label
    ),
    this.slot('help', vnode, values, context),
    m('div.bx--text-area__wrapper',
      {
        'data-invalid': '',
      },
      [
        values.element,
        this.tmpl('icon_invalid', vnode, values, context),
      ]),
    m('div.bx--form-requirement', null, values.form_errors),
  ]);
//##
            );
        }
        return (
//##
m('div.bx--form-item', null,
  [
    m('label',
      {
        'for': values.id,
        'class': 'bx--label ' + values.label_class,
        ...values.label_props,
      },
      values.label
    ),
    this.slot('help', vnode, values context),
    m('div.bx--text-area__wrapper', null, values.element),
  ]);
//##
        );
    }

    render_tmpl_icon_invalid(vnode, values, context)
    {
        return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    style: {'will-change': 'transform'},
    xmlns: 'http://www.w3.org/2000/svg',
    'class': 'bx--text-area__invalid-icon',
    width: 16,
    height: 16,
    viewBox: '0 0 16 16',
    'aria-hidden': true,
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
  ]);
//##
        );
    }
}
