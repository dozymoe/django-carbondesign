import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';


export class TextInput extends FormNode
{
    NODE_PROPS = ['light']
    TEMPLATES = ['icon_invalid']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.help_class.push('bx--form__helper-text--disabled');
            values.props.push(['disabled', 'disabled']);
        }
    }

    prepare_element_attributes(vnode, attrs, default_attrs, context)
    {
        attrs['class'].push('bx--text-input');

        if (vnode.attrs.light)
        {
            attrs['class'].push('bx--text-input--light');
        }

        if (this.bound_field.errors)
        {
            attrs['class'].push('bx--text-input--invalid');
        }
    }

    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item.bx--text-input-wrapper', null,
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
    m('div.bx--text-input__field-wrapper',
      {
        'data-invalid': '',
      },
      [
        this.tmpl('icon_invalid', vnode, values, context),
        values.element,
      ]),
    m('div.bx--form-requirement', null, values.form_errors),
  ]);
//##
            );
        }
        return (
//##
m('div.bx--form-item.bx--text-input-wrapper', null,
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
    m('div.bx--text-input__field-wrapper', null, values.element),
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
    'class': 'bx--text-input__invalid-icon',
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


export class PasswordInput extends TextInput
{
    NODE_PROPS = ['light']
    TEMPLATES = ['icon_invalid', 'visibility']

    prepare(vnode, values, context)
    {
        super.prepare(vnode, values, context)

        values.txt_show_password = "Show password";
    }

    prepare_element_attributes(vnode, attrs, default_attrs, context)
    {
        super.prepare_element_attributes(vnode, attrs, default_attrs, context)

        attrs['class'].push('bx--password-input');
        attrs['data-toggle-password-visibility'] = ''
    }

    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item.bx--text-input-wrapper.bx--password-input-wrapper',
  {
    data-text-input: '',
  },
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
    m('div.bx--text-input__field-wrapper',
      {
        'data-invalid': '',
      },
      [
        this.tmpl('icon_invalid', vnode, values, context),
        values.element,
        this.tmpl('visibility', vnode, values, context),
      ]),
    m('div.bx--form-requirement', null, values.form_errors),
  ])
//##
            );
        }
        return (
//##
m('div.bx--form-item.bx--text-input-wrapper.bx--password-input-wrapper',
  {
    data-text-input: '',
  },
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
    m('div.bx--text-input__field-wrapper', null,
      [
        values.element,
        this.tmpl('visibility', vnode, values, context),
      ]),
    m('div.bx--form-requirement', null, values.form_errors),
  ])
//##
        );
    }

    render_tmpl_visibility(vnode, values, context)
    {
        return (
//##
m('button.bx--text-input--password__visibility__toggle\
    .bx--tooltip__trigger.bx--tooltip--a11y.bx--tooltip--bottom\
    .bx--tooltip--align-center',
  null,
  [
    m('span.bx--assistive-text', null, values.txt_show_password),
    m('svg.bx--icon--visibility-off',
      {
        focusable: false,
        preserveAspectRation: 'xMidYMid meet',
        style: {'will-change': 'transform'},
        xmlns: 'http://www.w3.org/2000/svg',
        hidden: true,
        width: 16,
        height: 16,
        viewBox: '0 0 16 16',
        'aria-hidden': true,
      },
      [
        m('path',
          {
            d: "M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,\
                6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,\
                2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,\
                1.7,10.4,2.6,11.3z",
          }),
        m('path',
          {
            d: "M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 \
                7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-\
                2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 \
                2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 \
                15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 \
                7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-\
                1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 \
                2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z",
          }),
      ]),
    m('svg.bx--icon--visibility-on',
      {
        focusable: false,
        preserveAspectRation: 'xMidYMid meet',
        style: {'will-change': 'transform'},
        xmlns: 'http://www.w3.org/2000/svg',
        hidden: true,
        width: 16,
        height: 16,
        viewBox: '0 0 16 16',
        'aria-hidden': true,
      },
      [
        m('path',
          {
            d: "M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,\
                7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3c3.3-0.1,\
                6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-\
                2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,\
                4.5C13.4,10.5,10.6,12.5,8,12.5z",
          }),
        m('path',
          {
            d: "M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,\
                10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z",
          }),
      ]),
  ])
//##
        );
    }
}
