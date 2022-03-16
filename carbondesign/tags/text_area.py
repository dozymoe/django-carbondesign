"""
Text Area
=========

See: https://the-carbon-components.netlify.app/?nav=text-area

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
    TEMPLATES = ('icon_invalid', *FormNode.TEMPLATES)
    "Conditional templates. Please sort from outer to inner subtemplates."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['help_class'].append('bx--form__helper-text--disabled')
            values['props'].append(('disabled', 'disabled'))


    def prepare_element_props(self, props, default, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].extend([
                'bx--text-area',
                'bx--text-area--v2'])

        if self.eval(self.kwargs.get('light'), context):
            props['class'].append('bx--text-input--light')

        if self.bound_field.errors:
            props['class'].append('bx--text-input--invalid')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  {tmpl_help}
  <div class="bx--text-area__wrapper" data-invalid>
    {element}
    {tmpl_icon_invalid}
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
  {tmpl_help}
  <div class="bx--text-area__wrapper">
    {element}
  </div>
</div>

"""
        return self.format(template, values, context)


    def render_tmpl_icon_invalid(self, values, context):
        """Dynamically render a part of the component's template.
        """
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
