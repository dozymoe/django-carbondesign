# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class NumberInputTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number %}
"""
        expected = """
<div class="bx--form-item">
  <div data-numberinput class="bx--number">
<label for="id_number" class="bx--label">
  Number
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number" value="24" class="" required id="id_number">
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
