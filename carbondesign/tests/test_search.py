# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class SearchTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Search id="uid" %}
"""
        expected = """
<div class="bx--form-item">
  <div data-search role="search" class="bx--search">
    <label id="label-uid" class="bx--label" for="uid">
      Search
    </label>
    <input class="bx--search-input" type="text" id="uid"
        placeholder="Search">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--search-magnifier" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5 C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
    </svg>
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--search-clear" width="16" height="16" viewBox="0 0 32 32"
          aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
