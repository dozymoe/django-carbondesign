import m from 'mithril/hyperscript';
//-
import { FormNode, Node } from './base';

export class ComboBox extends FormNode
{
    WANT_CHILDREN = true
    NODE_PROPS = ['light']

    prepare(vnode, values, context)
    {
        values.txt_open = gettext("Open menu");
        values.txt_clear = gettext("Clear all");

        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.help_class.push('bx--form__helper-text--disabled');
            values.wrapper_class.push('bx--list-box--disabled');
            values.wrapper_props.push(['disabled', 'disabled']);
            values.props.push(['disabled', 'disabled']);
        }

        if (vnode.attrs.light)
        {
            values.wrapper_class.push('bx--list-box--light');
        }
    }

    prepare_element_props(vnode, props, default_props, context)
    {
        props['class'].push('bx--text-input');
        props['aria-autocomplete'] = 'list';
        props['aria-expanded'] = 'false';
        props['autocomplete'] = 'off';
        props['aria-owns'] = `menu-${this.id(context)}`;
    }

    render_default(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div.bx--list-box__wrapper', null,
    [
      this.tmpl('label', ...arguments),
      m('div',
        {
          'class': `bx--combo-box bx--list-box ${values.wrapper_class}`,
          'data-invalid': '',
        },
        [
          m('div.bx--list-box__field',
            {
              role: 'combobox',
              'aria-label': values.txt_open,
              'aria-expanded': false,
              'aria-haspopup': 'listbox',
              ...values.wrapper_props,
            },
            [
              values.element,
              this.tmpl('icon_invalid', ...arguments),
              this.tmpl('icon_clear', ...arguments),
              this.tmpl('icon_menu', ...arguments),
            ]),
          m('ul.bx--list-box__menu',
            {
              role: 'listbox',
              id: `menu-${values.id}`,
              'aria-label': values.label,
            },
            values.child),
        ]),
      this.tmpl('help', ...arguments),
      m('div.bx--form-requirement', null, values.form_errors),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div.bx--list-box__wrapper', null,
    [
      this.tmpl('label', ...arguments),
      m('div',
        {
          'class': `bx--combo-box bx--list-box ${values.wrapper_class}`,
        },
        [
          m('div.bx--list-box__field',
            {
              role: 'combobox',
              'aria-label': values.txt_open,
              'aria-expanded': false,
              'aria-haspopup': 'listbox',
              ...values.wrapper_props,
            },
            [
              values.element,
              this.tmpl('icon_clear', ...arguments),
              this.tmpl('icon_menu', ...arguments),
            ]),
          m('ul.bx--list-box__menu',
            {
              role: 'listbox',
              id: `menu-${values.id}`,
              'aria-label': values.label,
            },
            values.child),
        ]),
      this.tmpl('help', ...arguments),
    ]))
//##
        );
    }

    render_tmpl_label(vnode, values, context)
    {
        return (
//##
m('label',
  {
    'for': values.id,
    'class': `bx--label ${values.label_class}`,
    ...values.label_props,
  },
  values.label)
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
    xmlns: 'http://www.w3.org/2000/svg',
    fill: 'currentColor',
    'class': 'bx--list-box__invalid-icon',
    width: 16,
    height: 16,
    viewBox: '0 0 16 16',
    'aria-hidden': true,
  },
  [
    m('path',
      {
        d: 'M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,\
            4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.\
            3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z',
      }),
    m('path',
      {
        d: 'M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-\
            0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z',
        'data-icon-path': 'inner-path',
        opacity: 0,
      }),
  ])
//##
        );
    }

    render_tmpl_icon_menu(vnode, values, context)
    {
        return (
//##
m('div.bx--list-box__menu-icon',
  m('svg',
    {
      focusable: false,
      preserveAspectRatio: 'xMidYMid meet',
      xmlns: 'http://www.w3.org/2000/svg',
      fill: 'currentColor',
      'aria-label': values.txt_open,
      width: 16,
      height: 16,
      viewBox: '0 0 16 16',
      role: 'img',
    },
    m('path', {d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z'})))
//##
        );
    }

    render_tmpl_icon_clear(vnode, values, context)
    {
        return (
//##
m('div.bx--list-box__selection',
  {
    role: 'button',
  },
  m('svg',
    {
      focusable: false,
      preserveAspectRatio: 'xMidYMid meet',
      xmlns: 'http://www.w3.org/2000/svg',
      fill: 'currentColor',
      title: values.txt_clear,
      'aria-label': values.txt_clear,
      width: 16,
      height: 16,
      viewBox: '0 0 32 32',
      role: 'img',
    },
    m('path',
      {
        d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 \
            22.6 24 24 22.6 17.4 16 24 9.4z',
      })))
//##
        );
    }
}


export class ComboBoxItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['active']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.active)
        {
            values['class'].push('bx--list-box__menu-item--highlighted');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('li',
  {
    'class': `bx--list-box__menu-item ${values['class']}`,
    ...values.props,
  },
  m('div.bx--list-box__menu-item__option',
    {
      tabindex: 0,
    },
    values.child))
//##
        );
    }
}
