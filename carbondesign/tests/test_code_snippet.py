# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class CodeSnippetTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Code %}
{% endCode %}
"""
        expected = """
<div class="bx--snippet bx--snippet--multi" data-code-snippet>
  <div class="bx--snippet-container" aria-label="None">
    <pre><code>
</code></pre>
  </div>
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
  <button class="bx--btn bx--btn--ghost bx--btn--sm bx--snippet-btn--expand"
      type="button">
    <span class="bx--snippet-btn--text" data-show-more-text="Show more"
        data-show-less-text="Show less">
      Show more
    </span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        aria-label="Show more icon"
        class="bx--icon-chevron--down bx--snippet__icon" width="16" height="16"
        viewBox="0 0 16 16" role="img">
      <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
    </svg>
  </button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
