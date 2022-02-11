"""Implements Carbon Design Component: Checkbox
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import FormNode

class CheckBox(FormNode):
    """Checkbox component.
    """
    MODES = ('default', 'inside')
    "Available variants."
    NODE_PROPS = ('mixed',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        if self.eval(self.kwargs.get('disabled'), context):
            values['props'].append(('disabled', 'disabled'))

        if self.eval(self.kwargs.get('mixed'), context) and \
                self.mode == 'inside':

            values['label_props'].append(('data-contained-checkbox-state',
                    'mixed'))


    def render_default(self, values, context, slots):
        template = """
<div class="bx--form-item bx--checkbox-wrapper">
  {element}
  <label for="{id}" class="bx--checkbox-label {label_class}" {label_props}>
    {label}
  </label>
</div>
"""
        return self.format(template, values, slots)


    def render_inside(self, values, context, slots):
        template = """
<div class="bx--form-item bx--checkbox-wrapper">
  <label for="{id}" class="bx--checkbox-label {label_class}" {label_props}>
    {element}
    {label}
  </label>
</div>
"""
        return self.format(template, values, slots)


    def prepare_element_attributes(self, attrs, default, context):
        attrs['class'].append('bx--checkbox')

        if self.eval(self.kwargs.get('mixed'), context):
            attrs['aria-checked'] = 'mixed'


components = {
    'CheckBox': CheckBox,
}
