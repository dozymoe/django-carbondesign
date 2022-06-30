import { uniqueId } from 'lodash';
import m from 'mithril/hyperscript';
import m_tostring from 'mithril-node-render';
//-
import { FormNode, Node, clean_attr_value, modify_svg } from './base';
import { Button } from './button';

export class Table extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['title', 'description', 'batch_actions', 'search',
            'toolbar_actions', 'toolbar_overflow', 'head', 'foot', 'pagination']
    MODES = ['default', 'sticky']
    NODE_PROPS = ['variant', 'sortable', 'small_toolbar', 'batch_field',
            'visible_overflow']
    CLASS_AND_PROPS = ['toolbar']
    POSSIBLE_VARIANT = ['compact', 'short', 'tall', 'zebra']
    PAGER_SIZES = [10, 20, 30, 40, 50]

    prepare(vnode, values, context)
    {
        values.txt_batch_actions = gettext("Table Action Bar")
        values.txt_items_selected = gettext("items selected")
        values.txt_overflow = gettext("Overflow")

        if (vnode.attrs.variant)
        {
            values['class'].push(`bx--data-table--${vnode.attrs.variant}`);
        }
        if (vnode.attrs.compact)
        {
            context.compact = true;
        }

        if (vnode.attrs.sortable)
        {
            values['class'].push('bx--data-table--sort');
        }

        if (vnode.attrs.variant === 'compact' || vnode.attrs.small_toolbar)
        {
            values.toolbar_class.push('bx--table-toolbar--small');

            this.set_child_props(context, 'button_props', 'batch_actions',
                    {small: true});
            this.set_child_props(context, 'search_props', null, {small: true});
            this.set_child_props(context, 'button_props', 'toolbar',
                    {small: true});
        }

        if (vnode.attrs.visible_overflow)
        {
            values['class'].push('bx--data-table--visible-overflow-menu');
        }
    }

    render_default(vnode, values, context, slots)
    {
        if (this.has_tmpl_header() || this.has_tmpl_toolbar())
        {
            return (
//##
m('div.bx--data-table-container',
  {
    'data-table': '',
  },
  [
    this.tmpl('header', ...arguments),
    this.tmpl('toolbar', ...arguments),
    m('table',
      {
        'class': `bx--data-table ${values['class']}`,
        ...values.props,
      },
      [
        this.slot('head', ...arguments),
        values.child,
        this.slot('foot', ...arguments),
      ]),
    this.slot('pagination', ...arguments),
  ])
//##
            );
        }

        return (
//##
m.fragment(null,
  [
    m('table',
      {
        'class': `bx--data-table ${values['class']}`,
        ...values.props,
      },
      [
        this.slot('head', ...arguments),
        values.child,
        this.slot('foot', ...arguments),
      ]),
    this.slot('pagination', ...arguments),
  ])
//##
        );
    }

    render_sticky(vnode, values, context, slots)
    {
        if (this.has_tmpl_header() || this.has_tmpl_toolbar())
        {
            return (
//##
m('div.bx--data-table-container',
  {
    'data-table': '',
  },
  [
    this.tmpl('header', ...arguments),
    this.tmpl('toolbar', ...arguments),
    m('section.bx--data-table_inner-container', null,
      m('table',
        {
          'class': `bx--data-table bx--data-table--sticky-header ${values['class']}`,
          ...values.props,
        },
        [
          this.slot('head', ...arguments),
          values.child,
          this.slot('foot', ...arguments),
        ])),
    this.slot('pagination', ...arguments),
  ])
//##
            );
        }

        return (
//##
m.fragment(null,
  [
    m('section.bx--data-table_inner-container', null,
      m('table',
        {
          'class': `bx--data-table bx--data-table--sticky-header ${values['class']}`,
          ...values.props,
        },
        [
          this.slot('head', ...arguments),
          values.child,
          this.slot('foot', ...arguments),
        ])),
    this.slot('pagination', ...arguments),
  ])
//##
        );
    }

    render_slot_head(vnode, values, context)
    {
        return (
//##
m('thead', {'class': values['class'], ...values.props}, values.child)
//##
        );
    }

    render_slot_foot(vnode, values, context)
    {
        return (
//##
m('tfoot', {'class': values['class'], ...values.props}, values.child)
//##
        );
    }

    render_slot_title(vnode, values, context)
    {
        return (
//##
m('h4',
  {
    'class': `bx--data-table-header__title ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_slot_description(vnode, values, context)
    {
        return (
//##
m('p',
  {
    'class': `bx--data-table-header__description ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_slot_batch_actions(vnode, values, context)
    {
        let form_field = vnode.attrs.batch_field;
        let count = form_field && form_field.value() ?
                form_field.value().length : 0;
        return (
//##
m('div',
  {
    'class': `bx--batch-actions ${values['class']}`,
    'aria-label': values.txt_batch_actions,
    ...values.props,
  },
  [
    m('div.bx--action-list', null,
      [
          values.child,
          m(Button,
            {
              variant: 'primary',
              'data-event': 'action-bar-cancel',
              'class': 'bx--batch-summary__cancel',
              'small': context.compact,
            },
            values.txt_cancel),
      ]),
    m('div.bx--batch-summary', null,
      m('p.bx--batch-summary__para', null,
        [
          m('span', {'data-items-selected': count}),
          values.txt_items_selected,
        ])),
  ])
//##
        );
    }

    render_slot_toolbar_overflow(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--overflow-menu bx--toolbar-action ${values['class']}`,
    'data-overflow-menu': '',
    role: 'button',
    tabindex: 0,
    'aria-label': values.txt_overflow,
    'aria-haspopup': true,
    'aria-expanded': false,
    ...values.props,
  },
  [
    m('svg.bx--toolbar-action__icon',
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
            d: 'M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,\
                0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,\
                0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,\
                9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,\
                3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,\
                1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,\
                0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,\
                13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,\
                1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.\
                2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,\
                0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z \
                M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.\
                4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.\
                5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,\
                2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,\
                1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z',
          }),
        m('path',
          {
            d: 'M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,\
                11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,\
                0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.\
                1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z',
          }),
      ]),
    m('ul.bx--overflow-menu-options.bx--overflow-menu--flip',
      {
        tabindex: -1,
        role: 'menu',
        'aria-label': values.txt_overflow,
        'data-floating-menu-direction': 'bottom',
      },
      values.child),
  ])
//##
        );
    }

    has_tmpl_header()
    {
        return this.slots.title || this.slots.description;
    }

    render_tmpl_header(vnode, values, context)
    {
        if (!this.has_tmpl_header())
        {
            return;
        }
        return (
//##
m('div.bx--data-table-header', null,
  [
    this.slot('title', ...arguments),
    this.slot('description', ...arguments),
  ])
//##
        );
    }

    has_tmpl_toolbar()
    {
        return this.slots.batch_actions || this.slots.toolbar_overflow ||
                this.slots.toolbar_actions;
    }

    render_tmpl_toolbar(vnode, values, context)
    {
        if (!this.has_tmpl_toolbar())
        {
            return;
        }
        return (
//##
m('section',
  {
    'class': `bx--table-toolbar ${values.toolbar_class}`,
    ...values.toolbar_props,
  },
  [
    this.slot('batch_actions', ...arguments),
    m('div.bx--toolbar-content', null,
      [
        this.slot('search', ...arguments),
        this.slot('toolbar_overflow', ...arguments),
        this.slot('toolbar_actions', ...arguments),
      ]),
  ])
//##
        );
    }
}


export class TrExpandable extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['subrow']

    render_default(vnode, values, context)
    {
        let rendered_child = m_tostring(values.child);
        let total_column = (rendered_child.match(/<td/g) || []).length + 1;

        return (
//##
m.fragment(null,
  [
    m('tr',
      {
        'class': `bx--parent-row ${values['class']}`,
        'data-parent-row': '',
        ...values.props,
      },
      [
        m('td.bx--table-expand',
          {
            'data-event': 'expand',
          },
          m('button.bx--table-expand__button', null,
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                xmlns: 'http://www.w3.org/2000/svg',
                fill: 'currentColor',
                'class': 'bx--table-expand__svg',
                width: 16,
                height: 16,
                viewBox: '0 0 16 16',
                'aria-hidden': true,
              },
              m('path', {d: 'M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z'})))),
        values.child,
      ]),
    m('tr.bx--expandable-row.bx--expandable-row--hidden',
      {
        'data-child-row': '',
      },
      m('td',
        {
          colspan: total_column,
        },
        m('div.bx--child-row-inner-container', null,
          this.slot('subrow', ...arguments)))),
  ])
//##
        );
    }
}


export class Th extends Node
{
    WANT_CHILDREN = true
    MODES = ['default', 'checkbox', 'sortable', 'menu', 'expandable',
            'expand_all', 'row']
    NODE_PROPS = ['id']

    render_default(vnode, values, context)
    {
        return (
//##
m('th',
  {
    'class': values['class'],
    ...values.props,
  },
  m('span.bx--table-header-label', null, values.child))
//##
        );
    }

    render_checkbox(vnode, values, context)
    {
        return (
//##
m('th',
  {
    'class': `bx--table-column-checkbox ${values['class']}`,
  },
  [
    m('input.bx--checkbox',
      {
        'data-event': 'select-all',
        id: values.id,
        type: 'checkbox',
        ...values.props,
      }),
    m('label.bx--checkbox-label',
      {
        'for': values.id,
        'aria-label': `${values.label}${values.label_suffix}`,
      }),
  ])
//##
        );
    }

    render_sortable(vnode, values, context)
    {
        let cleaned_child = clean_attr_value(m_tostring(values.child));

        return (
//##
m('th',
  {
    'class': values['class'],
    ...values.props,
  },
  m('button.bx--table-sort',
    {
      'data-event': 'sort',
      title: cleaned_child,
    },
    [
      m('span.bx--table-header-label', null, values.child),
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          'class': 'bx--table-sort__icon',
          width: 16,
          height: 16,
          viewBox: '0 0 16 16',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 \
                10z',
          })),
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          'class': 'bx--table-sort__icon-unsorted',
          width: 16,
          height: 16,
          viewBox: '0 0 16 16',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 \
                14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 \
                5z',
          })),
    ]))
//##
        );
    }

    render_menu(vnode, values, context)
    {
        return m('th.bx--table-column-menu');
    }

    render_expandable(vnode, values, context)
    {
        return (
//##
m('th',
  {
    'class': `bx--table-expand ${values['class']}`,
    'data-event': 'expandAll',
    ...values.props,
  },
  m('span.bx--table-header-label'))
//##
        );
    }

    render_expand_all(vnode, values, context)
    {
        return (
//##
m('th',
  {
    'class': `bx--table-expand ${values['class']}`,
    'data-event': 'expandAll',
    ...values.props,
  },
  m('button.bx--table-expand__button', null,
    m('svg',
      {
        focusable: false,
        preserveAspectRatio: 'xMidYMid meet',
        xmlns: 'http://www.w3.org/2000/svg',
        fill: 'currentColor',
        'class': 'bx--table-expand__svg',
        width: 16,
        height: 16,
        viewBox: '0 0 16 16',
        'aria-hidden': true,
      },
      m('path', {d: 'M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z'}))))
//##
        );
    }

    render_row(vnode, values, context)
    {
        return (
//##
m('th',
  {
    scope: 'row',
    'class': values['class'],
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class Td extends Node
{
    WANT_CHILDREN = true
    MODE = ['default', 'menu', 'menu_visible']
    SLOTS = ['secondary']

    prepare(vnode, values, context)
    {
        values.txt_menu = gettext("Open menu");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('td',
  {
    'class': values['class'],
    ...values.props,
  },
  [
    values.child,
    this.slot('secondary', ...arguments),
  ])
//##
        );
    }

    render_menu(vnode, values, context)
    {
        return (
//##
m('td',
  {
    'class': `bx--table-column-menu ${values['class']}`,
    ...values.props,
  },
  m('div',
    {
      'data-overflow-menu': '',
      role: 'menu',
      tabindex: 0,
      'aria-label': `${values.label}${values.label_suffix}`,
      'class': 'bx--overflow-menu',
      title: values.txt_menu,
    },
    [
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          'class': 'bx--overflow-menu__icon',
          width: 16,
          height: 16,
          viewBox: '0 0 16 16',
          'aria-hidden': true,
        },
        [
          m('circle', {cx: 8, cy: 3, r: 1}),
          m('circle', {cx: 8, cy: 8, r: 1}),
          m('circle', {cx: 8, cy: 13, r: 1}),
        ]),
      m('ul.bx--overflow-menu-options.bx--overflow-menu--flip', null,
        values.child),
    ]))
//##
        );
    }

    render_menu_visible(vnode, values, context)
    {
        return (
//##
m('td',
  {
    'class': `bx--table-column-menu ${values['class']}`,
    ...values.props,
  },
  m('div',
    {
      'data-overflow-menu': '',
      role: 'menu',
      tabindex: 0,
      'aria-label': `${values.label}${values.label_suffix}`,
      'class': 'bx--overflow-menu',
      title: values.txt_menu,
    },
    [
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          fill: 'currentColor',
          xmlns: 'http://www.w3.org/2000/svg',
          'class': 'bx--overflow-menu__icon',
          width: 16,
          height: 16,
          viewBox: '0 0 16 16',
          'aria-hidden': true,
        },
        [
          m('circle', {cx: 8, cy: 3, r: 1}),
          m('circle', {cx: 8, cy: 8, r: 1}),
          m('circle', {cx: 8, cy: 13, r: 1}),
        ]),
      m('ul.bx--overflow-menu-options.bx--overflow-menu--flip', null,
        values.child),
    ]))
//##
        );
    }

    render_slot_secondary(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': `bx--data-table--cell-secondary-text ${values['class']}`,
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class TdCheckbox extends FormNode
{
    NODE_PROPS = ['value']
    REQUIRED_PROPS = ['value']

    default_id(vnode)
    {
        return uniqueId(this.bound_field.id_for_label + '-');
    }

    label()
    {
        for (let [group, val, txt] of this.choices())
        {
            if (val === this.value)
            {
                return txt;
            }
        }
    }

    before_prepare(vnode, values, context)
    {
        this.value = vnode.attrs.value;
        super.before_prepare(...arguments);
    }

    prepare(vnode, values, context)
    {
        if (this.bound_value && this.bound_value.indexOf(this.value) !== -1)
        {
            values.props.push(['checked', '']);
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('td.bx--table-column-checkbox',
  [
    m('input',
      {
        type: 'checkbox',
        name: this.bound_field.name,
        value: this.value,
        id: values.id,
        'class': `bx--checkbox ${values['class']}`,
        'data-event': 'select',
        ...values.props,
      }),
    m('label.bx--checkbox-label',
      {
        'for': values.id,
        'aria-label': `${values.label}${values.label_suffix}`,
      }),
  ])
//##
        );
    }

}


export class TbSearch extends Node
{
    NODE_PROPS = ['id', 'expandable', 'small']
    CLASS_AND_PROPS = ['wrapper', 'magnifier']
    CATCH_PROPS = ['search_props']

    prepare(vnode, values, context)
    {
        values.txt_search = gettext("Search");
        values.txt_clear = gettext("Clear search input");
        if (!values.label)
        {
            values.label = values.txt_search;
        }

        if (vnode.attrs.expandable)
        {
            values.wrapper_class.push('bx--toolbar-search-container-expandable');
            values.magnifier_props.push(['tabindex', 0]);
        }
        else
        {
            values.wrapper_class.push('bx--toolbar-search-container-persistent');
        }

        if (vnode.attrs.small)
        {
            values['class'].push('bx--search--sm');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': values.wrapper_class,
    ...values.wrapper_props,
  },
  m('div',
    {
      'data-search': '',
      'class': `bx--search ${values['class']}`,
      role: 'search',
      ...values.props,
    },
    [
      m('div',
        {
          'class': `bx--search-magnifier ${values.magnifier_class}`,
          ...values.magnifier_props,
        },
        this.tmpl('magnifier_icon', ...arguments)),
      m('label.bx--label',
        {
          id: `label-${values.id}`,
          'for': values.id,
        },
        `${values.label}${values.label_suffix}`),
      m('input.bx--search-input',
        {
          type: 'text',
          id: values.id,
          role: 'search',
          placeholder: values.txt_search,
          'aria-labelledby': `label-${values.id}`,
        }),
      m('button.bx--search-close.bx--search-close--hidden',
        {
          title: values.txt_clear,
          'aria-label': values.txt_clear,
        },
        m('svg',
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
              d: 'M12 4.7L11.3 4 8 7.3 4.7 4 4 4.7 7.3 8 4 11.3 4.7 12 8 8.7 \
                  11.3 12 12 11.3 8.7 8z',
            }))),
    ]))
//##
        );
    }

    render_tmpl_magnifier_icon(vnode, values, context)
    {
        return (
//##
m('svg',
  {
    focusable: false,
    preserveAspectRatio: 'xMidYMid meet',
    style: {'will-change': 'transform'},
    xmlns: 'http://www.w3.org/2000/svg',
    width: 16,
    height: 16,
    viewBox: '0 0 16 16',
    'aria-hidden': true,
  },
  m('path',
    {
      d: 'M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,\
          8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,\
          4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z',
    }))
//##
        );
    }
}


export class TableOvButton extends Node
{
    WANT_CHILDREN = true
    NODE_PROPS = ['active']
    CLASS_AND_PROPS = ['list']

    prepare(vnode, values, context)
    {
        if (vnode.attrs.active)
        {
            values.props.push(['data-floating-menu-primary-focus', '']);
        }

        if (context.compact)
        {
            values.list_class.push('bx--overflow-menu--data-table');
        }
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('li',
  {
    'class': `bx--overflow-menu-options__option ${values.list_class}`,
    role: 'presentation',
    ...values.list_props,
  },
  m('button',
    {
      'class': `bx--overflow-menu-options__btn ${values['class']}`,
      role: 'menuitem',
      ...values.props,
    },
    m('div.bx--overflow-menu-options__option-content', null, values.child)))
//##
        );
    }
}


export class TdOvButton extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['icon']
    NODE_PROPS = ['icon_size']

    render_default(vnode, values, context)
    {
        let cleaned_child = clean_attr_value(m_tostring(values.child));

        return (
//##
m('li.bx--overflow-menu-options__option.bx--table-row--menu-option',
  m(values.astag,
    {
      'class': `bx--overflow-menu-options__btn ${values['class']}`,
      title: cleaned_child,
      ...values.props,
    },
    m('div.bx--overflow-menu-options__option-content', null,
      [
        this.slot('icon', ...arguments),
        values.child,
      ])))
//##
        );
    }

    render_slot_icon(vnode, values, context)
    {
        let size = vnode.attrs.icon_size || 16;
        return modify_svg(values.child,
            {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                fill: 'currentColor',
                style: {
                    width: `${size}px`,
                    height: `${size}px`,
                },
                'aria-hidden': true,
                'class': values['class'],
                ...values.props,
            });
    }
}
