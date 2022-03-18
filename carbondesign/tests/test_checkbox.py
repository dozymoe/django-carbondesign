# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class CheckBoxTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% CheckBox form.choice value="val1" %}
"""
        expected = """
<div class="bx--form-item bx--checkbox-wrapper">
  <input name="choice" value="val1" type="checkbox" id="id_choice-0"
      class="bx--checkbox" checked="" required="">
<label for="id_choice-0" class="bx--checkbox-label">
  Value One
</label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
