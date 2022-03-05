"""Implements Carbon Design Component: Loading
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
        values['txt_loading'] = _("Loading")


    def render_default(self, values, context):
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
