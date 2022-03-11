"""Implements Carbon Design Component: Pagination
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node


class Pagination(Node):
    """Pagination component.
    """
    NODE_PROPS = ('pager', 'pager_sizes', 'disabled')
    "Extended Template Tag arguments."
    TEMPLATES = ('pagination_sizes', 'pagination_numbers', 'pagination_range',
            'pagination_num_pages')
    "Conditional templates."
    PAGER_SIZES = (10, 20, 30, 40, 50)

    pager = None

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        self.pager = self.eval(self.kwargs.get('pager'), context)

        values['txt_per_page'] = _("Items per page")
        values['txt_select_per_page'] = _("select number of items per page")
        values['txt_select_page_num'] = _("select page number to view")
        values['txt_back_btn'] = _("Backward button")
        values['txt_forw_btn'] = _("Forward button")


    def render_default(self, values, context):
        """Output html of the component.
        """
        if not self.pager:
            return ''

        template = """
<div class="bx--pagination" data-pagination>
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
        for="select-id-pagination-page">
      {tmpl_pagination_num_pages}
    </label>
    <button class="bx--pagination__button bx--pagination__button--backward"
        tabindex="0" data-page-backward aria-label="{txt_back_btn}">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M20 24L10 16 20 8z"></path>
      </svg>
    </button>
    <button class="bx--pagination__button bx--pagination__button--forward"
        tabindex="0" data-page-forward aria-label="{txt_next_btn}">
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
        template = """
<option class="bx--select-option" value="{value}" {props}>
  {label}
</option>
"""
        options = []

        pager_sizes = self.eval(self.kwargs.get('pager_sizes',
                self.PAGER_SIZES), context)
        if isinstance(pager_sizes, str):
            pager_sizes = [int(x) for x in pager_sizes.split(',')]

        for ii, value in enumerate(pager_sizes):
            if ii:
                options.append(template.format(value=value, label=value,
                        props=''))
            else:
                options.append(template.format(value=value, label=value,
                        props='selected'))
        return ''.join(options)


    def render_tmpl_pagination_numbers(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<option class="bx--select-option" value="{value}" {props}>
  {label}
</option>
"""
        options = []

        for value in (x + 1 for x in range(self.pager.num_pages)):
            if value != self.pager.number:
                options.append(template.format(value=value, label=value,
                        props=''))
            else:
                options.append(template.format(value=value, label=value,
                        props='selected'))
        return ''.join(options)


    def render_tmpl_pagination_range(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<span data-displayed-item-range>{range_start}-{range_end}</span>
"""
        page_range = template.format(
                {
                    'range_start': self.pager.page_range[0],
                    'range_end': self.pager.page_range[1],
                })
        template = '<span data-total-items>{total}</span>'
        page_total = template.format(
                {
                    'total': self.pager.count,
                })

        range_of_items = _("%s of %s items")
        return range_of_items % (page_range, page_total)


    def render_tmpl_pagination_num_pages(self, values, context):
        """Dynamically render a part of the component's template.
        """
        num_pages = _("of %s pages")
        return num_pages % self.pager.num_pages


components = {
    'Pagination': Pagination,
}
