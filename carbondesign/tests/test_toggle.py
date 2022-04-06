# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ToggleTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Toggle form.text %}
"""
        expected = """
<div class="bx--form-item">
  <input type="text" name="text" value="a text" class="bx--toggle-input" required id="id_text">
  <label class="bx--toggle-input__label" for="id_text">
    Text
    <span class="bx--toggle__switch">
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
