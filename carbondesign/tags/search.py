"""Implements Carbon Design Component: Search
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class Search(Node):
    """Search component.
    """
    NODE_PROPS = ('style', 'light')
    "Extended Template Tag arguments."
    AVAILABLE_STYLES = ('sm', 'lg', 'xl')
    "Documentation only."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_clear'] = _("Clear search input")

        if not values['label']:
            values['label'] = _("Search")

        style = self.eval(self.kwargs.get('style'), context)
        if style:
            values['class'].append(f'bx--search--{style}')

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--search--light')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item">
  <div data-search role="search" class="bx--search {class}">
    <label id="label-{id}" class="bx--label {label_class}" for="{id}"
        {label_props}>
      {label}
    </label>
    <input class="bx--search-input" type="text" id="{id}"
        placeholder="{label}">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--search-magnifier" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5 C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
    </svg>
    <button class="bx--search-close bx--search-close--hidden"
        title="{txt_clear}" aria-label="{txt_clear}">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--search-clear" width="16" height="16" viewBox="0 0 32 32"
          aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        return self.format(template, values)


components = {
    'Search': Search,
}
