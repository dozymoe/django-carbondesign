import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';
import timezones from './timezones.json';

export class TimePicker extends FormNode
{
    NODE_PROPS = ['light']

    prepare(vnode, values, context)
    {
        values.txt_select_ampm = gettext("Select AM/PM");
        values.txt_select_zone = gettext("Select time zone");

        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.props.push(['disabled', '']);
            values.select_props = 'disabled';
        }
        else
        {
            values.select_props = '';
        }

        if (vnode.attrs.light)
        {
            values['class'].push('bx--time-picker--light');
            values.select_class = 'bx--select--light';
        }
        else
        {
            values.select_class = '';
        }
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--text-input');
        props['class'].push('bx--time-picker__input-field');
        props.pattern = '(1[012]|[1-9]):[0-5][0-9](\\\\s)?';
        props.placeholder = 'hh:mm';
        props.maxlength = '5'

        if (vnode.attrslight)
        {
            props['class'].push('bx--text-input--light');
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
        'class': `bx--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    m('div',
      {
        'class': `bx--time-picker ${values['class']}`,
        'data-invalid': '',
      },
      [
        m('div.bx--time-picker__input', null, values.element),
        this.tmpl('select_ampm', vnode, values, context),
        this.tmpl('select_zone', vnode, values, context),
      ]),
    m('div.bx--form-requirement', null, values.form_errors),
    this.tmpl('help', vnode, values, context),
  ])
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
        'class': `bx--label ${values.label_class}`,
        ...values.label_props,
      },
      values.label),
    m('div',
      {
        'class': `bx--time-picker ${values['class']}`,
      },
      [
        m('div.bx--time-picker__input', null, values.element),
        this.tmpl('select_ampm', vnode, values, context),
        this.tmpl('select_zone', vnode, values, context),
      ])
    this.tmpl('help', vnode, values, context),
  ])
//##
        );
    }

    render_tmpl_select_ampm(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--time-picker__select bx--select ${values.select_class}`,
  },
  [
    m('label',
      {
        'for': `select-ampm-${values.id}`,
        'class': 'bx--label bx--visually-hidden',
      },
      values.txt_select_ampm),
    m('select',
      {
        id: `select-ampm-${values.id}`,
        'class': 'bx--select-input',
        ...values.select_props,
      },
      [
        m('option.bx--select-option', null, "AM"),
        m('option.bx--select-option', null, "PM"),
      ]),
    m('svg',
      {
        focusable: false,
        preserveAspectRatio: 'xMidYMid meet',
        xmlns: 'http://www.w3.org/2000/svg',
        fill: 'currentColor',
        'class': 'bx--select__arrow',
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

    render_tmpl_select_zone(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--time-picker__select bx--select ${values.select_class}`,
  },
  [
    m('label',
      {
        'for': `select-zone-${values.id}`,
        'class': 'bx--label bx--visually-hidden',
      },
      values.txt_select_zone),
    m('select',
      {
        id: `select-zone-${values.id}`,
        'class': 'bx--select-input',
        ...values.select_props,
      },
      this.tmpl('timezones', vnode, values, context)),
    m('svg',
      {
        focusable: false,
        preserveAspectRatio: 'xMidYMid meet',
        xmlns: 'http://www.w3.org/2000/svg',
        fill: 'currentColor',
        'class': 'bx--select__arrow',
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

    render_tmpl_timezones(vnode, values, context)
    {
        items = []
        for (let zone of timezones)
        {
            items.append(m('option.bx--select-option', null, zone));
        }
        return m.fragment(null, items)
    }
}
