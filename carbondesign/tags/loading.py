"""
Loading
=======

See: https://www.carbondesignsystem.com/components/loading/usage/

Loading spinners are used when retrieving data or performing slow computations,
and help to notify users that loading is underway.

Overview
--------

Loading spinners are used when retrieving data or performing slow computations.
They notify to the user that their request is being processed. Although they
do not provide details about what is occurring on the back-end, they reassure
the user that their action is being processed.

Use a loading spinner whenever the wait time is anticipated to be longer than
three seconds.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class Loading(Node):
    """Loading component.
    """
    MODES = ('default', 'overlay', 'small')
    "Available variants."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_loading'] = _("Loading")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-loading class="bx--loading">
  <svg class="bx--loading__svg" viewBox="0 0 100 100">
    <title>{txt_loading}</title>
    <circle class="bx--loading__stroke" cx="50%" cy="50%" r="44" />
  </svg>
</div>
"""
        return self.format(template, values)


    def render_overlay(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--loading-overlay">
  <div data-loading class="bx--loading">
    <svg class="bx--loading__svg" viewBox="0 0 100 100">
      <title>{txt_loading}</title>
      <circle class="bx--loading__stroke" cx="50%" cy="50%" r="44" />
    </svg>
  </div>
</div>
"""
        return self.format(template, values)


    def render_small(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-loading class="bx--loading bx--loading--small">
  <svg class="bx--loading__svg" viewBox="0 0 100 100">
    <title>{txt_loading}</title>
    <circle class="bx--loading__background" cx="50%" cy="50%" r="42" />
    <circle class="bx--loading__stroke" cx="50%" cy="50%" r="42" />
  </svg>
</div>
"""
        return self.format(template, values)


components = {
    'Loading': Loading,
}
