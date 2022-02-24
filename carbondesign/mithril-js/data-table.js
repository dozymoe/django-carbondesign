import { range } from 'lodash';
import m from 'mithril/hyperscript';
//-
import { Node } from './base';


export class Table extends Node
{
    WANT_CHILDREN = true
    SLOTS = ['title', 'description', 'batch_actions', 'toolbar',
            'toolbar_overflow', 'head', 'foot']
    MODES = ['default', 'sticky']
    NODE_PROPS = ['style', 'pager', 'pager_size', 'sortable']
    TEMPLATES = ['header', 'toolbar', 'pagination', 'pagination_sizes',
            'pagination_numbers', 'pagination_range', 'pagination_num_pages']
    AVAILABLE_STYLES = ['compact', 'short', 'tall', 'zebra']
    PAGER_SIZES = [10, 20, 30, 40, 50]

    prepare(vnode, values, context)
    {
        values.txt_batch_actions = gettext("Table Action Bar")
        values.txt_items_selected = gettext("items selected")
        values.txt_overflow = gettext("Overflow")

        if (vnode.attrs.style)
        {
            values['class'].push('bx--data-table--' + vnode.attrs.style);
        }
        if (vnode.attrs.sortable)
        {
            values['class'].push('bx--data-table--sort');
        }
    }

    render_default(vnode, values, context, slots)
    {
        return (
//##
m.fragment(null,
  [
    m('div.bx--data-table-container',
      {
        'data-table': '',
      },
      [
        this.tmpl('header', ...arguments),
        this.tmpl('toolbar', ...arguments),
      ]),
    m('table',
      {
        'class': 'bx--data-table ' + values['class'],
        ...values.props,
      },
      [
        this.slot('head', ...arguments),
        values.child,
        this.slot('foot', ...arguments),
      ]),
    this.tmpl('pagination', ...arguments),
  ])
//##
        );
    }

    render_sticky(vnode, values, context, slots)
    {
        return (
//##
m.fragment(null,
  [
    m('section.bx--data-table_inner-container', null,
      m('table',
        {
          'class': 'bx--data-table bx--data-table--sticky-header ' +
              values['class'],
          ...values.props,
        },
        [
          this.slot('head', ...arguments),
          values.child,
          this.slot('foot', ...arguments),
        ])),
    this.tmpl('pagination', ...arguments),
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
    'class': 'bx--data-table-header__title ' + values['class'],
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
    'class': 'bx--data-table-header__description ' + values['class'],
    ...values.props,
  },
  values.child)
//##
        );
    }

