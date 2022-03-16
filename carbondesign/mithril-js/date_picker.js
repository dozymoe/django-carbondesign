import { some } from 'lodash';
import m from 'mithril/hyperscript';
//-
import { FormNode, FormNodes } from './base';

export class DatePicker extends FormNode
{
    MODES = ['default', 'basic', 'nolabel']
    NODE_PROPS = ['light']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.light)
        {
            values.wrapper_class.push('bx--date-picker--light');
        }
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--date-picker__input');
        props['data-date-picker-input'] = '';
        props.pattern = '\\d{1,2}/\\d{1,2}/\\d{4}';
        props.placeholder = 'mm/dd/yyyy';

        if (this.bound_field.errors)
        {
            props['data-invalid'] = '';
        }
    }

    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-date-picker': '',
      'data-date-picker-type': 'single',
      'class': `bx--date-picker bx--date-picker--single ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('label',
          {
            'for': values.id,
            'class': `bx--label ${values.label_class}`,
            ...values.label_props,
          },
          values.label),
        m('div.bx--date-picker-input__wrapper', null,
          [
            values.element,
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                xmlns: 'http://www.w3.org/2000/svg',
                fill: 'currentColor',
                'data-date-picker-icon': true,
                'class': 'bx--date-picker__icon',
                width: 16,
                height: 16,
                viewBox: '0 0 32 32',
                'aria-hidden': true,
              },
              m('path',
                {
                  d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                      0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,\
                      26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                })),
          ]),
        m('div.bx--form-requirement', null, values.form_errors),
      ])))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-date-picker': '',
      'data-date-picker-type': 'single',
      'class': `bx--date-picker bx--date-picker--single ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('label',
          {
            'for': values.id,
            'class': `bx--label ${values.label_class}`,
            ...values.label_props,
          },
          values.label),
        m('div.bx--date-picker-input__wrapper', null,
          [
            values.element,
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                xmlns: 'http://www.w3.org/2000/svg',
                fill: 'currentColor',
                'data-date-picker-icon': true,
                'class': 'bx--date-picker__icon',
                width: 16,
                height: 16,
                viewBox: '0 0 32 32',
                'aria-hidden': true,
              },
              m('path',
                {
                  d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                      0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,\
                      26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                })),
          ]),
      ])))
//##
        );
    }

    render_nolabel(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-date-picker': '',
      'data-date-picker-type': 'single',
      'class': `bx--date-picker bx--date-picker--single bx--date-picker--nolabel ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('div.bx--date-picker-input__wrapper', null,
          [
            value.element,
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                xmlns: 'http://www.w3.org/2000/svg',
                fill: 'currentColor',
                'data-date-picker-icon': true,
                'class': 'bx--date-picker__icon',
                width: 16,
                height: 16,
                viewBox: '0 0 32 32',
                'aria-hidden': true,
              },
              m('path',
                {
                  d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                      0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,\
                      26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                })),
            m('div.bx--form-requirement', null, values.form_errors),
          ]),
      ])))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-date-picker': '',
      'data-date-picker-type': 'single',
      'class': `bx--date-picker bx--date-picker--single bx--date-picker--nolabel ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('div.bx--date-picker-input__wrapper', null,
          [
            value.element,
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                xmlns: 'http://www.w3.org/2000/svg',
                fill: 'currentColor',
                'data-date-picker-icon': true,
                'class': 'bx--date-picker__icon',
                width: 16,
                height: 16,
                viewBox: '0 0 32 32',
                'aria-hidden': true,
              },
              m('path',
                {
                  d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                      0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,\
                      26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                })),
            m('div.bx--form-requirement', null, values.form_errors),
          ]),
      ])))
//##
        );
    }

    render_basic(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--date-picker bx--date-picker--simple ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('label',
          {
            'for': values.id,
            'class': `bx--label ${values.label_class}`,
            ...values.label_props,
          },
          values.label),
        values.element,
        m('div.bx--form-requirement', null, values.form_errors),
      ])))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--date-picker bx--date-picker--simple bx--date-picker--short ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('label',
          {
            'for': values.id,
            'class': `bx--label ${values.label_class}`,
            ...values.label_props,
          },
          values.label),
        values.element,
      ])))
//##
        );
    }
}


