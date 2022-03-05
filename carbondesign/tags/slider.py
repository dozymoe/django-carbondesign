"""Implements Carbon Design Component: Slider
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class Slider(FormNode):
    """Slider component.
    """
    NODE_PROPS = ('min', 'max', 'step', 'light')

    def prepare(self, values, context):
        values['txt_slider'] = _("slider")
        values['min'] = self.eval(self.kwargs.get('min', 0), context)
        values['max'] = self.eval(self.kwargs.get('max', 100), context)
        values['step'] = self.eval(self.kwargs.get('step', 1), context)
        values['value'] = self.bound_field.value()

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--slider-text-input--light')

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['wrapper_class'].append('bx--slider--disabled')


    def render_default(self, values, context):
        template = """
<div class="bx--form-item">
  <label class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  <div class="bx--slider-container">
    <label id="slider-input-box_bottom-range-label-{id}"
        class="bx--slider__range-label">
      {min}
    </label>
    <div class="bx--slider {wrapper_class}"
        data-slider data-slider-input-box="#{id}">
      <div class="bx--slider__thumb" tabindex="0"></div>
      <div class="bx--slider__track"></div>
      <div class="bx--slider__filled-track"></div>
      <input aria-label="{txt_slider}" id="slider-{id}"
          class="bx--slider__input" type="range" step="{step}" min="{min}"
          max="{max}" value="{value}">
    </div>
    <label id="slider-input-box_top-range-label-{id}"
        class="bx--slider__range-label">
      {max}
    </label>
    <input id="{id}"
        aria-labelledby="slider-input-box_bottom-range-label-{id} slider-input-box_top-range-label-{id}"
        type="number" class="bx--text-input bx--slider-text-input {class}"
        placeholder="{min}" value="{value}">
  </div>
</div>
"""
        return self.format(template, values, context)


components = {
    'Slider': Slider,
}
