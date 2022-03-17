# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class ListBoxTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ListBox form.choice %}
{% endListBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
<label for="id_choice" class="bx--label">
  Choice
</label>
    <div class="bx--list-box">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Open menu" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">{value}</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="combobox" id="menu-id_choice">
      </ul>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ListBoxItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ListBoxItem %}
{% endListBoxItem %}
"""
        expected = """
<li class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        aria-hidden="true" class="bx--list-box__menu-item__selected-icon"
        width="16" height="16" viewBox="0 0 32 32">
      <path d="M13 24L4 15 5.414 13.586 13 21.171 26.586 7.586 28 9 13 24z"></path>
    </svg>
  </div>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
