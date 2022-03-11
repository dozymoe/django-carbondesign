import { isString } from 'lodash';
import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class Pagination extends Node
{
    NODE_PROPS = ['pager', 'pager_sizes', 'disabled']
    PAGER_SIZES = [10, 20, 30, 40, 50]

    prepare(vnode, values, context)
    {
        this.pager = vnode.attrs.pager;

        values.txt_per_page = gettext("Items per page");
        values.txt_select_per_page = gettext("select number of items per page");
        values.txt_select_page_num = gettext("select page number to view");
        values.txt_back_btn = gettext("Backward button");
        values.txt_forw_btn = gettext("Forward button");
    }

    render_default(vnode, values, context)
    {
        if (this.pager)
        {
            return (
//##
m('div.bx--pagination',
  {
    'data-pagination': '',
  },
  [
    m('div.bx--pagination__left', null,
      [
        m('label',
          {
            id: `select-${values.id}-pagination-count-label`,
            'class': 'bx--pagination__text',
            'for': `select-${values.id}-pagination-count`,
          },
          values.txt_per_page),
        m('div.bx--select.bx--select--inline.bx--select__item-count', null,
          [
            m('select.bx--select-input',
              {
                id: `select-${values.id}-pagination-count`,
                'aria-label': values.txt_select_per_page,
                tabindex: 0,
                'data-items-per-page': '',
              },
              this.tmpl('pagination_sizes', vnode, values, context)),
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
                id: `select-${values.id}-pagination-page`,
                'aria-label': values.txt_select_page_num,
                tabindex: 0,
                'data-page-number-input': '',
              },
              this.tmpl('pagination_numbers', vnode, values, context)),
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
          ]),
      ]),
    m('label',
      {
        id: `select-${values.id}-pagination-page-label`,
        'class': 'bx--pagination__text',
        'for': `select-${values.id}-pagination-page`,
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
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          'class': 'bx--pagination__nav-arrow',
          width: 20,
          height: 20,
          viewBox: '0 0 32 32',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z',
          }))),
    m('button.bx--pagination__button.bx--pagination__button--forward',
      {
        tabindex: 0,
        'data-page-forward': '',
        'aria-label': values.txt_next_btn,
      },
      m('svg',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          'class': 'bx--pagination__nav-arrow',
          width: 20,
          height: 20,
          viewBox: '0 0 32 32',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M12 8L22 16 12 24z',
          }))),
  ])
//##
            );
        }
    }

    render_tmpl_pagination_sizes(vnode, values, context)
    {
        let items = [];
        let pager_sizes = vnode.attrs.pager_sizes || this.PAGER_SIZES;
        if (isString(pager_sizes))
        {
            pager_sizes = pager_sizes.split(',').map(x => parseInt(x));
        }
        for (let ii = 0; ii < pager_sizes.length; ii++)
        {
            if (ii)
            {
                items.push(
//##
m('option.bx--select-option', null, pager_sizes[ii])
//##
                );
            }
            else
            {
                items.push(
//##
m('option.bx--select-option', {selected: ''}, pager_sizes[ii])
//##
                );
            }
        }

        if (items.length)
        {
            return m.fragment(null, items);
        }
    }

    render_tmpl_pagination_numbers(vnode, values, context)
    {
        let items = [];
        for (let ii = 1; ii <= this.pager.num_pages; ii++)
        {
            if (ii !== this.pager.number)
            {
                items.push(
//##
m('option.bx--select-option', null, ii)
//##
                );
            }
            else
            {
                items.push(
//##
m('option.bx--select-option', {selected: ''}, ii)
//##
                );
            }
        }
        if (items.length)
        {
            return m.fragment(null, items);
        }
    }

    render_tmpl_pagination_range(vnode, values, context)
    {
        return (
//##
m.fragment(null,
  [
    m('span',
      {
        'data-displayed-item-range': '',
      },
      [
        this.pager.page_range[0],
        '-',
        this.pager.page_range[1],
      ]),
    'of',
    m('span',
      {
        'data-total-items': '',
      },
      this.pager.count),
    'items',
  ])
//##
        );
    }

    render_tmpl_pagination_num_pages(vnode, values, context)
    {
        return interpolate(gettext("of %s pages"), [this.pager.num_pages]);
    }
}
