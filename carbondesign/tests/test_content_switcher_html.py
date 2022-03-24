# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ContentSwitcherHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% ContentSwitcher label="Demo switch content" %}
  {% ContentSwitcherItem target=".demo--panel--opt-1" active=True %}
    First section
  {% endContentSwitcherItem %}
  {% ContentSwitcherItem target=".demo--panel--opt-2" %}
    Second section
  {% endContentSwitcherItem %}
  {% ContentSwitcherItem target=".demo--panel--opt-3" %}
    Third section
  {% endContentSwitcherItem %}
{% endContentSwitcher %}
"""
        expected = """
<div data-content-switcher class="bx--content-switcher" role="tablist"
    aria-label="Demo switch content">
<button class="bx--content-switcher-btn bx--content-switcher--selected" data-target=".demo--panel--opt-1"
    role="tab" aria-selected="true">
  <span class="bx--content-switcher__label">
    First section
  </span>
</button>
<button class="bx--content-switcher-btn" data-target=".demo--panel--opt-2"
    role="tab">
  <span class="bx--content-switcher__label">
    Second section
  </span>
</button>
<button class="bx--content-switcher-btn" data-target=".demo--panel--opt-3"
    role="tab">
  <span class="bx--content-switcher__label">
    Third section
  </span>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_disabled(self):
        template = """
{% load carbondesign %}
{% ContentSwitcher label="Demo switch content" %}
  {% ContentSwitcherItem target=".demo--panel--opt-1" active=True disabled=True %}
    First section
  {% endContentSwitcherItem %}
  {% ContentSwitcherItem target=".demo--panel--opt-2" disabled=True %}
    Second section
  {% endContentSwitcherItem %}
  {% ContentSwitcherItem target=".demo--panel--opt-3" disabled=True %}
    Third section
  {% endContentSwitcherItem %}
{% endContentSwitcher %}
"""
        expected = """
<div data-content-switcher class="bx--content-switcher" role="tablist"
    aria-label="Demo switch content">
<button class="bx--content-switcher-btn bx--content-switcher--selected" data-target=".demo--panel--opt-1"
    role="tab" aria-selected="true" disabled="">
  <span class="bx--content-switcher__label">
    First section
  </span>
</button>
<button class="bx--content-switcher-btn" data-target=".demo--panel--opt-2"
    role="tab" disabled="">
  <span class="bx--content-switcher__label">
    Second section
  </span>
</button>
<button class="bx--content-switcher-btn" data-target=".demo--panel--opt-3"
    role="tab" disabled="">
  <span class="bx--content-switcher__label">
    Third section
  </span>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
