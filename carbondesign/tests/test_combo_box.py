# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class ComboBoxTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ComboBox form.choice %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
<label for="id_choice" class="bx--label">
  Choice
</label>
    <div class="bx--combo-box bx--list-box">
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-expanded="false" aria-haspopup="listbox">
        <select name="choice" class="bx--text-input" aria-autocomplete="list" aria-expanded="false" autocomplete="off" aria-owns="menu-id_choice" id="id_choice">
  <option value="val1" selected>Value One</option>
  <option value="val2">Value Two</option>
</select>
<div class="bx--list-box__selection" role="button">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" title="Clear all"
      aria-label="Clear all" width="16" height="16" viewBox="0 0 32 32"
      role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-id_choice"
          aria-label="Choice">
      </ul>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ComboBoxItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ComboBoxItem %}
{% endComboBoxItem %}
"""
        expected = """
<li class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option" tabindex="0">
  </div>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
