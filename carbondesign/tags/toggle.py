"""Implements Carbon Design Component: Toggle
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
    NODE_PROPS = ('nolabel',)

    def prepare(self, values, context):
        values['txt_off'] = _("Off")
        values['txt_on'] = _("On")

        if self.eval(self.kwargs.get('disabled'), context):
            values['props'].append(('disabled', ''))


    def prepare_element_props(self, props, default, context):
        props['class'].append('bx--toggle-input')

        if self.eval(self.kwargs.get('nolabel'), context):
            props['class'].append('bx--toggle-input--small')


    def render_default(self, values, context):
        template = """
<div class="bx--form-item">
  {element}
  <label class="bx--toggle-input__label {label_class}" for="{id}">
    {label}
    <span class="bx--toggle__switch">
      <svg class="bx--toggle__check" width="6px" height="5px" viewBox="0 0 6 5">
        <path d="M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z" />
      </svg>
      <span class="bx--toggle__text--off" aria-hidden="true">{txt_off}</span>
      <span class="bx--toggle__text--on" aria-hidden="true">{txt_on}</span>
    </span>
  </label>
  {tmpl_help}
</div>
"""
        return self.format(template, values)


    def render_nolabel(self, values, context):
        template = """
<div class="bx--form-item">
  {element}
  <label class="bx--toggle-input__label {label_class}" for="{id}"
      aria-label="{label}">
    <span class="bx--toggle__switch">
      <svg class="bx--toggle__check" width="6px" height="5px" viewBox="0 0 6 5">
        <path d="M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z" />
      </svg>
      <span class="bx--toggle__text--off" aria-hidden="true">{txt_off}</span>
      <span class="bx--toggle__text--on" aria-hidden="true">{txt_on}</span>
    </span>
  </label>
  {tmpl_help}
</div>
"""
        return self.format(template, values)


components = {
    'Toggle': Toggle,
}
