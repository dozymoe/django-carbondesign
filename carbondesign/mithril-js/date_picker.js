import flatpickr from 'flatpickr';
import { some } from 'lodash';
import m from 'mithril/hyperscript';
//-
import { FormNode, FormNodes } from './base';

const TOKEN_REGEX = {
    D: "(\\w+)",
    F: "(\\w+)",
    G: "(\\d\\d|\\d)",
    H: "(\\d\\d|\\d)",
    J: "(\\d\\d|\\d)\\w+",
    // ToDo: K is ignored
    M: "(\\w+)",
    S: "(\\d\\d|\\d)",
    U: "(.+)",
    W: "(\\d\\d|\\d)",
    Y: "(\\d{4})",
    Z: "(.+)",
    d: "(\\d\\d|\\d)",
    h: "(\\d\\d|\\d)",
    i: "(\\d\\d|\\d)",
    j: "(\\d\\d|\\d)",
    l: "(\\w+)",
    m: "(\\d\\d|\\d)",
    n: "(\\d\\d|\\d)",
    s: "(\\d\\d|\\d)",
    u: "(.+)",
    w: "(\\d\\d|\\d)",
    y: "(\\d{2})",
};
const DEFAULT_DATE_FORMAT = 'm/d/Y';
const DEFAULT_SHORTDATE_FORMAT = 'm/Y';

function format_to_pattern(value)
{
    return value.split('').map((x) => REGEX_PATTERN[x] || x).join('');
}

export class DatePicker extends FormNode
{
    MODES = ['default', 'basic', 'nolabel']
    NODE_PROPS = ['short', 'light', 'format']
    CLASS_AND_PROPS = ['label', 'help', 'picker']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.light)
        {
            values.picker_class.push('bx--date-picker--light');
        }
        if (vnode.attrs.short)
        {
            values.picker_class.push('bx--date-picker--short');
        }

        if (vnode.attrs.format)
        {
            this.datefmt = vnode.attrs.format;
        }
        else if (vnode.attrs.short)
        {
            this.datefmt = DEFAULT_SHORTDATE_FORMAT;
        }
        else
        {
            this.datefmt = DEFAULT_DATE_FORMAT;
        }
        this.placeholder = flatpickr.formatDate(new Date(1, 1, 1, 0, 0, 0),
                this.datefmt);
        this.pattern = format_to_pattern(this.datefmt);

        values['picker_props'].push(['data-date-picker-format', this.datefmt]);
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--date-picker__input');
        props['data-date-picker-input'] = '';
        props.pattern = this.pattern;
        props.placeholder = this.placeholder;

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
      'class': `bx--date-picker bx--date-picker--single ${values.picker_class}`,
      ...values.picker_props,
    },
    m('div.bx--date-picker-container', null,
      [
        this.tmpl('label', ...arguments),
        m('div.bx--date-picker-input__wrapper', null,
          [
            this.tmpl('element', ...arguments),
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
        m('div.bx--form-requirement', null,
            this.tmpl('errors', ...arguments)),
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
      'class': `bx--date-picker bx--date-picker--single ${values.picker_class}`,
      ...values.picker_props,
    },
    m('div.bx--date-picker-container', null,
      [
        this.tmpl('label', ...arguments),
        m('div.bx--date-picker-input__wrapper', null,
          [
            this.tmpl('element', ...arguments),
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
      'class': `bx--date-picker bx--date-picker--single bx--date-picker--nolabel ${values.picker_class}`,
      ...values.picker_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('div.bx--date-picker-input__wrapper', null,
          [
            this.tmpl('element', ...arguments),
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
            m('div.bx--form-requirement', null,
                this.tmpl('errors', ...arguments)),
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
      'class': `bx--date-picker bx--date-picker--single bx--date-picker--nolabel ${values.picker_class}`,
      ...values.picker_props,
    },
    m('div.bx--date-picker-container', null,
      [
        m('div.bx--date-picker-input__wrapper', null,
          [
            this.tmpl('element', ...arguments),
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

    render_basic(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--date-picker bx--date-picker--simple ${values.picker_class}`,
      ...values.picker_props,
    },
    m('div.bx--date-picker-container', null,
      [
        this.tmpl('label', ...arguments),
        this.tmpl('element', ...arguments),
        m('div.bx--form-requirement', null,
            this.tmpl('errors', ...arguments)),
      ])))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--date-picker bx--date-picker--simple ${values.picker_class}`,
      ...values.picker_props,
    },
    m('div.bx--date-picker-container', null,
      [
        this.tmpl('label', ...arguments),
        this.tmpl('element', ...arguments),
      ])))
//##
        );
    }
}


export class RangeDatePicker extends FormNodes
{
    NODE_PROPS = ['light', 'format']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.light)
        {
            values.wrapper_class.push('bx--date-picker--light');
        }

        if (vnode.attrs.format)
        {
            this.datefmt = vnode.attrs.format;
        }
        else
        {
            this.datefmt = DEFAULT_DATE_FORMAT;
        }
        this.placeholder = flatpickr.formatDate(new Date(1, 1, 1, 0, 0, 0),
                this.datefmt);
        this.pattern = format_to_pattern(this.datefmt);
    }

    prepare_element_props(vnode, field, props, default_props, context)
    {
        let index = this.bound_fields.indexOf(field);

        props['class'].push('bx--date-picker__input');
        props.pattern = this.pattern;
        props.placeholder = this.placeholder;

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
      'class': `bx--date-picker bx--date-picker--range ${values.picker_class}`,
      ...values.picker_props,
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
              this.tmpl('element_0', ...arguments),
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
          m('div.bx--form-requirement', null,
              this.tmpl('errors_0', ...arguments)),
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
              this.tmpl('element_1', ...arguments),
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
          m('div.bx--form-requirement', null,
              this.tmpl('errors_1', ...arguments)),
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
      'class': `bx--date-picker bx--date-picker--range ${values.picker_class}`,
      ...values.picker_props,
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
              this.tmpl('element_0', ...arguments),
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
              this.tmpl('element_1', ..arguments),
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
