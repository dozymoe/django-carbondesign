import m from 'mithril/hyperscript';
import DOMPurify from 'dompurify';
//-
import { Node, modify_svg } from './base';

export class DropDown extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['help', 'errors']
    CLASS_AND_PROPS = ['help']
    NODE_PROPS = ['value', 'disabled', 'up', 'light', 'inline']

    prepare(vnode, values, context)
    {
        values.value = vnode.attrs.value;

        if (vnode.attrs.disabled)
        {
            values['class'].push('bx--dropdown--disabled');
            values.props.push(['disabled', 'disabled']);
            values.label_class.push('bx--label--disabled');
            values.label_props.push(['aria-disabled', 'true']);
            values.help_class.push('bx--form__helper-text--disabled');
            values.help_props.push(['aria-disabled', 'true']);
            context.dropdown_disabled = true;
        }
        if (vnode.attrs.up)
        {
            values['class'].push('bx--dropdown--up');
        }
        if (vnode.attrs.light)
        {
            values['class'].push('bx--dropdown--light');
        }
        if (vnode.attrs.inline)
        {
            values['class'].push('bx--dropdown--inline');
            values.wrapper_class.push('bx--dropdown__wrapper--inline');
            values.wrapper_props.push(['data-dropdown-type', 'inline']);
        }
    }

    render_default(vnode, values, context)
    {
        if (this.slots.errors)
        {
            return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--dropdown__wrapper ${values.wrapper_class}`,
    },
    [
      m('span',
        {
          id: `label-${values.id}`,
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div',
        {
          'data-dropdown': '',
          'data-value': '',
          'class': `bx--dropdown bx--dropdown--invalid ${values['class']}`,
          'data-invalid': '',
          ...values.wrapper_props,
        },
        [
          m('button.bx--dropdown-text',
            {
              'aria-haspopup': true,
              'aria-expanded': false,
              'aria-controls': `menu-${values.id}`,
              'aria-labelledby': `label-${values.id} value-${values.id}`,
              type: 'button',
              ...values.props,
            },
            [
              m('svg',
                {
                  focusable: false,
                  preserveAspectRatio: 'xMidYMid meet',
                  xmlns: 'http://www.w3.org/2000/svg',
                  fill: 'currentColor',
                  'class': 'bx--dropdown__invalid-icon',
                  width: 16,
                  height: 16,
                  viewBox: '0 0 16 16',
                  'aria-hidden': true,
                },
                [
                  m('path',
                    {
                      d: 'M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,\
                          1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,\
                          0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,\
                          0.8S8.4,12.2,8,12.2z',
                    }),
                  m('path',
                    {
                      d: 'M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-\
                          0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,\
                          0.8S8.4,12.2,8,12.2z',
                      'data-icon-path': 'inner-path',
                      opacity: 0,
                    }),
                ]),
              m('span.bx--dropdown-text__inner',
                {
                  id: `value-${values.id}`,
                },
                values.value),
              m('span.bx--dropdown__arrow-container', null,
                m('svg',
                  {
                    focusable: false,
                    preserveAspectRatio: 'xMidYMid meet',
                    xmlns: 'http://www.w3.org/2000/svg',
                    fill: 'currentColor',
                    'class': 'bx--dropdown__arrow',
                    width: 16,
                    height: 16,
                    viewBox: '0 0 16 16',
                    'aria-hidden': true,
                  },
                  m('path',
                    {
                      d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
                    }))),
            ]),
          m('ul.bx--dropdown-list',
            {
              id: `menu-${values.id}`,
              role: 'menu',
              tabindex: -1,
              'aria-hidden': true,
              'aria-labelledby': `label-${values.id}`,
            },
            values.child),
        ]),
      this.slot('help', vnode, values, context),
      m('div.bx--form-requirement', null,
        this.slot('errors', vnode, values, context)),
    ]))
//##
            );
        }

        return (
//##
m('div.bx--form-item', null,
  m('div',
    {
      'class': `bx--dropdown__wrapper ${values.wrapper_class}`,
    },
    [
      m('span',
        {
          id: `label-${values.id}`,
          'class': `bx--label ${values.label_class}`,
          ...values.label_props,
        },
        values.label),
      m('div',
        {
          'data-dropdown': '',
          'data-value': '',
          'class': `bx--dropdown ${values['class']}`,
          ...values.wrapper_props,
        },
        [
          m('button.bx--dropdown-text',
            {
              'aria-haspopup': true,
              'aria-expanded': false,
              'aria-controls': `menu-${values.id}`,
              'aria-labelledby': `label-${values.id} value-${values.id}`,
              type: 'button',
              ...values.props,
            },
            [
              m('span.bx--dropdown-text__inner',
                {
                  id: `value-${values.id}`,
                },
                values.value),
              m('span.bx--dropdown__arrow-container', null,
                m('svg',
                  {
                    focusable: false,
                    preserveAspectRatio: 'xMidYMid meet',
                    xmlns: 'http://www.w3.org/2000/svg',
                    fill: 'currentColor',
                    'class': 'bx--dropdown__arrow',
                    width: 16,
                    height: 16,
                    viewBox: '0 0 16 16',
                    'aria-hidden': true,
                  },
                  m('path',
                    {
                      d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
                    }))),
            ]),
          m('ul.bx--dropdown-list',
            {
              id: `menu-${values.id}`,
              role: 'menu',
              tabindex: -1,
              'aria-hidden': true,
              'aria-labelledby': `label-${values.id}`,
            },
            values.child),
        ]),
      this.slot('help', vnode, values, context),
    ]))
//##
        );
    }

    render_slot_help(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--form__helper-text ${values.class}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class DropdownItem extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']
    NODE_PROPS = ['active', 'value']

    prepare(vnode, values, context)
    {
        values.value = vnode.attrs.value;

        if (vnode.attrs.active)
        {
            values.props.push(['aria-checked', 'true']);
        }
        else
        {
            values.props.push(['aria-checked', 'false']);
            values.props.push(['tabindex', '-1']);
        }

        if (context.dropdown_disabled)
        {
            values.props.push(['tabindex', '-1']);
        }
    }

    render_default(vnode, values, context)
    {
        let cleaned_child = DOMPurify.sanitize(values.child);

        return (
//##
m('li',
  {
    'data-option': '',
    'data-value': values.value,
    'class': `bx--dropdown-item ${values['class']}`,
    title: cleaned_child,
  },
  [
    m('a.bx--dropdown-link',
      {
        role: 'menuitemradio',
        id: `item-${values.id}`,
        ...values.props,
      },
      values.child),
    this.slot('icon', vnode, values, context),
  ])
//##
        );
    }

    render_slot_icon(vnode, values, context)
    {
        return modify_svg(values.child,
            {
                'focusable': false,
                'preserveAspectRatio': 'xMidYMid meet',
                'fill': 'currentColor',
                'class': `bx--list-box__menu-item__selected-icon ${values['class']}`,
                'style': {
                    'will-change': 'transform',
                    width: '16px',
                    height: '16px',
                },
                'aria-hidden': true,
            })
    }
}
