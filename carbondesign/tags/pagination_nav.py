"""
Pagination Nav
==============

See: https://the-carbon-components.netlify.app/?nav=pagination-nav

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

NUMBERS_TEMPLATE = """
<li class="bx--pagination-nav__list-item">
  <{item_tag} class="bx--pagination-nav__page {item_class}" data-page="{num}"
      data-page-button {item_props}>
    <span class="bx--pagination-nav__accessibility-label">{txt_page}</span>
    {num}
  </{item_tag}>
</li>
"""
PRE_NUMBERS_SELECT_TEMPLATE = """
<li class="bx--pagination-nav__list-item">
  <div class="bx--pagination-nav__select">
    <select class="bx--pagination-nav__page bx--pagination-nav__page--select"
        data-page-select aria-label="{txt_select}">
      <option value="" hidden></option>
"""
POST_NUMBERS_SELECT_TEMPLATE = """
    </select>
    <div class="bx--pagination-nav__select-icon-wrapper">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination-nav__select-icon" width="16" height="16"
          viewBox="0 0 32 32" aria-hidden="true">
        <circle cx="8" cy="16" r="2"></circle>
        <circle cx="16" cy="16" r="2"></circle>
        <circle cx="24" cy="16" r="2"></circle>
      </svg>
    </div>
  </div>
</li>
"""


class PaginationNav(Node):
    """Pagination Nav component.
    """
    NODE_PROPS = ('pager', 'max_links', 'extra_links', 'as_link')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('item',)
    "Prepare xxx_class and xxx_props values."

    pager = None
    links_begin = None
    links_end = None
    links_before = []
    links_after = []

    def calculate_links(self, max_links, max_extra):
        """Prepare page links.
        """
        current = self.pager.number
        last = self.pager.paginator.num_pages

        # Try to keep current page in the middle of the links.
        self.links_begin = max(current - int(max_links / 2), 1)
        self.links_end = min(self.links_begin + max_links - 1, last)

        # Don't show extra selections if the number of links is too low.
        if not max_extra or self.links_end - self.links_begin + 1 < 7:
            return

        # Links 1 and 2 are going to be replaced with first in extra links and
        # the select box.
        begin = max(self.links_begin + 1 - max_extra, 1)
        end = min(self.links_begin + 1, current - 2)
        if begin < end:
            self.links_before = list(range(begin, end + 1))
            self.links_begin = end + 1

        begin = max(self.links_end - 1, current + 2)
        end = min(self.links_end - 1 + max_extra, last)
        if begin < end:
            self.links_after = list(range(begin, end + 1))
            self.links_end = begin - 1


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_pagination'] = _("pagination")
        values['txt_prev'] = _("Previous page")
        values['txt_next'] = _("Next page")
        values['txt_page'] = _("page")
        values['txt_select'] = _("select page number")

        self.pager = self.eval(self.kwargs.get('pager'), context)

        max_links = self.eval(self.kwargs.get('max_links', 7), context)
        max_extra = self.eval(self.kwargs.get('extra_links'), context)
        if self.pager:
            self.calculate_links(max_links, max_extra)

        if self.pager:
            if self.pager.has_previous():
                values['prev_class'] = ''
                values['prev_props'] = ''
            else:
                values['prev_class'] = 'bx--pagination-nav__page--disabled'
                values['prev_props'] = 'aria-disabled="true"'

            if self.pager.has_next():
                values['next_class'] = ''
                values['next_props'] = ''
            else:
                values['next_class'] = 'bx--pagination-nav__page--disabled'
                values['next_props'] = 'aria-disabled="true"'

        if self.eval(self.kwargs.get('as_link'), context):
            values['item_tag'] = 'a'
            values['item_props'].append(('href', 'javascript:void(0)'))
        else:
            values['item_tag'] = 'button'


    def render_default(self, values, context):
        """Output html of the component.
        """
        if not self.pager:
            return ''

        template = """
<nav class="bx--pagination-nav" aria-label="{txt_pagination}" data-pagination-nav>
  <ul class="bx--pagination-nav__list">
    {tmpl_prev}
    {tmpl_numbers_before}
    {tmpl_numbers}
    {tmpl_numbers_after}
    {tmpl_next}
  </ul>
</nav>
"""
        return self.format(template, values, context)


    def render_tmpl_prev(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<li class="bx--pagination-nav__list-item">
  <{item_tag} class="bx--pagination-nav__page bx--pagination-nav__page--direction {prev_class} {item_class}"
      data-page-previous {prev_props} {item_props}>
    <span class="bx--pagination-nav__accessibility-label">{txt_prev}</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--pagination-nav__icon" width="5" height="8" viewBox="0 0 5 8"
        aria-hidden="true">
      <path d="M5 8L0 4 5 0z"></path>
    </svg>
  </{item_tag}>
</li>
"""
        return self.format(template, values)


    def render_tmpl_next(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<li class="bx--pagination-nav__list-item">
  <{item_tag} class="bx--pagination-nav__page bx--pagination-nav__page--direction {next_class} {item_class}"
      data-page-next {next_props} {item_props}>
    <span class="bx--pagination-nav__accessibility-label">{txt_next}</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--pagination-nav__icon" width="5" height="8" viewBox="0 0 5 8"
        aria-hidden="true">
      <path d="M0 0L5 4 0 8z"></path>
    </svg>
  </{item_tag}>
</li>
"""
        return self.format(template, values)


    def render_tmpl_numbers(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.links_begin >= self.links_end:
            return ''
        items = []
        for ii in range(self.links_begin, self.links_end + 1):
            # There are `item_tag` and `txt_page` in the template, but those
            # will be replaced when rendering the whole component.
            options = {'num': ii}
            if ii == self.pager.number:
                options['item_class'] = 'bx--pagination-nav__page--active ' +\
                        'bx--pagination-nav__page--disabled ' +\
                        values['item_class']
                options['item_props'] = 'data-page-active="true" ' +\
                        'aria-current="page" aria-disabled="true" ' +\
                        values['item_props']
            items.append(self.format(NUMBERS_TEMPLATE, options))
        return '\n'.join(items)


    def render_tmpl_numbers_before(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not self.links_before:
            return ''
        first = self.links_before.pop(0)
        items = []

        items.append(self.format(NUMBERS_TEMPLATE, {'num': first}))
        items.append(PRE_NUMBERS_SELECT_TEMPLATE)
        for ii in self.links_before:
            items.append(f'<option data-page="{ii}">{ii}</option>')
        items.append(POST_NUMBERS_SELECT_TEMPLATE)
        return '\n'.join(items)


    def render_tmpl_numbers_after(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not self.links_after:
            return ''
        last = self.links_after.pop(-1)
        items = []

        items.append(PRE_NUMBERS_SELECT_TEMPLATE)
        for ii in self.links_after:
            items.append(f'<option data-page="{ii}">{ii}</option>')
        items.append(POST_NUMBERS_SELECT_TEMPLATE)
        items.append(self.format(NUMBERS_TEMPLATE, {'num': last}))
        return '\n'.join(items)


components = {
    'PaginationNav': PaginationNav,
}
