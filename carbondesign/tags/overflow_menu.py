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

from django.utils.translation import gettext as _
#-
from .base import Node, clean_attr_value

class OverflowMenu(Node):
    """UI Shell component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('id', 'flip', 'direction', 'position', 'align')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('trigger',)
    "Prepare xxx_class and xxx_props values."
    POSSIBLE_DIRECTION = ('top', 'bottom')
    "Documentation only."
    POSSIBLE_POSITION = ('left', 'right')
    "Documentation only."
    POSSIBLE_ALIGN = ('start',)
    "Documentation only."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_overflow'] = _("Overflow")

        if self.eval(self.kwargs.get('flip'), context):
            values['class'].append('bx--overflow-menu--flip')

        direction = self.eval(self.kwargs.get('direction', 'bottom'), context)
        values['props'].append(('data-floating-menu-direction', direction))

        position = self.eval(self.kwargs.get('position', 'right'), context)
        values['trigger_class'].append(f'bx--tooltip--{position}')

        align = self.eval(self.kwargs.get('align', 'start'), context)
        values['trigger_class'].append(f'bx--tooltip--align-{align}')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y {trigger_class}"
      aria-haspopup="true" aria-expanded="false" id="trigger-{id}"
      aria-controls="{id}" {trigger_props}>
    <span class="bx--assistive-text">{txt_overflow}</span>
    {tmpl_icon}
  </button>
  <div class="bx--overflow-menu-options {class}" tabindex="-1" role="menu"
      aria-labelledby="trigger-{id}" id="{id}" {props}>
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
    "Template Tag needs closing end tag."
    NODE_PROPS = ('disabled', 'active', 'variant')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."
    CLASS_AND_PROPS = ('list',)
    "Prepare xxx_class and xxx_props values."
    POSSIBLE_VARIANT = ('danger',)
    "Documentation only."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('disabled'), context):
            values['list_class'].append(
                    'bx--overflow-menu-options__option--disabled')
            if values['astag'] == 'button':
                values['props'].append(('disabled', True))
            else:
                values['props'].append(('tabindex', '-1'))
                values['props'].append(('aria-disabled', 'true'))

        if self.eval(self.kwargs.get('active'), context):
            values['props'].append(('data-floating-menu-primary-focus', True))

        variant = self.eval(self.kwargs.get('variant'), context)
        if variant:
            values['list_class'].append(
                    f'bx--overflow-menu-options__option--{variant}')


    def after_prepare(self, values, context):
        """Simplifying values meant for rendering templates.
        """
        if self.eval(self.kwargs.get('active'), context) and\
                'title' not in self.kwargs:
            values['props'].append(('title', clean_attr_value(values['child'])))
        super().after_prepare(values, context)


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--overflow-menu-options__option {list_class}" {list_props}>
  <{astag} class="bx--overflow-menu-options__btn {class}" role="menuitem" {props}>
    <span class="bx--overflow-menu-options__option-content">
      {child}
    </span>
  </{astag}>
</li>
"""
        return self.format(template, values)


components = {
    'OvMenu': OverflowMenu,
    'OvMenuItem': OverflowMenuItem,
}
