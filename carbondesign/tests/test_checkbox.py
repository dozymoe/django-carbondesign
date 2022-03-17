# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class CheckBoxTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% CheckBox form.text %}
"""
        expected = """
<div class="bx--form-item bx--checkbox-wrapper">
  <input type="text" name="text" value="a text" class="bx--checkbox" required id="id_text">
  <label for="id_text" class="bx--checkbox-label">
    Text
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
