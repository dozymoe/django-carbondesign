"""Implements Carbon Design Component: Radio Button
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import FormNode

class RadioButton(FormNode):
    """Radio Button component.
    """
    NODE_PROPS = ('exclude', 'vertical', 'left')
    "Extended Template Tag arguments."
    TEMPLATES = ('items', *FormNode.TEMPLATES)
    "Conditional templates."

    def prepare(self, values, context):
        if self.eval(self.kwargs.get('vertical'), context):
            values['wrapper_class'].append('bx--radio-button-group--vertical')

        if self.eval(self.kwargs.get('left'), context):
            values['class'].append('bx--radio-button-wrapper--label-left')


    def render_default(self, values, context):
        template = """
<fieldset class="bx--fieldset">
  <legend class="bx--label {label_class}" {label_props}>{label}</legend>
  <div class="bx--form-item">
    <div class="bx--radio-button-group {wrapper_class}">
      {tmpl_items}
    </div>
  </div>
</fieldset>
"""
        return self.format(template, values, context)


    def render_tmpl_items(self, values, context):
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
        value = self.bound_field.value()
        excludes = self.eval(self.kwargs.get('exclude', []), context)

        items = []
        for ii, (val, txt) in enumerate(self.bound_field.field.choices):
            options = {
                'index': '%s-%s' % (values['id'], ii),
                'value': val,
                'child': txt,
                'name': self.bound_field.name,
                'class': values['class'],
            }
            props = []
            if val == value:
                props.append('checked')
            if val in excludes:
                props.append('disabled')
            options['props'] = ' '.join(props)
            items.append(self.format(template, options))

        return '\n'.join(items)


components = {
    'Radio': RadioButton,
}
