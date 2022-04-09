# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class GridTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Grid %}
{% endGrid %}
"""
        expected = """
<div class="bx--grid">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class RowTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Row %}
{% endRow %}
"""
        expected = """
<div class="bx--row">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ColTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Col %}
{% endCol %}
"""
        expected = """
<div class="bx--col bx--col--auto">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class AspectRatioTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% AspectRatio %}
{% endAspectRatio %}
"""
        expected = """
<div class="bx--aspect-ratio">
  <div class="bx--aspect-ratio--object">
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
