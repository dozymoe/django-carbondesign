# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class TileTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Tile %}
{% endTile %}
"""
        expected = """
<div class="bx--tile">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
