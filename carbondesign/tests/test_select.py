# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class SelectTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Select form.choice %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select">
    <label for="id_choice" class="bx--label">
      Choice
    </label>
    <div class="bx--select-input__wrapper">
      <select class="bx--select-input" id="id_choice" name="choice" required="">
<option class="bx--select-option" value="val1" selected>
  Value One
</option>
<option class="bx--select-option" value="val2">
  Value Two
</option>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
