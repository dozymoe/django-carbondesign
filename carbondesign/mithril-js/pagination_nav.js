import m from 'mithril/hyperscript';
//-
import { Node } from './base';

export class PaginationNav extends Node
{
    NODE_PROPS = ['pager', 'count']

    prepare(vnode, values, context)
    {
        values.txt_pagination = gettext("pagination");
        values.txt_prev = gettext("Previous page");
        values.txt_next = gettext("Next page");
        values.txt_page = gettext("page");

        this.pager = vnode.attrs.pager;
        this.count = vnode.attrs.count || 5;

        if (this.pager)
        {
            if (this.pager.has_previous())
            {
                values.prev_class = '';
                values.prev_props = {};
            }
            else
            {
                values.prev_class = 'bx--pagination-nav__page--disabled';
                values.prev_props = {'aria-disabled': true};
            }
            if (this.pager.has_next())
            {
                values.next_class = '';
                values.next_props = {};
            }
            else
            {
                values.next_class = 'bx--pagination-nav__page--disabled';
                values.next_props = {'aria-disabled': true};
            }
        }
    }

    render_default(vnode, values, context)
    {
        if (this.pager)
        {
            return (
//##
m('nav.bx--pagination-nav',
  {
    'aria-label': values.txt_pagination,
    'data-pagination-nav': '',
  },
  m('ul.bx--pagination-nav__list', null,
    [
      this.tmpl('prev', vnode, values, context),
      this.tmpl('numbers', vnode, values, context),
      this.tmpl('prev', vnode, values, context),
    ]))
//##
            );
        }
    }

    render_tmpl_prev(vnode, values, context)
    {
        return (
//##
m('li.bx--pagination-nav__list-item', null,
  m('button',
    {
      'class': `bx--pagination-nav__page bx--pagination-nav__page--direction ${values.prev_class}`,
      'data-page-previous': '',
      ...values.prev_props,
    },
    [
      m('span.bx--pagination-nav__accessibility-label', null, values.txt_prev),
      m('svg.bx--pagination-nav__icon',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          width: 5,
          height: 8,
          viewBox: '0 0 5 8',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M5 8L0 4 5 0z',
          })),
    ]))
//##
        );
    }

    render_tmpl_next(vnode, values, context)
    {
        return (
//##
m('li.bx--pagination-nav__list-item', null,
  m('button',
    {
      'class': `bx--pagination-nav__page bx--pagination-nav__page--direction ${values.next_class}`,
      'data-page-next': '',
      ...values.next_props,
    },
    [
      m('span.bx--pagination-nav__accessibility-label', null, values.txt_next),
      m('svg.bx--pagination-nav__icon',
        {
          focusable: false,
          preserveAspectRatio: 'xMidYMid meet',
          xmlns: 'http://www.w3.org/2000/svg',
          fill: 'currentColor',
          width: 5,
          height: 8,
          viewBox: '0 0 5 8',
          'aria-hidden': true,
        },
        m('path',
          {
            d: 'M0 0L5 4 0 8z',
          })),
    ]))
//##
        );
    }

    render_tmpl_numbers(vnode, values, context)
    {
        let current = this.pager.current_page_number;
        let begin = Math.max(current - Math.floor(this.count / 2), 1);
        let end = Math.min(begin + this.count, this.pager.num_pages);

        let items = [];
        for (let ii = begin; ii <= end; ii++)
        {
            let classes = '', props = {};
            if (ii === current)
            {
                classes = 'bx--pagination-nav__page--active \
                    bx--pagination-nav__page--disabled';
                props['data-page-active'] = true;
                props['aria-current'] = 'page';
                props['aria-disabled'] = true;
            }
            items.push(
//##
m('li.bx--pagination-nav__list-item',
  m('button',
    {
      'class': `bx--pagination-nav__page ${classes}`,
      'data-page': ii,
      'data-page-button': '',
      ...props,
    },
    [
      m('span.bx--pagination-nav__accessibility-label', null, values.txt_page),
      ii,
    ]))
//##
            );
        }

        if (items.length)
        {
            return m.fragment(null, items);
        }
    }
}