    render_slot_batch_actions(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': 'bx--batch-actions ' + values['class'],
    'aria-label': values.txt_batch_actions,
    ...values.props,
  },
  [
    m('div.bx--action-list', null, values.child),
    m('div.bx--batch-summary', null,
      m('p.bx--batch-summary__para', null,
        [
          m('span', {'data-items-selected': 0}),
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
    'class': 'bx--overflow-menu bx--toolbar-action ' + values['class'],
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
        style: {'will-change': 'transform'},
        xmlns: 'http://www.w3.org/2000/svg',
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

    render_tmpl_header(vnode, values, context)
    {
        if (!this.slots.title && !this.slots.description)
        {
            return;
        }
        return (
//##
m('div.bx--data-table-header', null,
  [
    this.slot('title', vnode, values, context),
    this.slot('description', vnode, values, context),
  ])
//##
        );
    }

    render_tmpl_toolbar(vnode, values, context)
    {
        if (!this.slots.batch_actions && !this.slots.toolbar_overflow &&
                !this.slots.toolbar)
        {
            return;
        }
        return (
//##
m('section.bx--table-toolbar', null,
  [
    this.slot('batch_actions', vnode, values, context),
    m('div.bx--toolbar-content', null,
      [
        this.slot('toolbar_overflow', vnode, values, context),
        this.slot('toolbar', vnode, values, context),
      ]),
  ])
//##
        );
    }

    render_tmpl_pagination(vnode, values, context)
    {
        let pager = vnode.attrs.pager;
        if (!pager)
        {
            return;
        }
        if (!pager.has_previous() && !pager.has_next())
        {
            return;
        }

        values.txt_per_page = gettext("Items per page")
        values.txt_select_per_page = gettext("select number of items per page")
        values.txt_select_page_num = gettext("select page number to view")
        values.txt_back_btn = gettext("Backward button")
        values.txt_forw_btn = gettext("Forward button")

        return (
//##
m('div.bx--pagination',
  {
    'data-pagination': '',
  },
  [
    m('div.bx--pagination__left', null,
      [
        m('label.bx--pagination__text',
          {
            id: 'select-' + values.id + '-pagination-count-label',
            'for': 'select-' + values.id + '-pagination-count',
          },
          values.txt_per_page),
        m('div.bx--select bx--select--inline.bx--select__item-count', null,
          [
            m('select.bx--select-input',
              {
                id: 'select-' + values.id + '-pagination-count',
                'aria-label': values.txt_select_per_page,
                tabindex: 0,
                'data-items-per-page': '',
              },
              this.tmpl('pagination_sizes', vnode, values, context)),
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                style: {'will-change': 'transform'},
                xmlns: 'http://www.w3.org/2000/svg',
                'class': 'bx--select__arrow',
                width: 10,
                height: 6,
                viewBox: '0 0 10 6',
                'aria-hidden': true,
              },
              m('path',
                {
                  d: 'M5 6L0 1 0.7 0.3 5 4.6 9.3 0.3 10 1z',
                }))
          ]),
        m('span.bx--pagination__text', null,
          this.tmpl('pagination_range', vnode, values, context)),
      ]),
    m('div.bx--pagination__right', null,
      [
        m('div.bx--select.bx--select--inline.bx--select__page-number', null,
          [
            m('select.bx--select-input',
              {
                id: 'select-' + values.id + '-pagination-page',
                'aria-label': values.txt_select_page_num,
                tabindex: '0',
                'data-page-number-input': '',
              },
              this.tmpl('pagination_numbers', vnode, values, context)),
            m('svg',
              {
                focusable: false,
                preserveAspectRatio: 'xMidYMid meet',
                style: {'will-change': 'transform'},
                xmlns: 'http://www.w3.org/2000/svg',
                'class': 'bx--select__arrow',
                width: 10,
                height: 6,
                viewBox: '0 0 10 6',
                'aria-hidden': true,
              },
              m('path',
                {
                  d: 'M5 6L0 1 0.7 0.3 5 4.6 9.3 0.3 10 1z',
                })),

          ]),
        m('label',
          {
            id: 'select-' + values.id + '-pagination-page-label',
            'class': 'bx--pagination__text',
            'for': 'select-' + values.id + '-pagination-page',
          },
          this.tmpl('pagination_num_pages', vnode, values, context)),
        m('button.bx--pagination__button.bx--pagination__button--backward',
          {
            tabindex: 0,
            'data-page-backward': '',
            'aria-label': values.txt_back_btn,
          },
          m('svg',
            {
              focusable: false,
              preserveAspectRatio: 'xMidYMid meet',
              style: {'will-change': 'transform'},
              xmlns: 'http://www.w3.org/2000/svg',
              'class': 'bx--pagination__nav-arrow',
              width: 20,
              height: 20,
              viewBox: '0 0 32 32',
              'aria-hidden': true,
            },
            m('path',
              {
                d: 'M19 23L11 16 19 9 19 23z',
              }))),
        m('button.bx--pagination__button.bx--pagination__button--forward',
          {
            tabindex: 0,
            'data-page-forward': '',
            'aria-label': values.txt_forw_btn,
          },
          m('svg',
            {
              focusable: false,
              preserveAspectRatio: 'xMidYMid meet',
              style: {'will-change': 'transform'},
              xmlns: 'http://www.w3.org/2000/svg',
              'class': 'bx--pagination__nav-arrow',
              width: 20,
              height: 20,
              viewBox: '0 0 32 32',
              'aria-hidden': true,
            },
            m('path',
              {
                d: 'M13 9L21 16 13 23 13 9z',
              }))),
      ]),
  ])
//##
        );
    }

    render_tmpl_pagination_sizes(vnode, values, context)
    {
        let pager = vnode.attrs.pager;
        if (!pager)
        {
            return;
        }

        let options = []

        let pager_sizes = vnode.attrs.pager_size || this.PAGER_SIZES;
        if (typeof pager_sizes === 'string' || pager_sizes instanceof String)
        {
            pager_sizes = pager_sizes.split(',')
        }

        for (let value of pager_sizes)
        {
            if (options.length)
            {
                options.push(m('option.bx--select-option', {value: value},
                        value));
            }
            else
            {
                options.push(m('option.bx--select-option',
                        {value: value, selected: ''}, value));
            }
        }
        return m.fragment({}, options)
    }

    render_tmpl_pagination_numbers(vnode, values, context)
    {
        let pager = vnode.attrs.pager;
        if (!pager)
        {
            return;
        }

        let options = []

        for (let value of range(1, pager.num_pages))
        {
            if (value != pager.number)
            {
                options.push(m('option.bx--select-option', {value: value},
                        value));
            }
            else
            {
                options.push(m('option.bx--select-option',
                        {value: value, selected: ''}, value));
            }
        }
        return m.fragment({}, options)
    }


    render_tmpl_pagination_range(vnode, values, context)
    {
        let pager = vnode.attrs.pager;
        if (!pager)
        {
            return;
        }

        return (
//##
m.fragment(null,
  [
    m('span',
      {
        'data-displayed-item-range': '',
      },
      pager.start_index() + '-' + pager.end_index()),
    gettext(' of '),
    m('span',
      {
        'data-total-items': '',
      },
      pager.count),
    gettext(' items'),
  ])
//##
        );
    }

    render_tmpl_pagination_num_pages(vnode, values, context)
    {
        let pager = vnode.attrs.pager;
        if (!pager)
        {
            return;
        }

        return (
//##
m.fragment(null,
  [
    gettext('of '),
    pager.num_pages,
    gettext(' pages'),
  ])
//##
        );
    }
}


export class Th extends Node
{
    WANT_CHILDREN = true
    MODES = ['default', 'checkbox', 'sortable', 'menu']

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
    'class': 'bx--table-column-checkbox ' + values['class'],
  },
  [
    m('input.bx--checkbox',
      {
        'data-event': 'select-all',
        id: values.id,
        type: 'checkbox',
        ...values.props,
      }),
    m('label',
      {
        'for': values.id,
        'class': 'bx--checkbox-label ' + values.label_class,
        'aria-label': values.label,
        ...values.label_props,
      }),
  ])
//##
        );
    }

    render_sortable(vnode, values, context)
    {
        values.cleaned_child = '';//strip_tags(values['child'])

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
      title: values.cleaned_child,
    },
    [
      m('span.bx--table-header-label', null, values.child),
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          style: {'will-change': 'transform'},
          xmlns: 'http://www.w3.org/2000/svg',
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
          style: {'will-change': 'transform'},
          xmlns: 'http://www.w3.org/2000/svg',
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
        return (
//##
m('th',
  {
    'class': 'bx--table-column-menu ' + values['class'],
    ...values.props,
  })
//##
        );
    }
}


