# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class TableTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Table %}
{% endTable %}
"""
        expected = """
<table class="bx--data-table">
</table>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ThTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Th %}
{% endTh %}
"""
        expected = """
<th class="">
  <span class="bx--table-header-label">
</span>
</th>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class TdTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Td %}
{% endTd %}
"""
        expected = """
<td class="">
</td>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class TableOvButtonTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TableOvButton %}
{% endTableOvButton %}
"""
        expected = """
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
    </div>
  </button>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class TdOvButtonTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TdOvButton %}
{% endTdOvButton %}
"""
        expected = """
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <div class="bx--overflow-menu-options__btn"
      title="">
    <div class="bx--overflow-menu-options__option-content">
    </div>
  </div>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class TbSearchTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TbSearch id="uid" %}
"""
        expected = """
<div class="bx--toolbar-search-container-persistent">
  <div data-search class="bx--search" role="search" id="uid">
    <div class="bx--search-magnifier">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
        <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
      </svg>
    </div>
    <label id="label-uid" class="bx--label" for="uid">
    </label>
    <input class="bx--search-input" type="text" id="uid" role="search"
        placeholder="Search" aria-labelledby="label-uid">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
        <path d="M12 4.7L11.3 4 8 7.3 4.7 4 4 4.7 7.3 8 4 11.3 4.7 12 8 8.7 11.3 12 12 11.3 8.7 8z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
