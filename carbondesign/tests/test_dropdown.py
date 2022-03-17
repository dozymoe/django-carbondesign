# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class DropdownTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Dropdown id="uid" %}
{% endDropdown %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--dropdown__wrapper">
    <span id="label-uid" class="bx--label">
      None
    </span>
    <div data-dropdown data-value class="bx--dropdown">
      <button class="bx--dropdown-text" aria-haspopup="true"
          aria-expanded="false" aria-controls="menu-uid"
          aria-labelledby="label-uid value-uid" type="button" id="uid">
        <span class="bx--dropdown-text__inner" id="value-uid">
        </span>
        <span class="bx--dropdown__arrow-container">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              class="bx--dropdown__arrow" width="16" height="16"
              viewBox="0 0 16 16" aria-hidden="true">
            <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
          </svg>
        </span>
      </button>
      <ul class="bx--dropdown-list" id="menu-uid" role="menu" tabindex="-1"
          aria-hidden="true" aria-labelledby="label-uid">
      </ul>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class DropdownItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% DropdownItem id="uid" %}
{% endDropdownItem %}
"""
        expected = """
<li data-option data-value="" class="bx--dropdown-item"
    title="">
  <a class="bx--dropdown-link" role="menuitemradio" id="item-uid" tabindex="-1" aria-checked="false" id="uid">
  </a>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
