"""
Pagination
==========

See: https://www.carbondesignsystem.com/components/pagination/usage/

Pagination is used for splitting up content or data into several pages, with
a control for navigating to the next or previous page.

Overview
--------

Generally, pagination is used if there are more than 25 items displayed in
one view.

The default number displayed will vary depending on the context.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

import logging
#-
from django.utils.translation import gettext as _
#-
from .base import Node

_logger = logging.getLogger(__name__)


class Pagination(Node):
    """Pagination component.
    """
    NODE_PROPS = ('pager', 'pager_sizes', 'disabled', 'page_name',
            'pagesize_name')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('navbtn',)
    "Prepare xxx_class and xxx_props values."
    PAGER_SIZES = (10, 20, 30, 40, 50)

    pager = None
    pagesize = 10

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        request = context.get('request')
        self.pager = self.eval(self.kwargs.get('pager'), context)

        values['txt_per_page'] = _("Items per page")
        values['txt_select_per_page'] = _("select number of items per page")
        values['txt_select_page_num'] = _("select page number to view")
        values['txt_back_btn'] = _("previous page")
        values['txt_forw_btn'] = _("next page")

        values['page_name'] = self.eval(self.kwargs.get('page_name', 'page'),
                context)
        values['pagesize_name'] = self.eval(self.kwargs.get('pagesize_name',
                'pagesize'), context)

        if request:
            self.pagesize = request.GET.get(values['pagesize_name'],
                    self.pagesize)

        if self.eval(self.kwargs.get('disabled'), context):
            values['navbtn_class'].append('bx--pagination__button--no-index')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if not self.pager:
            return ''
        if not self.pager.has_previous and not self.pager.has_next:
            return ''

        template = """
<div class="bx--pagination" data-pagination data-page-name="{page_name}"
    data-pagesize-name="{pagesize_name}">
  <div class="bx--pagination__left">
    <label id="select-{id}-pagination-count-label" class="bx--pagination__text"
        for="select-{id}-pagination-count">
      {txt_per_page}:
    </label>
    <div class="bx--select bx--select--inline bx--select__item-count">
      <select class="bx--select-input" id="select-{id}-pagination-count"
          aria-label="{txt_select_per_page}" tabindex="0"
          data-items-per-page>
        {tmpl_pagination_sizes}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <span class="bx--pagination__text">
      {tmpl_pagination_range}
    </span>
  </div>
  <div class="bx--pagination__right">
    <div class="bx--select bx--select--inline bx--select__page-number">
      <select class="bx--select-input" id="select-{id}-pagination-page"
          aria-label="{txt_select_page_num}" tabindex="0"
          data-page-number-input>
        {tmpl_pagination_numbers}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <label id="select-{id}-pagination-page-label" class="bx--pagination__text"
        for="select-{id}-pagination-page">
      {tmpl_pagination_num_pages}
    </label>
    <button class="bx--pagination__button bx--pagination__button--backward {navbtn_class}"
        tabindex="0" data-page-backward aria-label="{txt_back_btn}" {navbtn_props}>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M20 24L10 16 20 8z"></path>
      </svg>
    </button>
    <button class="bx--pagination__button bx--pagination__button--forward {navbtn_class}"
        tabindex="0" data-page-forward aria-label="{txt_forw_btn}" {navbtn_props}>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M12 8L22 16 12 24z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_pagination_sizes(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = '<option class="bx--select-option" {props}>{value}</option>'
        options = []

        pager_sizes = self.eval(self.kwargs.get('pager_sizes',
                self.PAGER_SIZES), context)
        if isinstance(pager_sizes, str):
            pager_sizes = [int(x) for x in pager_sizes.split(',')]
        else:
            # Make sure it's a copy
            pager_sizes = list(pager_sizes)
        if self.pagesize not in pager_sizes:
            pager_sizes.insert(0, self.pagesize)

        for value in pager_sizes:
            if value == self.pagesize:
                options.append(template.format(value=value, props='selected'))
            else:
                options.append(template.format(value=value, props=''))
        return '\n' + '\n'.join(options)


    def render_tmpl_pagination_numbers(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = '<option class="bx--select-option" {props}>{value}</option>'
        options = []

        for value in (x + 1 for x in range(self.pager.paginator.num_pages)):
            if value != self.pager.number:
                options.append(template.format(value=value, props=''))
            else:
                options.append(template.format(value=value, props='selected'))
        return '\n' + '\n'.join(options)


    def render_tmpl_pagination_range(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<span data-displayed-item-range>{range_start} – {range_end}</span>
"""
        page_range = template.format(
                range_start=self.pager.start_index(),
                range_end=self.pager.end_index())
        template = '<span data-total-items>{total}</span>'
        page_total = template.format(total=self.pager.paginator.count)

        range_of_items = _("{range} of {total} items")
        return range_of_items.format(range=page_range, total=page_total)


    def render_tmpl_pagination_num_pages(self, values, context):
        """Dynamically render a part of the component's template.
        """
        num_pages = _("of {total} pages")
        return num_pages.format(total=self.pager.paginator.num_pages)


components = {
    'Pagination': Pagination,
}
