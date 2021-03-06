# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ButtonGhostTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Button variant="ghost" type="button" %}
  Button
{% endButton %}
"""
        expected = """
<button class="bx--btn bx--btn--ghost" type="button">
  Button
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_disabled(self):
        template = """
{% load carbondesign %}
{% Button variant="ghost" type="button" disabled=True %}
  Button
{% endButton %}
"""
        expected = """
<button class="bx--btn bx--btn--ghost" type="button" disabled="disabled">
  Button
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_icon(self):
        template = """
{% load carbondesign %}
{% Button variant="ghost" type="button" %}
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
<button class="bx--btn bx--btn--ghost" type="button">
  With icon
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
    </svg>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_icon_disabled(self):
        template = """
{% load carbondesign %}
{% Button variant="ghost" type="button" disabled=True %}
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
<button class="bx--btn bx--btn--ghost" type="button" disabled="disabled">
  With icon
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
      <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
    </svg>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
