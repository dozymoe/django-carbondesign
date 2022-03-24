# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ToolbarTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Toolbar %}
{% endToolbar %}
"""
        expected = """
<div class="bx--toolbar" data-toolbar>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ToolbarSearchTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ToolbarSearch id="uid" %}
"""
        expected = """
<div class="bx--search bx--search--sm bx--toolbar-search" role="search"
    data-search data-toolbar-search>
  <label for="search__input-uid" class="bx--label">
    Search
  </label>
  <input type="text" class="bx--search-input" id="search__input-uid"
      placeholder="Search">
  <button class="bx--toolbar-search__btn" aria-label="Toolbar Search">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--search-magnifier" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5   C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
    </svg>
  </button>
  <button class="bx--search-close bx--search-close--hidden"
      title="Clear search input" aria-label="Clear search input">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 32 32" aria-hidden="true">
      <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
    </svg>
  </button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ToolbarItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ToolbarItem %}
{% endToolbarItem %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu" tabindex="0"
    aria-label="List of options">
  <ul class="bx--overflow-menu-options">
  </ul>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ToolbarMultiSelectTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ToolbarMultiSelect form.choice %}
"""
        expected = """
<li class="bx--toolbar-menu__option">
  <input id="id_choice-0" class="bx--checkbox" type="checkbox" value="val1"
      name="choice" data-floating-menu-primary-focus checked>
  <label for="id_choice-0" class="bx--checkbox-label">
    Value One
  </label>
</li>
<li class="bx--toolbar-menu__option">
  <input id="id_choice-1" class="bx--checkbox" type="checkbox" value="val2"
      name="choice">
  <label for="id_choice-1" class="bx--checkbox-label">
    Value Two
  </label>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ToolbarRadioTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ToolbarRadio form.choice %}
"""
        expected = """
<fieldset data-row-height class="bx--radio-button-group">
  <legend class="bx--visually-hidden">Choice</legend>
<li class="bx--toolbar-menu__option">
  <input id="id_choice-0" class="bx--radio-button" type="radio" value="val1"
      name="choice" data-floating-menu-primary-focus checked>
  <label for="id_choice-0" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    Value One
  </label>
</li>
<li class="bx--toolbar-menu__option">
  <input id="id_choice-1" class="bx--radio-button" type="radio" value="val2"
      name="choice">
  <label for="id_choice-1" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    Value Two
  </label>
</li>
</fieldset>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ToolbarHeadingTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ToolbarHeading %}
{% endToolbarHeading %}
"""
        expected = """
<li class="bx--toolbar-menu__title">
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ToolbarDividerTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ToolbarDivider %}
"""
        expected = """
<hr class="bx--toolbar-menu__divider"/>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
