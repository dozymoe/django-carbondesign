"""
Code Snippet
============

See: https://www.carbondesignsystem.com/components/code-snippet/usage/

Code snippets are strings or small blocks of reusable code that can be copied
and inserted in a code file.

Overview
--------

There are three different variants of code snippets to help cater to varied
line length use cases—inline, single line, and multi-line.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class CodeSnippet(Node):
    """Code Snippet component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('inline', 'single', 'multi')
    "Available variants."
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_copied'] = _("Copied!")
        values['txt_copy'] = _("Copy code")
        values['txt_show_more'] = _("Show more")
        values['txt_show_more_icon'] = _("Show more icon")
        values['txt_show_less'] = _("Show less")

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--snippet--light')


    def render_multi(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--snippet bx--snippet--multi {class}" data-code-snippet {props}>
  <div class="bx--snippet-container" aria-label="{label}{label_suffix}">
    <pre><code>{child}</code></pre>
  </div>
  <button data-copy-btn class="bx--copy-btn" type="button" tabindex="0">
    <span class="bx--assistive-text bx--copy-btn__feedback">{txt_copied}</span>
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
    <span class="bx--snippet-btn--text" data-show-more-text="{txt_show_more}"
        data-show-less-text="{txt_show_less}">
      {txt_show_more}
    </span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        aria-label="{txt_show_more_icon}"
        class="bx--icon-chevron--down bx--snippet__icon" width="16" height="16"
        viewBox="0 0 16 16" role="img">
      <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
    </svg>
  </button>
</{astag}>
"""
        return self.format(template, values)


    def render_single(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--snippet bx--snippet--single {class}" {props}>
  <div tabindex="0"  class="bx--snippet-container" aria-label="{label}{label_suffix}">
    <pre><code>{child}</code></pre>
  </div>
  <button data-copy-btn class="bx--copy-btn" type="button" tabindex="0">
    <span class="bx--assistive-text bx--copy-btn__feedback">{txt_copied}</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--snippet__icon" width="16" height="16" viewBox="0 0 32 32"
        aria-hidden="true">
      <path d="M28,10V28H10V10H28m0-2H10a2,2,0,0,0-2,2V28a2,2,0,0,0,2,2H28a2,2,0,0,0,2-2V10a2,2,0,0,0-2-2Z"></path>
      <path d="M4,18H2V4A2,2,0,0,1,4,2H18V4H4Z"></path>
    </svg>
  </button>
</{astag}>
"""
        return self.format(template, values)


    def render_inline(self, values, context):
        """Output html of the component.
        """
        template = """
<button data-copy-btn type="button"
    class="bx--snippet bx--snippet--inline {class}"
    aria-label="{txt_copy}" tabindex="0" {props}>
  <code>{child}</code>
  <span class="bx--assistive-text bx--copy-btn__feedback">{txt_copied}</span>
</button>
"""
        return self.format(template, values)


components = {
    'Code': CodeSnippet,
}
