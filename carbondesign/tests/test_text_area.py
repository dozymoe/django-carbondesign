# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TextAreaTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TextArea form.text %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text" class="bx--label">
  Text
</label>
  <div class="bx--text-area__wrapper">
    <textarea name="text" cols="40" rows="10" class="bx--text-area bx--text-area--v2" required id="id_text">
a text</textarea>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
