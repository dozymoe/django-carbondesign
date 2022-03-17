# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class LoadingTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Loading %}
"""
        expected = """
<div data-loading class="bx--loading">
  <svg class="bx--loading__svg" viewBox="0 0 100 100">
    <title>Loading</title>
    <circle class="bx--loading__stroke" cx="50%" cy="50%" r="44" />
  </svg>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
