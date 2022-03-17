# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class ButtonTertiaryFieldTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Button field=True variant="tertiary" type="button" %}
  Button
{% endButton %}
"""
        expected = """
<button class="bx--btn bx--btn--tertiary bx--btn--field" type="button">
  Button
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_disabled(self):
        template = """
{% load carbondesign %}
{% Button field=True variant="tertiary" type="button" disabled=True %}
  Button
{% endButton %}
"""
        expected = """
<button class="bx--btn bx--btn--tertiary bx--btn--field" disabled="disabled" type="button">
  Button
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_icon(self):
        template = """
{% load carbondesign %}
{% Button field=True variant="tertiary" type="button" %}
  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
    </svg>
  {% endSlot %}

  With icon
{% endButton %}
"""
        expected = """
<button class="bx--btn bx--btn--tertiary bx--btn--field" type="button">
  With icon
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true" class="bx--btn__icon">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
    </svg>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_icon_disabled(self):
        template = """
{% load carbondesign %}
{% Button field=True variant="tertiary" type="button" disabled=True %}
  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
    </svg>
  {% endSlot %}

  With icon
{% endButton %}
"""
        expected = """
<button class="bx--btn bx--btn--tertiary bx--btn--field" disabled="disabled" type="button">
  With icon
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true" class="bx--btn__icon">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
    </svg>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_icon_only(self):
        template = """
{% load carbondesign %}
{% IconButton variant="tertiary" field=True %}
  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
    </svg>
  {% endSlot %}

  Add
{% endIconButton %}
"""
        expected = """
<button class="bx--btn bx--btn--tertiary bx--btn--field bx--btn--icon-only bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">
  Add
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true" class="bx--btn__icon">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
    </svg>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_demo(self):
        template = """
{% load carbondesign %}
<div class="example-input-button-pairing">
  <div class="bx--form-item">
    <label for="text-input-3" class="bx--label">Text Input label</label>
    <input id="text-input-3" type="text"
        class="bx--text-input"
        placeholder="Optional placeholder text">
  </div>
  <div class="example-button-wrapper">
    {% Button field=True variant="tertiary" type="button" %}
      Button
    {% endButton %}
  </div>
</div>
"""
        expected = """
<div class="example-input-button-pairing">
  <div class="bx--form-item">
    <label for="text-input-3" class="bx--label">Text Input label</label>
    <input id="text-input-3" type="text"
        class="bx--text-input"
        placeholder="Optional placeholder text">
  </div>
  <div class="example-button-wrapper">
<button class="bx--btn bx--btn--tertiary bx--btn--field" type="button">
      Button
</button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
