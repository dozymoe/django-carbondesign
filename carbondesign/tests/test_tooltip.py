# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class TooltipTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Tooltip id="uid" %}
{% endTooltip %}
"""
        expected = """
<div id="label-uid" class="bx--tooltip__label">
  None
  <button aria-expanded="false" aria-labelledby="label-uid"
      data-tooltip-trigger data-tooltip-target="#uid"
      class="bx--tooltip__trigger" aria-controls="uid">
  </button>
</div>
<div id="uid" aria-hidden="true" data-floating-menu-direction="bottom"
    class="bx--tooltip">
  <span class="bx--tooltip__caret"></span>
  <div class="bx--tooltip__content" tabindex="-1" role="dialog"
      aria-describedby="body-uid" aria-labelledby="label-uid">
    <div id="body-uid">
</div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class TooltipHeadingTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TooltipHeading %}
{% endTooltipHeading %}
"""
        expected = """
<h4 class="bx--tooltip__heading">
</h4>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
