"""
Tag
===

See: https://www.carbondesignsystem.com/components/tag/usage/

Use tags to label, categorize, or organize items using keywords that describe
them.

Overview
--------

Multiple or single tags can be used to categorize items.

Use short labels for easy scanning. Use two words only if necessary to
describe the status and differentiate it from other tags.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class Tag(Node):
    """Tag component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'filter')
    "Available variants."
    NODE_PROPS = ('variant',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_clear'] = _("Clear filter")

        variant = self.eval(self.kwargs.get('variant'), context)
        if variant:
            values['class'].append(f'bx--tag--{variant}')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<button class="bx--tag {class}" {props}>
  <span class="bx--tag__label">{child}</span>
</button>
"""
        return self.format(template, values)


    def render_filter(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--tag bx--tag--filter" title="{txt_clear}">
  <span class="bx--tag__label">{child}</span>
  <button class="bx--tag__close-icon">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 32 32" aria-hidden="true">
      <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
    </svg>
  </button>
</div>
"""
        return self.format(template, values)


components = {
    'Tag': Tag,
}
