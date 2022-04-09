# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TooltipTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% InteractiveTooltip id="uid" label="Text" %}
{% endInteractiveTooltip %}
"""
        expected = """
<div id="label-uid" class="bx--tooltip__label">
  Text
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
    <p id="body-uid">
</p>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
