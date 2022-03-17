# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class LinkTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Link %}
{% endLink %}
"""
        expected = """
<a class="bx--link">
</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
