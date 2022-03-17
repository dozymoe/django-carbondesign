# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class MultiSelectTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% MultiSelect form.choice %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    <label class="bx--label">
      Choice
    </label>
    <div class="bx--multi-select bx--list-box">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Open menu" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">Multi select options</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Choice
        </legend>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Value One" class="bx--checkbox-label">
        <input type="checkbox" name="choice" readonly class="bx--checkbox"
            id="id_choice-0" value="val1" checked>
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Value One
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Value Two" class="bx--checkbox-label">
        <input type="checkbox" name="choice" readonly class="bx--checkbox"
            id="id_choice-1" value="val2">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Value Two
        </span>
      </label>
    </div>
  </div>
</div>
      </fieldset>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
