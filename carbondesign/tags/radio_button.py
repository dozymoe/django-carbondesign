"""
Radio Button
============

See: https://www.carbondesignsystem.com/components/radio-button/usage/

Use radio buttons when you have a group of mutually exclusive choices and only
one selection from the group is allowed.

Overview
--------

Radio buttons are used for mutually exclusive choices, not for multiple
choices. Only one radio button can be selected at a time. When a user chooses
a new item, the previous choice is automatically deselected.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import FormNode

class RadioButton(FormNode):
    """Radio Button component.
    """
    NODE_PROPS = ('exclude', 'vertical', 'left')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('radio',)
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('vertical'), context):
            values['radio_class'].append('bx--radio-button-group--vertical')

        if self.eval(self.kwargs.get('left'), context):
            values['class'].append('bx--radio-button-wrapper--label-left')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">{label}{label_suffix}</legend>
  <div class="bx--form-item">
    <div class="bx--radio-button-group {radio_class}">
      {tmpl_items}
    </div>
  </div>
</fieldset>
"""
        return self.format(template, values, context)


    def render_tmpl_items(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<div class="bx--radio-button-wrapper {class}">
  <input id="{id}" class="bx--radio-button" type="radio" value="{value}"
      name="{name}" tabindex="0" {props}>
  <label for="{id}" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">{child}</span>
  </label>
</div>
"""
        selected = self.bound_field.value()
        excludes = self.eval(self.kwargs.get('exclude', []), context)
        if isinstance(excludes, str):
            excludes = [x.strip() for x in excludes.split(';')]

        items = []
        for ii, (_, val, txt) in enumerate(self.choices()):
            options = {
                'id': '%s-%s' % (values['id'], ii + 1),
                'value': val,
                'child': txt,
                'name': self.bound_field.name,
                'class': values['class'],
            }
            props = []
            if val == selected:
                props.append('checked')
            if val in excludes:
                props.append('disabled')
            options['props'] = ' '.join(props)
            items.append(self.format(template, options))

        return '\n'.join(items)


components = {
    'Radio': RadioButton,
}
