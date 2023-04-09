import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class Select extends FormNode
{
    MODEs = ['default', 'inline']
    NODE_PROPS = ['light']
    CLASS_AND_PROPS = ['label', 'help', 'select']

    prepare(vnode, values, context)
    {
        values.txt_choose = gettext("Choose an option");

        values.props.push(['id', values.id]);
        values.props.push(['name', this.bound_field.name]);

        required = this.bound_field.field.required &&
                this.bound_field.form.use_required_attribute;
        if (required)
        {
            values.props.push(['required', '']);
        }

        if (vnode.attrs.disabled)
        {
            values.props.push(['disabled', '']);
            values.label_class.push('bx--label--disabled');
            values.select_class.push('bx--select--disabled');
        }

        if (vnode.attrs.light)
        {
            values.select_class.push('bx--select--light');
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
      'class': `bx--select bx--select--invalid ${values.select_class}`,
      ...values.select_props,
    },
    [
      this.tmpl('label', ...arguments),
      m('div.bx--select-input__wrapper',
        {
          'data-invalid': '',
        },
        [
          m('select',
            {
              'class': `bx--select-input ${values['class']}`,
              ...values.props,
            },
            this.tmpl('items', ...arguments)),
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
        ]),
      m('div.bx--form-requirement', null, this.tmpl('errors', ...arguments)),
      this.tmpl('help', ...arguments),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--select ${values.select_class}`,
       ...values.select_props,
    },
    [
      this.tmpl('label', ...arguments),
      m('div.bx--select-input__wrapper', null,
        [
          m('select',
            {
              'class': `bx--select-input ${values['class']}`,
              ...values.props,
            },
            this.tmpl('items', ...arguments)),
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
  m('div',
    {
      'class': `bx--select bx--select--inline bx--select--invalid ${values.select_class}`,
      ...values.select_props,
    },
    [
      this.tmpl('label', ...arguments),
      m('div.bx--select-input--inline__wrapper', null,
        [
          m('select',
            {
              'class': `bx--select-input ${values['class']}`,
              ...values.props,
            },
            this.tmpl('items', ...arguments)),
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
        ]),
      m('div.bx--form-requirement', null, this.tmpl('errors', ...arguments)),
      this.tmpl('help', ...arguments),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--select bx--select-inline ${values.select_class}`,
      ...values.select_props,
    },
    [
      this.tmpl('label', ...arguments),
      m('div.bx--select-input--inline__wrapper', null,
        m('div.bx--select-input__wrapper', null,
          [
            m('select',
              {
                'class': `bx--select-input ${values['class']}`,
                ...values.props,
              },
              this.tmpl('items', ...arguments)),
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
          ])),
      this.tmpl('help', ...arguments),
    ]))
//##
        );
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
        let items = [], group_items = [], group_name;
        items.push(
//##
m('option.bx--select-option', {value: ''}, values.txt_choose)
//##
        );

        for (let [group, val, txt] of this.choices(vnode))
        {
            if (group && group != group_name)
            {
                if (group_items.length)
                {
                    items.push(
//##
m('optgroup.bx--select-optgroup', {label: group_name}, group_items)
//##
                    );
                }
                group_name = group;
                group_items = [];
            }
            let props = {};
            if (this.boundValue && this.boundValue.indexOf(val) != -1)
            {
                props.selected = '';
            }
            let current_items = group ? group_items : items;
            current_items.push(
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
