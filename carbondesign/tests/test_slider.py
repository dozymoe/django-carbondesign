# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class SliderTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Slider form.number %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_number" class="bx--label">
  Number
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
          max="100" value="24">
    </div>
    <label id="top_range-label-id_number" class="bx--slider__range-label">
      100
    </label>
    <input id="id_number"
        aria-labelledby="bottom_range-label-id_number top_range-label-id_number"
        type="number" class="bx--text-input bx--slider-text-input"
        placeholder="0" value="24">
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
