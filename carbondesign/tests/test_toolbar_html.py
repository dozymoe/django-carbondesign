# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    checkbox = forms.ChoiceField(required=False,
            label="FILTER BY",
            choices=(
                ('filter-option-1', "Filter option 1"),
                ('filter-option-2', "Filter option 2"),
                ('filter-option-3', "Filter option 3"),
            ))
    radio = forms.ChoiceField(required=False,
            label="ROW HEIGHT",
            choices=(
                ('short', "Short"),
                ('tall', "Tall"),
            ))


class ToolbarHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        form = DummyForm(data={'radio': 'short'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Toolbar %}
  {% ToolbarSearch id="search__input" %}
  {% ToolbarItem filter=True %}
    {% ToolbarMultiSelect form.checkbox %}
    {% Slot 'icon' %}
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
          viewBox="0 0 32 32">
        <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"></path>
      </svg>
    {% endSlot %}
  {% endToolbarItem %}
  {% ToolbarItem %}
    {% ToolbarButton type="button" %}Refresh table{% endToolbarButton %}
    {% ToolbarDivider %}
    {% ToolbarRadio form.radio legend="Select table row height" %}
    {% Slot 'icon' %}
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
          viewBox="0 0 32 32">
        <circle cx="16" cy="8" r="2"></circle>
        <circle cx="16" cy="16" r="2"></circle>
        <circle cx="16" cy="24" r="2"></circle>
      </svg>
    {% endSlot %}
  {% endToolbarItem %}
{% endToolbar %}
"""
        expected = """
<div class="bx--toolbar" data-toolbar>
<div class="bx--search bx--search--sm bx--toolbar-search" role="search"
    data-search data-toolbar-search>
  <label for="search__input" class="bx--label">
    Search
  </label>
  <input type="text" class="bx--search-input" id="search__input"
      placeholder="Search">
  <button class="bx--toolbar-search__btn" aria-label="Toolbar Search">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--search-magnifier" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
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
<div data-overflow-menu class="bx--overflow-menu" tabindex="0"
    aria-label="List of options">
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" class="bx--overflow-menu__icon bx--toolbar-filter-icon" style="width:16;height:16" aria-hidden="true">
        <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
      </svg>
  <ul class="bx--overflow-menu-options">
<li class="bx--toolbar-menu__title">FILTER BY</li>
<li class="bx--toolbar-menu__option">
  <input id="id_checkbox-0" class="bx--checkbox" type="checkbox" value="filter-option-1"
      name="checkbox" data-floating-menu-primary-focus>
  <label for="id_checkbox-0" class="bx--checkbox-label">
    Filter option 1
  </label>
</li>
<li class="bx--toolbar-menu__option">
  <input id="id_checkbox-1" class="bx--checkbox" type="checkbox" value="filter-option-2"
      name="checkbox">
  <label for="id_checkbox-1" class="bx--checkbox-label">
    Filter option 2
  </label>
</li>
<li class="bx--toolbar-menu__option">
  <input id="id_checkbox-2" class="bx--checkbox" type="checkbox" value="filter-option-3"
      name="checkbox">
  <label for="id_checkbox-2" class="bx--checkbox-label">
    Filter option 3
  </label>
</li>
  </ul>
</div>
<div data-overflow-menu class="bx--overflow-menu" tabindex="0"
    aria-label="List of options">
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" class="bx--overflow-menu__icon" style="width:16;height:16" aria-hidden="true">
        <circle cx="16" cy="8" r="2"/>
        <circle cx="16" cy="16" r="2"/>
        <circle cx="16" cy="24" r="2"/>
      </svg>
  <ul class="bx--overflow-menu-options">
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" type="button">
    Refresh table
  </button>
</li>
    <hr class="bx--toolbar-menu__divider"/>
<li class="bx--toolbar-menu__title">ROW HEIGHT</li>
<fieldset data-row-height class="bx--radio-button-group">
  <legend class="bx--visually-hidden">Select table row height</legend>
<li class="bx--toolbar-menu__option">
  <input id="id_radio-0" class="bx--radio-button" type="radio" value="short"
      name="radio" data-floating-menu-primary-focus checked>
  <label for="id_radio-0" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    Short
  </label>
</li>
<li class="bx--toolbar-menu__option">
  <input id="id_radio-1" class="bx--radio-button" type="radio" value="tall"
      name="radio">
  <label for="id_radio-1" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    Tall
  </label>
</li>
</fieldset>
  </ul>
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
