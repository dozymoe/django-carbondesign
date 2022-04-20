"""
Number Input
============

See: https://www.carbondesignsystem.com/components/number-input/usage/

The number input component is used for entering numeric values and includes
controls for incrementally increasing or decreasing the value.

Overview
--------

Number inputs are similar to text inputs, but contain controls used to
increase or decrease an incremental value.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class NumberInput(FormNode):
    """Number Input component.
    """
    MODES = ('default', 'mobile')
    "Available variants."
    NODE_PROPS = ('nolabel', 'light')
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_increase'] = _("increase number input")
        values['txt_decrease'] = _("decrease number input")

        if self.eval(self.kwargs.get('nolabel'), context):
            values['class'].append('bx--number--nolabel')

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--number--light')

        if self.bound_field.help_text:
            values['class'].append('bx--number--helpertext')


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        if self.bound_field.errors:
            props['role'] = 'alert'
            props['aria-atomic'] = 'true'


    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div data-invalid data-numberinput class="bx--number {class}">
    {tmpl_label}
    <div class="bx--number__input-wrapper">
      {tmpl_element}
      {tmpl_icon_invalid}
      <div class="bx--number__controls">
        {tmpl_btn_incr}
        {tmpl_btn_decr}
      </div>
    </div>
    <div class="bx--form-requirement">
      {tmpl_errors}
    </div>
    {tmpl_help}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div data-numberinput class="bx--number {class}">
    {tmpl_label}
    <div class="bx--number__input-wrapper">
      {tmpl_element}
      <div class="bx--number__controls">
        {tmpl_btn_incr}
        {tmpl_btn_decr}
      </div>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_mobile(self, values, context):
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div data-invalid data-numberinput
      class="bx--number bx--number--mobile {class}">
    {tmpl_label}
    <div class="bx--number__input-wrapper">
      {tmpl_btn_decr}
      {tmpl_element}
      {tmpl_btn_incr}
    </div>
    <div class="bx--form-requirement">
      {tmpl_errors}
    </div>
    {tmpl_help}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--mobile {class}">
    {tmpl_label}
    <div class="bx--number__input-wrapper">
      {tmpl_btn_decr}
      {tmpl_element}
      {tmpl_btn_incr}
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.eval(self.kwargs.get('nolabel'), context):
            return ''

        template = """
<label for="{id}" class="bx--label {label_class}" {label_props}>
  {label}{label_suffix}
</label>
"""
        return self.format(template, values)


    def render_tmpl_icon_invalid(self, values, context):
        """Dynamically render a part of the component's template.
        """
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--number__invalid" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
"""


    def render_tmpl_btn_incr(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<button aria-label="{txt_increase}" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
"""
        return self.format(template, values)


    def render_tmpl_btn_decr(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<button aria-label="{txt_decrease}" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
"""
        return self.format(template, values)


components = {
    'NumberInput': NumberInput,
}
