"""
Copy Button
===========

See: https://the-carbon-components.netlify.app/?nav=copy-button

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class CopyButton(Node):
    """Copy Button component.
    """

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_copied'] = _("Copied!")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<button data-copy-btn class="bx--copy-btn {class}" type="button" tabindex="0"
    {props}>
  <span class="bx--assistive-text bx--copy-btn__feedback">{txt_copied}</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--snippet__icon" width="16" height="16" viewBox="0 0 32 32"
      aria-hidden="true">
    <path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z"></path>
    <path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z"></path>
  </svg>
</button>
"""
        return self.format(template, values)


components = {
    'CopyButton': CopyButton,
}
