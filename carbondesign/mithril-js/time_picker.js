import m from 'mithril/hyperscript';
//-
import { FormNode, render_errors } from './base';

class BaseSelectFormNode extends FormNode
{
    prepare(vnode, values, context)
    {
        values.props.push(['id', values.id]);
        values.props.push(['name', this.bound_field.name]);

        required = this.bound_field.field.required &&
                this.bound_field.form.use_required_attribute;
        if (required)
        {
            values.props.push(['required', '']);
        }
    }

    render_tmpl_icon_error(vnode, values, context)
    {
        return (
//##
m('svg.bx--select__invalid-icon',
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
  [
    m('path',
      {
        d: 'M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z \
            M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2 c-0.4,0-0.8-\
            0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,\
            12.2,8,12.2z',
      }),
    m('path',
      {
        d: 'M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-\
            0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,\
            12.2,8,12.2z',
        'data-icon-path': 'inner-path',
        opacity: 0,
      }),
  ])
//##
        );
    }

    render_tmpl_items(vnode, values, context)
    {
        let items = [];

        for (let [_, val, txt] of this.choices(vnode))
        {
            let props = {};
            if (this.boundValue && this.boundValue.indexOf(val) != -1)
            {
                props.selected = '';
            }
            items.push(
//##
m('option.bx--select-option', {value: val, ...props}, txt)
//##
            );
        }

        if (items.length)
        {
            return m.fragment(null, items);
        }
    }
}

class AmPmPicker extends BaseSelectFormNode
{
    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div',
  {
    'class': `bx--time-picker__select bx--select bx--select--invalid ${values.class}`,
    'data-invalid': '',
  },
  [
    this.tmpl('label', ...arguments),
    m('select.bx--select-input', props, this.tmpl('items', ...arguments)),
    m('svg.bx--select__arrow',
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
          d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
        })),
    this.tmpl('icon_error', ...arguments),
  ])
//##
            );
        }

        return (
//##
m('div',
  {
    'class': `bx--time-picker__select bx--select ${values.class}`,
  },
  [
    this.tmpl('label', ...arguments),
    m('select.bx--select-input', props, this.tmpl('items', ...arguments)),
    m('svg.bx--select__arrow',
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
          d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
        })),
  ])
//##
        );
    }
}

class TimezonePicker extends BaseSelectFormNode
{
    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div',
  {
    'class': `bx--time-picker__select bx--select bx--select--invalid ${values.class}`,
    'data-invalid': '',
  },
  [
    this.tmpl('label', ...arguments),
    m('select.bx--select-input', props, this.tmpl('items', ...arguments)),
    m('svg.bx--select__arrow',
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
          d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
        })),
    this.tmpl('icon_error', ...arguments),
  ])
//##
            );

        return (
//##
m('div',
  {
    'class': `bx--time-picker__select bx--select ${values.class}`,
  },
  [
    this.tmpl('label', ...arguments),
    m('select.bx--select-input', props, this.tmpl('items', ...arguments)),
    m('svg.bx--select__arrow',
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
          d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
        })),
  ])
//##
        );
    }
}

export class TimePicker extends FormNode
{
    NODE_PROPS = ['light', 'ampm', 'tzinfo']

    prepare(vnode, values, context)
    {
        let child_class = [];
        let child_props = {};

        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.props.push(['disabled', '']);
            child_props.disabled = '';
        }

        if (vnode.attrs.light)
        {
            values['class'].push('bx--time-picker--light');
            child_class.push('bx--select--light');
        }

        if (child_class.length)
        {
            child_props['class'] = child_class.join(' ');
        }

        this.nodelist = [];

        if (vnode.attrs.ampm)
        {
            this.nodelist.push(new AmPmPicker(Object.assign(
                    {field: vnode.attrs.ampm}, child_props)))
        }

        if (vnode.attrs.tzinfo)
        {
            this.nodelist.push(new TimezonePicker(Object.assign(
                    {field: vnode.attrs.tzinfo}, child_props)))
        }
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--text-input');
        props['class'].push('bx--time-picker__input-field');
        props.pattern = '(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\\\s)?';
        props.placeholder = 'hh:mm';
        props.maxlength = '5'

        if (vnode.attrslight)
        {
            props['class'].push('bx--text-input--light');
        }
    }

    render_default(vnode, values, context)
    {
        let light = vnode.attrs.light;
        if (this.bound_field.errors)
        {
            if (light)
            {
                return (
//##
m('div.bx--form-item', null,
  [
    m('div',
      {
        'class': `bx--time-picker ${values.class}`,
        'data-invalid': '',
      },
      [
        m('div.bx--time-picker__input', null,
          [
            this.tmpl('label', ...arguments),
            this.tmpl('element', ...arguments),
          ]),
        values.child,
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
    m('div',
      {
        'class': `bx--time-picker ${values.class}`,
        'data-invalid': '',
      },
      [
        m('div.bx--time-picker__input', null,
            this.tmpl('element', ...arguments)),
        values.child,
      ]),
    m('div.bx--form-requirement', null, this.tmpl('errors', ...arguments)),
    this.tmpl('help', ...arguments),
  ])
//##
        }
        if (light && vnode.attrs.disabled)
        {
            return (
//##
m('div.bx--form-item', null,
  [
    m('div',
      {
        'class': `bx--time-picker ${values.class}`,
      },
      [
        m('div.bx--time-picker__input', null,
          [
            this.tmpl('label', ...arguments),
            this.tmpl('element', ...arguments),
          ]),
        values.child,
      ]),
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
    m('div',
      {
        'class': `bx--time-picker ${values.class}`,
      },
      [
        m('div.bx--time-picker__input', null,
            this.tmpl('element', ...arguments)),
        values.child,
      ]),
    this.tmpl('help', ...arguments),
  ])
//##
        );
    }

    render_tmpl_errors(vnode, values, context)
    {
        let bound_fields = [this.bound_field];
        if (vnode.attrs.ampm)
        {
            bound_fields.push(vnode.attrs.ampm);
        }
        if (vnode.attrs.tzinfo)
        {
            bound_fields.push(vnode.attrs.tzinfo);
        }
        return render_errors(bound_fields);
    }
}
