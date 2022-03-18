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

from typing import Sequence
#-
from .base import FormNode

class CheckBox(FormNode):
    """Checkbox component.
    """
    MODES = ('default', 'inside')
    "Available variants."
    NODE_PROPS = ('value', 'id', 'mixed')
    "Extended Template Tag arguments."
    RENDER_ELEMENT = False
    "Render the form field widget."

    value = None

    def default_id(self):
        """Get Django form field html id.
        """
        id_ = self.bound_field.id_for_label
        for ii, (_, val, _) in enumerate(self.choices()):
            if val == self.value:
                return f'{id_}-{ii}'
        return id_


    def label(self):
        """Get Django form field label.
        """
        for _, val, txt in self.choices():
            if val == self.value:
                return txt
        return ''


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.value = self.eval(self.kwargs['value'], context)
        super().before_prepare(values, context)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['value'] = self.value
        values['name'] = self.bound_field.name

        if self.eval(self.kwargs.get('disabled'), context):
            values['props'].append(('disabled', ''))

        if self.eval(self.kwargs.get('mixed'), context):
            values['props'].append(('aria-checked', 'mixed'))

            if self.mode == 'inside':
                values['label_props'].append(('data-contained-checkbox-state',
                        'mixed'))

        selected = self.bound_field.value()
        if not isinstance(selected, Sequence):
            selected = [selected]
        if self.value in selected:
            values['props'].append(('checked', ''))

        required = self.bound_field.field.required and\
                self.bound_field.form.use_required_attribute
        if required:
            values['props'].append(('required', ''))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item bx--checkbox-wrapper">
  <input name="{name}" value="{value}" type="checkbox" id="{id}"
      class="bx--checkbox {class}" {props}>
  <label for="{id}" class="bx--checkbox-label {label_class}" {label_props}>
    {label}
  </label>
</div>
"""
        return self.format(template, values)


    def render_inside(self, values, context,):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item bx--checkbox-wrapper">
  <label for="{id}" class="bx--checkbox-label {label_class}" {label_props}>
    <input name="{name}" value="{value}" type="checkbox" id="{id}"
        class="bx--checkbox {class}" {props}>
    {label}
  </label>
</div>
"""
        return self.format(template, values)


components = {
    'CheckBox': CheckBox,
}
