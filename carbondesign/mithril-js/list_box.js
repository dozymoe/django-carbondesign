import m from 'mithril/hyperscript';
//-
import { FormNode, Node } from './base';

export class ListBox extends FormNode
{
    WANT_CHILDREN = true
    MODES = ['default', 'inline']
    NODE_PROPS = ['light']

    prepare(vnode, values, context)
    {
        values.txt_open = gettext("Open menu");

        if (vnode.attrs.disabled)
        {
            values.label_class.push('bx--label--disabled');
            values.help_class.push('bx--form__helper-text--disabled');
            values.wrapper_class.push('bx--list-box--disabled');
            values.props.push(['disabled', 'disabled']);
        }
        if (vnode.attrs.light)
        {
            values.wrapper_class.push('bx--list-box--light');
        }
    }

    prepare_element_props(vnode, values, context)
    {
        props['class'].append('bx--text-input');
        props['aria-autocomplete'] = 'list';
        props['aria-expanded'] = false;
        props.autocomplete = 'off';
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
      this.tmpl('label', vnode, values, context),
      m('div',
        {
          'class': `bx--list-box ${values.wrapper_class}`,
          'data-invalid': '',
        },
        [
          this.tmpl('icon_invalid', vnode, values, context),
          m('div',
            {
              role: 'button',
              'class': 'bx--list-box__field',
              tabindex: 0,
              'aria-label': values.txt_open,
              'aria-expanded': false,
              'aria-haspopup': true,
            },
            [
              m('span.bx--list-box__label', null, values.value),
              this.tmpl('icon_menu', vnode, values, context),
            ]),
          m('ul.bx--list-box__menu',
            {
              role: 'combobox',
              id: `menu-${values.id}`,
            },
            values.child),
        ]),
      this.tmpl('help', vnode, values, context),
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
      this.tmpl('label', vnode, values, context),
      m('div',
        {
          'class': `bx--list-box ${values.wrapper_class}`,
        },
        [
          m('div',
            {
              role: 'button',
              'class': 'bx--list-box__field',
              tabindex: 0,
              'aria-label': values.txt_open,
              'aria-expanded': false,
              'aria-haspopup': true,
            },
            [
              m('span.bx--list-box__label', null, values.value),
              this.tmpl('icon_menu', vnode, values, context),
            ]),
          m('ul.bx--list-box__menu',
            {
              role: 'combobox',
              id: `menu-${values.id}`,
            },
            values.child),
        ]),
      this.tmpl('help', vnode, values, context),
    ]))
//##
        );
    }

    render_inline(vnode, values, context)
    {
        if (this.bound_field.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div.bx--list-box__wrapper.bx--list-box__wrapper--inline', null,
    [
      this.tmpl('label', vnode, values, context),
      m('div',
        {
          'class': `bx--list-box bx--list-box--inline ${values.wrapper_class}`,
          'data-invalid': '',
        },
        [
          this.tmpl('icon_invalid', vnode, values, context),
          m('div',
            {
              role: 'button',
              'class': 'bx--list-box__field',
              tabindex: 0,
              'aria-label': values.txt_open,
              'aria-expanded': false,
              'aria-haspopup': true,
            },
            [
              m('span.bx--list-box__label', null, values.value),
              this.tmpl('icon_menu', vnode, values, context),
            ]),
          m('ul.bx--list-box__menu',
            {
              role: 'combobox',
              id: `menu-${values.id}`,
            },
            values.child),
        ]),
      this.tmpl('help', vnode, values, context),
      m('div.bx--form-requirement', null, values.form_errors),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div.bx--list-box__wrapper.bx--list-box__wrapper--inline', null,
    [
      this.tmpl('label', vnode, values, context),
      m('div',
        {
          'class': `bx--list-box bx--list-box--inline ${values.wrapper_class}`,
        },
        [
          m('div',
            {
              role: 'button',
              'class': 'bx--list-box__field',
              tabindex: 0,
              'aria-label': values.txt_open,
              'aria-expanded': false,
              'aria-haspopup': true,
            },
            [
              m('span.bx--list-box__label', null, values.value),
              this.tmpl('icon_menu', vnode, values, context),
            ]),
          m('ul.bx--list-box__menu',
            {
              role: 'combobox',
              id: `menu-${values.id}`,
            },
            values.child),
        ]),
      this.tmpl('help', vnode, values, context),
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
            4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-\
            0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z',
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
m('div.bx--list-box__menu-icon', null,
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
    m('path',
      {
        d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
      })))
//##
        );
    }
}


export class ListBoxItem extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['active']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.active)
        {
            values['class'].push('bx--list-box__menu-item--active');
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
    [
      values.child,
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          'aria-hidden': true,
          'class': 'bx--list-box__menu-item__selected-icon',
          width: 16,
          height: 16,
          viewBox: '0 0 32 32',
        },
        m('path',
          {
            d: 'M13 24L4 15 5.414 13.586 13 21.171 26.586 7.586 28 9 13 24z',
          })),
    ]))
//##
        );
    }
}