export class RangeDatePicker extends FormNodes
{
    NODE_PROPS = ['light']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.light)
        {
            values.wrapper_class.push('bx--date-picker--light');
        }
    }

    prepare_element_props(vnode, field, props, default_props, context)
    {
        let index = this.bound_fields.indexOf(field);

        props['class'].push('bx--date-picker__input');
        props.pattern = '\\d{1,2}/\\d{1,2}/\\d{4}';
        props.placeholder = 'mm/dd/yyyy';

        if (index)
        {
            props['data-date-picker-input-to'] = '';
        }
        else
        {
            props['data-date-picker-input-from'] = '';
        }

        if (field.errors)
        {
            props['data-invalid'] = '';
        }
    }

    render_default(vnode, values, context)
    {
        let has_errors = some(this.bound_fields, x => x.errors);
        if (has_errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-date-picker': '',
      'data-date-picker-type': 'range',
      'class': `bx--date-picker bx--date-picker--range ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    [
      m('div.bx--date-picker-container', null,
        [
          m('label',
            {
              'for': values.id_0,
              'class': `bx--label ${values.label_class}`,
              ...values.label_props,
            },
            values.label_0),
          m('div.bx--date-picker-input__wrapper', null,
            [
              values.element_0,
              m('svg',
                {
                  focusable: false,
                  preserveAspectRatio: 'xMidYMid meet',
                  xmlns: 'http://www.w3.org/2000/svg',
                  fill: 'currentColor',
                  'data-date-picker-icon': true,
                  'class': 'bx--date-picker__icon',
                  width: 16,
                  height: 16,
                  viewBox: '0 0 32 32',
                  'aria-hidden': true,
                },
                m('path',
                  {
                    d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                        0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,\
                        4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                  })),
            ]),
          m('div.bx--form-requirement', null, values.form_errors_0),
        ]),
      m('div.bx--date-picker-container', null,
        [
          m('label',
            {
              'for': values.id_1,
              'class': `bx--label ${values.label_class}`,
              ...values.label_props,
            },
            values.label_1),
          m('div.bx--date-picker-input__wrapper', null,
            [
              values.element_1,
              m('svg',
                {
                  focusable: false,
                  preserveAspectRatio: 'xMidYMid meet',
                  xmlns: 'http://www.w3.org/2000/svg',
                  fill: 'currentColor',
                  'data-date-picker-icon': true,
                  'class': 'bx--date-picker__icon',
                  width: 16,
                  height: 16,
                  viewBox: '0 0 32 32',
                  'aria-hidden': true,
                },
                m('path',
                  {
                    d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                        0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z \
                        M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                  })),
            ]),
          m('div.bx--form-requirement', null, values.form_errors_1),
        ]),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'data-date-picker': '',
      'data-date-picker-type': 'range',
      'class': `bx--date-picker bx--date-picker--range ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    [
      m('div.bx--date-picker-container', null,
        [
          m('label',
            {
              'for': values.id_0,
              'class': `bx--label ${values.label_class}`,
              ...values.label_props,
            },
            values.label_0),
          m('div.bx--date-picker-input__wrapper', null,
            [
              values.element_0,
              m('svg',
                {
                  focusable: false,
                  preserveAspectRatio: 'xMidYMid meet',
                  xmlns: 'http://www.w3.org/2000/svg',
                  fill: 'currentColor',
                  'data-date-picker-icon': true,
                  'class': 'bx--date-picker__icon',
                  width: 16,
                  height: 16,
                  viewBox: '0 0 32 32',
                  'aria-hidden': true,
                },
                m('path',
                  {
                    d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                        0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,\
                        4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                  })),
            ]),
        ]),
      m('div.bx--date-picker-container', null,
        [
          m('label',
            {
              'for': values.id_1,
              'class': `bx--label ${values.label_class}`,
              ...values.label_props,
            },
            values.label_1),
          m('div.bx--date-picker-input__wrapper', null,
            [
              values.element_1,
              m('svg',
                {
                  focusable: false,
                  preserveAspectRatio: 'xMidYMid meet',
                  xmlns: 'http://www.w3.org/2000/svg',
                  fill: 'currentColor',
                  'data-date-picker-icon': true,
                  'class': 'bx--date-picker__icon',
                  width: 16,
                  height: 16,
                  viewBox: '0 0 32 32',
                  'aria-hidden': true,
                },
                m('path',
                  {
                    d: 'M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,\
                        0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z \
                        M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z',
                  })),
            ]),
        ]),
    ]))
//##
        );
    }
}
