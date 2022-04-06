# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    number = forms.IntegerField(required=False,
            label="Number input label",
            validators=[MaxValueValidator(100), MinValueValidator(0)],
            )


class SliderHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        form = DummyForm(data={'number': 25})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Slider form.number min=0 max=100 step=1 label="Slider label" id="id_number" %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_number" class="bx--label">
  Slider label
</label>
  <div class="bx--slider-container">
    <label id="bottom_range-label-id_number" class="bx--slider__range-label">
      0
    </label>
    <div class="bx--slider" data-slider
        data-slider-input-box="#id_number">
      <div class="bx--slider__thumb" tabindex="0"></div>
      <div class="bx--slider__track"></div>
      <div class="bx--slider__filled-track"></div>
      <input aria-label="slider" id="slider-id_number"
          class="bx--slider__input" type="range" step="1" min="0"
          max="100" value="25">
    </div>
    <label id="top_range-label-id_number" class="bx--slider__range-label">
      100
    </label>
    <input id="id_number"
        aria-labelledby="bottom_range-label-id_number top_range-label-id_number"
        type="number" class="bx--text-input bx--slider-text-input"
        placeholder="0" value="25">
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_light(self):
        form = DummyForm(data={'number': 75})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Slider form.number min=0 max=100 step=1 label="Slider label" light=True %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_number" class="bx--label">
  Slider label
</label>
  <div class="bx--slider-container">
    <label id="bottom_range-label-id_number" class="bx--slider__range-label">
      0
    </label>
    <div class="bx--slider" data-slider
        data-slider-input-box="#id_number">
      <div class="bx--slider__thumb" tabindex="0"></div>
      <div class="bx--slider__track"></div>
      <div class="bx--slider__filled-track"></div>
      <input aria-label="slider" id="slider-id_number"
          class="bx--slider__input" type="range" step="1" min="0"
          max="100" value="75">
    </div>
    <label id="top_range-label-id_number" class="bx--slider__range-label">
      100
    </label>
    <input id="id_number"
        aria-labelledby="bottom_range-label-id_number top_range-label-id_number"
        type="number" class="bx--text-input bx--slider-text-input bx--text-input--light"
        placeholder="0" value="75">
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
