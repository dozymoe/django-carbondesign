"""Implements Carbon Design Component: Pagination Nav
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class PaginationNav(Node):
    """Pagination Nav component.
    """
    NODE_PROPS = ('pager', 'count')
    "Extended Template Tag arguments."
    TEMPLATES = ('prev', 'next', 'numbers')
    "Conditional templates."

    pager = None
    count = None

    def prepare(self, values, context):
        values['txt_pagination'] = _("pagination")
        values['txt_prev'] = _("Previous page")
        values['txt_next'] = _("Next page")
        values['txt_page'] = _("page")

        self.pager = self.eval(self.kwargs.get('pager'), context)
        self.count = self.eval(self.kwargs.get('count', 5), context)


    def render_default(self, values, context):
        if not self.pager:
            return ''

        template = """
<nav class="bx--pagination-nav" aria-label="{txt_pagination}"
    data-pagination-nav>
  <ul class="bx--pagination-nav__list">
    {tmpl_prev}
    {tmpl_numbers}
    {tmpl_prev}
  </ul>
</nav>
"""
        return self.format(template, values, context)


    def render_tmpl_prev(self, values, context):
        if not self.pager.has_previous():
            values['class'].append('bx--pagination-nav__page--disabled')
            values['props'].append(('aria-disabled', 'true'))

        template = """
<li class="bx--pagination-nav__list-item">
  <button
      class="bx--pagination-nav__page bx--pagination-nav__page--direction {class}"
      data-page-previous {props}>
    <span class="bx--pagination-nav__accessibility-label">{txt_prev}</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--pagination-nav__icon" width="5" height="8" viewBox="0 0 5 8"
        aria-hidden="true">
      <path d="M5 8L0 4 5 0z"></path>
    </svg>
  </button>
</li>
"""
        return self.format(template, values)


    def render_tmpl_next(self, values, context):
        if not self.pager.has_next():
            values['class'].append('bx--pagination-nav__page--disabled')
            values['props'].append(('aria-disabled', 'true'))

        template = """
<li class="bx--pagination-nav__list-item">
  <button
      class="bx--pagination-nav__page bx--pagination-nav__page--direction {class}"
      data-page-next {props}>
    <span class="bx--pagination-nav__accessibility-label">{txt_next}</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--pagination-nav__icon" width="5" height="8" viewBox="0 0 5 8"
        aria-hidden="true">
      <path d="M0 0L5 4 0 8z"></path>
    </svg>
  </button>
</li>
"""
        return self.format(template, values)


    def render_tmpl_numbers(self, values, context):
        current = self.pager.current_page_number
        begin = max(current - int(self.count / 2), 1)
        end = min(begin + self.count, self.pager.num_pages)

        template = """
<li class="bx--pagination-nav__list-item">
  <button class="bx--pagination-nav__page {class}" data-page="{num}"
      data-page-button {props}>
    <span class="bx--pagination-nav__accessibility-label">{txt_page}</span>
    {num}
  </button>
</li>
"""
        items = []
        for ii in range(begin, end + 1):
            options = {'num': ii}
            if ii == 'current':
                options['class'] = ' '.join([
                    'bx--pagination-nav__page--active',
                    'bx--pagination-nav__page--disabled',
                ])
                options['props'] = ' '.join([
                    'data-page-active="true"',
                    'aria-current="page"',
                    'aria-disabled="true"',
                ])
            items.append(self.format(template, options))
        return '\n'.join(items)


components = {
    'PaginationNav': PaginationNav,
}
