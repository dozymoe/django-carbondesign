# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class OverflowMenuTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% OverflowMenu id="uid" %}
{% endOverflowMenu %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--right bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-uid"
      aria-controls="uid">
    <span class="bx--assistive-text">Overflow</span>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
  </button>
  <div class="bx--overflow-menu-options" tabindex="-1" role="menu"
      aria-labelledby="trigger-uid" id="uid" data-floating-menu-direction="bottom">
    <ul class="bx--overflow-menu-options__content">
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class OverflowMenuItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% OverflowMenuItem %}
{% endOverflowMenuItem %}
"""
        expected = """
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
    </span>
  </button>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
