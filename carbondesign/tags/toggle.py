"""
Toggle
======

See: https://www.carbondesignsystem.com/components/toggle/usage/

A toggle is used to quickly switch between two possible states. They are
commonly used for “on/off” switches.

Overview
--------

Toggle is a control that is used to quickly switch between two possible states.
Toggles are only used for these binary actions that occur immediately after
the user “flips the switch”. They are commonly used for “on/off” switches.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class Toggle(FormNode):
    """Toggle component.
    """
    MODES = ('default', 'nolabel')
    "Extended Template Tag arguments."
    NODE_PROPS = ('small',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_off'] = _("Off")
        values['txt_on'] = _("On")


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('bx--toggle-input')

        if self.eval(self.kwargs.get('small'), context):
            props['class'].append('bx--toggle-input--small')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item">
  {tmpl_element}
  <label class="bx--toggle-input__label" for="{id}">
    {label}{label_suffix}
    <span class="bx--toggle__switch">
      {tmpl_icon}
      <span class="bx--toggle__text--off" aria-hidden="true">{txt_off}</span>
      <span class="bx--toggle__text--on" aria-hidden="true">{txt_on}</span>
    </span>
  </label>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


    def render_nolabel(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item">
  {tmpl_element}
  <label class="bx--toggle-input__label" for="{id}" aria-label="{label}{label_suffix}">
    <span class="bx--toggle__switch">
      {tmpl_icon}
      <span class="bx--toggle__text--off" aria-hidden="true">{txt_off}</span>
      <span class="bx--toggle__text--on" aria-hidden="true">{txt_on}</span>
    </span>
  </label>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.eval(self.kwargs.get('small'), context):
            return """
<svg class="bx--toggle__check" width="6px" height="5px" viewBox="0 0 6 5">
  <path d="M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z" />
</svg>
"""
        return ''


components = {
    'Toggle': Toggle,
}
