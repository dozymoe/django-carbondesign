# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TagTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Tag %}
{% endTag %}
"""
        expected = """
<button class="bx--tag">
  <span class="bx--tag__label">
</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
