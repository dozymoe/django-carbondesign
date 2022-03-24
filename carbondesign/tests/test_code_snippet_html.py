# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class CodeSnippetHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_single(self):
        template = """
{% load carbondesign %}
{% Code mode="single" label="Code Snippet Text" %}
@mixin grid-container {
  width: 100%;
  padding-right: padding(mobile);
  padding-left: padding(mobile);

  @include breakpoint(bp--xs--major) {
    padding-right: padding(xs);
    padding-left: padding(xs);
  }
}

$z-indexes: (
  modal : 9000,
  overlay : 8000,
  dropdown : 7000,
  header : 6000,
  footer : 5000,
  hidden : - 1,
  overflowHidden: - 1,
  floating: 10000
);
{% endCode %}
"""
        expected = """
<div class="bx--snippet bx--snippet--single" >
  <div tabindex="0"  class="bx--snippet-container" aria-label="Code Snippet Text">
    <pre><code>
@mixin grid-container {
  width: 100%;
  padding-right: padding(mobile);
  padding-left: padding(mobile);

  @include breakpoint(bp--xs--major) {
    padding-right: padding(xs);
    padding-left: padding(xs);
  }
}

$z-indexes: (
  modal : 9000,
  overlay : 8000,
  dropdown : 7000,
  header : 6000,
  footer : 5000,
  hidden : - 1,
  overflowHidden: - 1,
  floating: 10000
);
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
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_inline(self):
        template = """
{% load carbondesign %}
<p>Here is an example of a text that a user would be reading. In this paragraph
    would be {% Code %}inline code{% endCode %} that the user could look at
    and copy in to their code editor.</p>
"""
        expected = """
<p>Here is an example of a text that a user would be reading. In this paragraph
    would be 
<button data-copy-btn type="button"
    class="bx--snippet bx--snippet--inline "
    aria-label="Copy code" tabindex="0">
  <code>inline code</code>
  <span class="bx--assistive-text bx--copy-btn__feedback">Copied!</span>
</button>
 that the user could look at
    and copy in to their code editor.</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_inline_light(self):
        template = """
{% load carbondesign %}
<p>Here is an example of a text that a user would be reading. In this paragraph
    would be {% Code light=True %}inline code{% endCode %} that the user could
    look at and copy in to their code editor.</p>
"""
        expected = """
<p>Here is an example of a text that a user would be reading. In this paragraph
    would be 
<button data-copy-btn type="button"
    class="bx--snippet bx--snippet--inline bx--snippet--light"
    aria-label="Copy code" tabindex="0">
  <code>inline code</code>
  <span class="bx--assistive-text bx--copy-btn__feedback">Copied!</span>
</button>
 that the user could
    look at and copy in to their code editor.</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_multi(self):
        template = """
{% load carbondesign %}
{% Code mode="multi" label="Code Snippet Text" %}
@mixin grid-container {
  width: 100%;
  padding-right: padding(mobile);
  padding-left: padding(mobile);

  @include breakpoint(bp--xs--major) {
    padding-right: padding(xs);
    padding-left: padding(xs);
  }
}

$z-indexes: (
  modal : 9000,
  overlay : 8000,
  dropdown : 7000,
  header : 6000,
  footer : 5000,
  hidden : - 1,
  overflowHidden: - 1,
  floating: 10000
);
{% endCode %}
"""
        expected = """
<div class="bx--snippet bx--snippet--multi" data-code-snippet>
  <div class="bx--snippet-container" aria-label="Code Snippet Text">
    <pre><code>
@mixin grid-container {
  width: 100%;
  padding-right: padding(mobile);
  padding-left: padding(mobile);

  @include breakpoint(bp--xs--major) {
    padding-right: padding(xs);
    padding-left: padding(xs);
  }
}

$z-indexes: (
  modal : 9000,
  overlay : 8000,
  dropdown : 7000,
  header : 6000,
  footer : 5000,
  hidden : - 1,
  overflowHidden: - 1,
  floating: 10000
);
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
