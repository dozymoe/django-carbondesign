# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TabsTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Tabs %}
{% endTabs %}
"""
        expected = """
<div data-tabs class="bx--tabs">
  <div class="bx--tabs-trigger" tabindex="0">
    <a href="javascript:void(0)" class="bx--tabs-trigger-text" tabindex="-1">
    </a>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
    </svg>
  </div>
  <ul class="bx--tabs__nav bx--tabs__nav--hidden" role="tablist">
  </ul>
</div>
<div class="bx--tab-content">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class TabItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TabItem %}
{% endTabItem %}
"""
        expected = """
<li class="bx--tabs__nav-item" data-target="None" role="tab">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="None">
  </a>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class TabContentTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TabContent %}
{% endTabContent %}
"""
        expected = """
<div role="tabpanel" aria-labelledby="None" aria-hidden="false" aria-hidden="true" hidden="">
  <div>
</div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
