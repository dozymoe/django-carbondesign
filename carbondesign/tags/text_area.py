"""Implements Carbon Design Component: Text input
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

#from django.utils.translation import gettext as _
#-
from .base import FormNode

class TextArea(FormNode):
    """Text Area component.
    """
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['help_class'].append('bx--form__helper-text--disabled')
            values['props'].append(('disabled', 'disabled'))


    def prepare_element_attributes(self, attrs, default, context):
        attrs['class'].extend([
                'bx--text-area',
                'bx--text-area--v2'])

        if self.eval(self.kwargs.get('light'), context):
            attrs['class'].append('bx--text-input--light')

        if self.bound_field.errors:
            attrs['class'].append('bx--text-input--invalid')


    def render_default(self, values, context, slots):
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  {slot_help}
  <div class="bx--text-area__wrapper" data-invalid>
    {slot_icon}
  </div>
  <div class="bx--form-requirement">
    {form_errors}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  {slot_help}
  <div class="bx--text-area__wrapper">
    {element}
  </div>
</div>

"""
        return self.format(template, values, slots)


    def render_slot_icon(self, values, context):
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
    class="bx--text-area__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8  c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>

"""


components = {
    'TextArea': TextArea,
}
