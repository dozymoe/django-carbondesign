import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class MultiSelect extends FormNode
{
    MODES = ['default', 'inline', 'filterable']
    NODE_PROPS = ['light']

    prepare(vnode, values, context)
    {
        values.txt_open = gettext("Open menu");
        values.txt_close = gettext("Close menu");
        values.txt_multi = gettext("Multi select options");
        values.txt_clear = gettext("Clear all selected items");
        values.txt_clear_num = gettext("Clear selection");
        values.txt_filter = gettext("Filter...");

        values.values_count = this.bound_field.value().length;

        if (vnode.attrs.light)
        {
            values.wrapper_class.push('bx--list-box-light');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item', null,
  m('div.bx--list-box__wrapper', null,
    [
      m('label',
        {
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div',
        {
          'class': `bx--multi-select bx--list-box ${values.wrapper_class}`,
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
              m('span.bx--list-box__label', null, values.txt_multi),
              this.tmpl('icon_menu', vnode, values, context),
            ]),
          m('fieldset.bx--list-box__menu',
            {
              role: 'listbox',
            },
            [
              m('legend.bx--assistive-text', null, values.label),
              this.tmpl('items', vnode, values, context),
            ]),
        ]),
      this.tmpl('help', vnode, values, context),
    ]))
//##
        );
    }

    render_filterable(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item', null,
  m('div.bx--list-box__wrapper', null,
    [
      m('label',
        {
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div',
        {
          'class': `bx--multi-select bx--list-box bx--combo-box bx--multi-select-filterable ${values.wrapper_class}`,
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
              m('input.bx--text-input',
                {
                  placeholder: values.txt_filter,
                }),
              this.tmpl('icon_menu', vnode, values, context),
            ]),
          m('fieldset.bx--list-box__menu',
            {
              role: 'listbox',
            },
            [
              m('legend.bx--assistive-text', null, values.label),
              this.tmpl('items', vnode, values, context),
            ]),
        ]),
      this.tmpl('help', vnode, values, context),
    ]))
//##
        );
    }

    render_inline(vnode, values, context)
    {
        return (
//##
m('div.bx--form-item', null,
  m('div.bx--list-box__wrapper.bx--list-box__wrapper--inline', null,
    [
      m('label',
        {
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div',
        {
          'class': `bx--multi-select bx--list-box bx--list-box--inline ${values.wrapper_class}`,
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
              m('span.bx--list-box__label', null, values.txt_multi),
              this.tmpl('icon_menu', vnode, values, context),
            ]),
          m('fieldset.bx--list-box__menu',
            {
              role: 'listbox',
            },
            [
              m('legend.bx--assistive-text', null, values.label),
              this.tmpl('items', vnode, values, context),
            ]),
        ]),
      this.tmpl('help', vnode, values, context),
    ]))
//##
        );
    }

    render_tmpl_icon_clear(vnode, values, context)
    {
        return (
//##
m('div',
  {
    role: 'button',
    'class': 'bx--list-box__selection bx--list-box__selection--multi bx--tag--filter',
    tabindex: 0,
    title: values.txt_clear,
  },
  [
    values_count,
    m('svg',
      {
        focusable: false,
        preserveAspectRatio: 'xMidYMid meet',
        xmlns: 'http://www.w3.org/2000/svg',
        fill: 'currentColor',
        'aria-label': values.txt_clear_num,
        width: 16,
        height: 16,
        viewBox: '0 0 32 32',
        role: 'img',
      },
      m('path',
        {
          d: 'M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 \
              17.4 22.6 24 24 22.6 17.4 16 24 9.4z',
        })),
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

    render_tmpl_items(vnode, values, context)
    {
        let values = this.bound_field.value();

        let items = [], ii = 0;
        for (let [group, val, txt] of this.choices(context))
        {
            let props = {};
            if (values.indexOf(val) != -1)
            {
                props['checked'] = '';
            }
            items.push(
//##
m('div.bx--list-box__menu-item', null,
  m('div.bx--list-box__menu-item__option', null,
    m('div.bx--form-item.bx--checkbox-wrapper', null,
      m('label',
        {
          title: txt,
          'class': 'bx--checkbox-label',
        },
        [
          m('input',
            {
              type: 'checkbox',
              name: this.bound_field.name,
              readonly: '',
              'class': 'bx--checkbox',
              id: `${values.id}-${ii}`,
              value: val,
              ...props,
            }),
          m('span.bx--checkbox-appearance'),
          m('span.bx--checkbox-label-text', null, values.child),
        ]))))
//##
            );
            ii++;
        }

        if (items.length)
        {
            return m.fragment(null, items);
        }
    }
}
