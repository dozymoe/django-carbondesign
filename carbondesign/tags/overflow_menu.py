"""
Overflow Menu
=============

See: https://www.carbondesignsystem.com/components/overflow-menu/usage/

Use the overflow menu component when additional options are available to the
user but there is a space constraint.

Overview
--------

Overflow menu is used when additional options are available to the user and
there is a space constraint.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.html import strip_tags
from django.utils.translation import gettext as _
#-
from .base import Node

class OverflowMenu(Node):
    """UI Shell component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('flip', 'up')
    "Extended Template Tag arguments."
    TEMPLATES = ('icon',)
    "Conditional templates."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_overflow'] = _("Overflow")

        if self.eval(self.kwargs.get('flip'), context):
            values['class'].append('bx--overflow-menu--flip')

        if self.eval(self.kwargs.get('up'), context):
            values['direction'] = 'top'
        else:
            values['direction'] = 'bottom'


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-overflow-menu class="bx--overflow-menu">
  <button
      class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--right bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-{id}"
      aria-controls="{id}">
    <span class="bx--assistive-text">{txt_overflow}</span>
    {tmpl_icon}
  </button>
  <div class="bx--overflow-menu-options {class}" tabindex="-1" role="menu"
      aria-labelledby="trigger-{id}" data-floating-menu-direction="{direction}"
      id="{id}">
    <ul class="bx--overflow-menu-options__content">
      {child}
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
"""


class OverflowMenuItem(Node):
    """Overflow Menu item component.
    """
    WANT_CHILDREN = True
    NODE_PROPS = ('disabled', 'active', 'danger')

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('disabled'), context):
            values['class'].append('bx--overflow-menu-options__option--disabled')
            values['props'].append(('disabled', 'disabled'))

        if self.eval(self.kwargs.get('active'), context):
            values['props'].append(('title',
                    strip_tags(values['child']).strip()))
            values['props'].append(('data-floating-menu-primary-focus', ''))

        if self.eval(self.kwargs.get('danger'), context):
            values['class'].append('bx--overflow-menu-options__option--danger')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--overflow-menu-options__option {class}">
  <button class="bx--overflow-menu-options__btn" role="menuitem" {props}>
    <span class="bx--overflow-menu-options__option-content">
      {child}
    </span>
  </button>
</li>
  """
        return self.format(template, values)


components = {
    'OverflowMenu': OverflowMenu,
    'OverflowMenuItem': OverflowMenuItem,
}
