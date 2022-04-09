# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class LoadingHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
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

    def test_small(self):
        template = """
{% load carbondesign %}
{% Loading mode="small" %}
"""
        expected = """
<div data-loading class="bx--loading bx--loading--small">
  <svg class="bx--loading__svg" viewBox="0 0 100 100">
    <title>Loading</title>
    <circle class="bx--loading__background" cx="50%" cy="50%" r="42" />
    <circle class="bx--loading__stroke" cx="50%" cy="50%" r="42" />
  </svg>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_overlay(self):
        template = """
{% load carbondesign %}
{% Loading mode="overlay" %}
"""
        expected = """
<div class="bx--loading-overlay">
  <div data-loading class="bx--loading">
    <svg class="bx--loading__svg" viewBox="0 0 100 100">
      <title>Loading</title>
      <circle class="bx--loading__stroke" cx="50%" cy="50%" r="44" />
    </svg>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
