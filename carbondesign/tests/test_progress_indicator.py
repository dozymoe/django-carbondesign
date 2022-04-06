# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ProgressIndicatorTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ProgressIndicator %}
{% endProgressIndicator %}
"""
        expected = """
<ul data-progress data-progress-current class="bx--progress">
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ProgressTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Progress id="uid" %}
{% endProgress %}
"""
        expected = """
<li class="bx--progress-step bx--progress-step--current">
<svg>
  <path d="M 7, 7 m -7, 0 a 7,7 0 1,0 14,0 a 7,7 0 1,0 -14,0"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid">
  </p>
  <span class="bx--progress-line"></span>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
