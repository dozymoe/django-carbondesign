"""
Checkbox
========

See: https://www.carbondesignsystem.com/components/checkbox/usage/

Checkboxes are used when there are multiple items to select in a list. Users
can select zero, one, or any number of items.

Overview
--------

Checkboxes are used for multiple choices, not for mutually exclusive choices.
Each checkbox works independently from other checkboxes in the list, therefore
checking an additional box does not affect any other selections.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import ChoiceFormNode

class CheckBox(ChoiceFormNode):
    """Checkbox component.
    """
    MODES = ('default', 'inside')
    "Available variants."
    NODE_PROPS = ('mixed',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('mixed'), context):
            values['props'].append(('aria-checked', 'mixed'))

            if self.mode == 'inside':
                values['label_props'].append(('data-contained-checkbox-state',
                        'mixed'))


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('bx--checkbox')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item bx--checkbox-wrapper">
  {tmpl_element}
  {tmpl_label}
</div>
"""
        return self.format(template, values, context)


    def render_inside(self, values, context,):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item bx--checkbox-wrapper">
  <label for="{id}" class="bx--checkbox-label {label_class}" {label_props}>
    {tmpl_element}
    {label}{label_suffix}
  </label>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''
        template = """
<label for="{id}" class="bx--checkbox-label {label_class}" {label_props}>
  {label}{label_suffix}
</label>
"""
        return self.format(template, values)


components = {
    'CheckBox': CheckBox,
}
