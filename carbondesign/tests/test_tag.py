# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class TagTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Tag %}
{% endTag %}
"""
        expected = """
<button type="button" class="bx--tag">
  <span class="bx--tag__label">
</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