export class Td extends Node
{
    WANT_CHILDREN = true
    MODE = ['default', 'checkbox', 'menu']
    SLOTS = ['secondary']

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
    this.slot('secondary', vnode, values, context),
  ])
//##
        );
    }

    render_checkbox(vnode, values, context)
    {
        return (
//##
m('td',
  {
    'class': 'bx--table-column-checkbox ' + values['class'],
  },
  [
    m('input.bx--checkbox',
      {
        'data-event': 'select',
        id: values.id,
        type: 'checkbox',
        ...values.props,
      }),
    m('label',
      {
        'for': values.id,
        'class': 'bx--checkbox-label ' + values.label_class,
        'aria-label': values.label,
        ...values.label_props,
      }),
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
    'class': 'bx--table-column-menu ' + values['class'],
    ...values.props,
  },
  m('div',
    {
      'data-overflow-menu': '',
      role: 'menu',
      tabindex: 0,
      'aria-label': values.label,
      'class': 'bx--overflow-menu ' + values.label_class,
      ...values.label_props,
    },
    [
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          style: {'will-change': 'transform'},
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
    'class': 'bx--data-table--cell-secondary-text ' + values['class'],
    ...values.props,
  },
  values.child)
//##
        );
    }
}


export class TbSearch extends Node
{
    prepare(vnode, values, context)
    {
        values.txt_search = gettext("Search");
        values.txt_clear = gettext("Clear search input");
    }

    render_default(vnode, values, context)
    {
        return (
//##
m('div',
  {
    'class': 'bx--toolbar-search-container-persistent ' + values['class'],
    ...values.props,
  },
  m('div',
    {
      'data-search': '',
      'class': 'bx--search bx--search--sm',
      role: 'search',
    },
    [
      m('div.bx--search-magnifier', null,
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
            }))),
      m('label',
        {
          id: 'label-' + values.id,
          'class': 'bx--label ' + values.label_class,
          'for': values.id,
          ...values.label_props,
        },
        values.label),
      m('input.bx--search-input',
        {
          type: 'text',
          id: values.id,
          role: 'search',
          placeholder: values.txt_search,
          'aria-labelledby': 'label-' + values.id,
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
            style: {'will-change': 'transform'},
            xmlns: 'http://www.w3.org/2000/svg',
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
}


export class TableOvButton extends Node
{
    WANT_CHILDREN = true

    render_default(vnode, values, context)
    {
        return (
//##
m('li.bx--overflow-menu-options__option.bx--overflow-menu--data-table',
  {
    role: 'presentation',
  },
  m('button',
    {
      'class': 'bx--overflow-menu-options__btn ' + values['class'],
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
    SLOTS = ['icon',]

    render_default(vnode, values, context)
    {
        return (
//##
m('li.bx--overflow-menu-options__option.bx--table-row--menu-option',
  m(values.tag,
    {
      'class': 'bx--overflow-menu-options__btn ' + values['class'],
      ...values.props,
    },
    m('div.bx--overflow-menu-options__option-content', null,
      [
        this.slot('icon', vnode, values, context),
        values.child,
      ])))
//##
        );
    }

    render_slot_icon(vnode, values, context)
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
    'class': values['class'],
    ...values.props,
  },
  values.child)
//##
        );
    }
}
