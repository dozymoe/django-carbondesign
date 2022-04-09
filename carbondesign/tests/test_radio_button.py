# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class RadioTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Radio form.choice %}
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Choice</legend>
  <div class="bx--form-item">
    <div class="bx--radio-button-group">
<div class="bx--radio-button-wrapper">
  <input id="id_choice-1" class="bx--radio-button" type="radio" value="val1"
      name="choice" tabindex="0" checked>
  <label for="id_choice-1" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Value One</span>
  </label>
</div>
<div class="bx--radio-button-wrapper">
  <input id="id_choice-2" class="bx--radio-button" type="radio" value="val2"
      name="choice" tabindex="0">
  <label for="id_choice-2" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Value Two</span>
  </label>
</div>
    </div>
  </div>
</fieldset>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
