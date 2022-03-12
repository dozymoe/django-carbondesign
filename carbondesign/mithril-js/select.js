import m from 'mithril/hyperscript';
//-
import { FormNode } from './base';

export class Select extends FormNode
{
    MODEs = ['default', 'inline']
    NODE_PROPS = ['light']
    RENDER_ELEMENT = false

    prepare(vnode, values, context)
    {
        values.txt_choose = gettext("Choose an option");

        values.props.push(['id', values.id]);
        values.props.push(['name', this.bound_field.name]);

        this.required = this.bound_field.field.required &&
                this.bound_field.form.use_required_attribute;
        if (this.required)
        {
            values.props.push(['required', '']);
        }

        if (this.bound_field.field.disabled)
        {
            values.props.push(['disabled', '']);
            values.label_class.push('bx--label--disabled');
            values.wrapper_class.push('bx--select--disabled');
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
      'class': `bx--select bx--select--invalid ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    [
      m('label',
        {
          'for': values.id,
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div.bx--select-input__wrapper', null,
        [
          m('select',
            {
              'class': `bx--select-input ${values['class']}`,
              ...values.props,
            },
            this.tmpl('items', vnode, values, context)),
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
            m('path'
              {
                d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
              })),
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
            ]),
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
      'class': `bx--select ${values.wrapper_class}`,
    },
    [
      m('label',
        {
          'for': values.id,
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div.bx--select-input__wrapper', null,
        [
          m('select',
            {
              'class': `bx--select-input ${values['class']}`,
              ...values.props,
            },
            this.tmpl('items', vnode, values, context)),
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
      'class': `bx--select bx--select--inline bx--select--invalid ${values.wrapper_class}`,
      ...values.wrapper_props,
    },
    [
      m('label',
        {
          'for': values.id,
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div.bx--select-input--inline__wrapper', null,
        [
          m('select',
            {
              'class': `bx--select-input ${values['class']}`,
              ...values.props,
            },
            this.tmpl('items', vnode, values, context)),
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
            m('path'
              {
                d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
              })),
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
            ]),
        ]),
      m('div.bx--form-requirement', null, values.form_errors),
      this.tmpl('help', vnode, values, context),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--select bx--select-inline ${values.wrapper_class}`,
    },
    [
      m('label',
        {
          'for': values.id,
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div.bx--select-input__wrapper', null,
        [
          m('select',
            {
              'class': `bx--select-input ${values['class']}`,
              ...values.props,
            },
            this.tmpl('items', vnode, values, context)),
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

    render_tmpl_items(vnode, values, context)
    {
        let values = this.bound_field.value();

        let items = [], group_items = [], group_name;
        if (!this.required)
        {
            items.push(
//##
m('option.bx--select-option', {value: ''}, values.txt_choose)
//##
            );
        }

        for (let [group, val, txt] of this.choices(context))
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
            if (values.indexOf(vl) != -1)
            {
                props.selected = '';
            }
            let current_items = group ? group_items : normal_items;
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
