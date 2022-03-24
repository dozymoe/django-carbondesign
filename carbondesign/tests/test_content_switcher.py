# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ContentSwitcherTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ContentSwitcher %}
{% endContentSwitcher %}
"""
        expected = """
<div data-content-switcher class="bx--content-switcher" role="tablist">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ContentSwitcherItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ContentSwitcherItem target='uid' %}
{% endContentSwitcherItem %}
"""
        expected = """
<button class="bx--content-switcher-btn" data-target="uid"
    role="tab">
  <span class="bx--content-switcher__label">
</span>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
