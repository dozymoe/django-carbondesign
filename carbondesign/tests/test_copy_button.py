# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class CopyButtonTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% CopyButton %}
"""
        expected = """
<button data-copy-btn class="bx--copy-btn" type="button" tabindex="0">
  <span class="bx--assistive-text bx--copy-btn__feedback">Copied!</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--snippet__icon" width="16" height="16" viewBox="0 0 32 32"
      aria-hidden="true">
    <path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z"></path>
    <path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z"></path>
  </svg>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
