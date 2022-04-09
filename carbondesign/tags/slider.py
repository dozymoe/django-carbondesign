"""
Slider
======

See: https://www.carbondesignsystem.com/components/slider/usage/

Sliders provide a visual indication of adjustable content, where the user can
increase or decrease the value by moving the handle along a horizontal track.

Overview
--------

The slider in its basic form should be accompanied by a label and a number
input that doubles as a display for the slider’s current value.

The basic slider does not include discrete values, as the slider represents
a percentage of 0-100. In this case it is not necessary for a user to choose
a specific value, but instead generally increase or decrease an input. For
example, the user increases the slider amount and the volume of the music gets
louder.

The more complex versions should be used for selecting a specific value within
a value range.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class Slider(FormNode):
    """Slider component.
    """
    NODE_PROPS = ('id', 'min', 'max', 'step', 'light')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'slider')
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_slider'] = _("slider")
        values['min'] = self.eval(self.kwargs.get('min', 0), context)
        values['max'] = self.eval(self.kwargs.get('max', 100), context)
        values['step'] = self.eval(self.kwargs.get('step', 1), context)
        values['value'] = self.bound_field.value()

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--text-input--light')

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['slider_class'].append('bx--slider--disabled')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item">
  {tmpl_label}
  <div class="bx--slider-container">
    <label id="bottom_range-label-{id}" class="bx--slider__range-label">
      {min}
    </label>
    <div class="bx--slider {slider_class}" data-slider
        data-slider-input-box="#{id}" {slider_props}>
      <div class="bx--slider__thumb" tabindex="0"></div>
      <div class="bx--slider__track"></div>
      <div class="bx--slider__filled-track"></div>
      <input aria-label="{txt_slider}" id="slider-{id}"
          class="bx--slider__input" type="range" step="{step}" min="{min}"
          max="{max}" value="{value}">
    </div>
    <label id="top_range-label-{id}" class="bx--slider__range-label">
      {max}
    </label>
    <input id="{id}"
        aria-labelledby="bottom_range-label-{id} top_range-label-{id}"
        type="number" class="bx--text-input bx--slider-text-input {class}"
        placeholder="{min}" value="{value}" {props}>
  </div>
</div>
"""
        return self.format(template, values, context)


components = {
    'Slider': Slider,
}
