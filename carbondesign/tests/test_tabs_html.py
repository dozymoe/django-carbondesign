# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TabsHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Tabs %}
  {% Slot 'header' %}
    {% TabItem target="tab-panel-1" active=True %}
      Tab label 1
    {% endTabItem %}
    {% TabItem target="tab-panel-2" %}
      Tab label 2
    {% endTabItem %}
    {% TabItem target="tab-panel-3" %}
      Tab label 3
    {% endTabItem %}
    {% TabItem target="tab-panel-4" disabled=True %}
      Tab label 4
    {% endTabItem %}
  {% endSlot %}

  {% TabContent id="tab-panel-1" active=True %}
    Content for first tab goes here.
  {% endTabContent %}
  {% TabContent id="tab-panel-2" %}
    Content for second tab goes here.
  {% endTabContent %}
  {% TabContent id="tab-panel-3" %}
    Content for third tab goes here.
  {% endTabContent %}
  {% TabContent id="tab-panel-4" %}
    Content for fourth tab goes here.
  {% endTabContent %}
{% endTabs %}
"""
        expected = """
<div data-tabs class="bx--tabs">
  <div class="bx--tabs-trigger" tabindex="0">
    <a href="javascript:void(0)" class="bx--tabs-trigger-text" tabindex="-1"></a>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
    </svg>
  </div>
  <ul class="bx--tabs__nav bx--tabs__nav--hidden" role="tablist">
<li class="bx--tabs__nav-item bx--tabs__nav-item--selected" data-target="#tab-panel-1"
    role="tab" aria-selected="true">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-1" id="tab-link-tab-panel-1">
      Tab label 1
  </a>
</li>
<li class="bx--tabs__nav-item" data-target="#tab-panel-2"
    role="tab">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-2" id="tab-link-tab-panel-2">
      Tab label 2
  </a>
</li>
<li class="bx--tabs__nav-item" data-target="#tab-panel-3"
    role="tab">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-3" id="tab-link-tab-panel-3">
      Tab label 3
  </a>
</li>
<li class="bx--tabs__nav-item bx--tabs__nav-item--disabled" data-target="#tab-panel-4"
    role="tab" aria-disabled="true">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-4" id="tab-link-tab-panel-4">
      Tab label 4
  </a>
</li>
  </ul>
</div>
<div class="bx--tab-content">
<div id="tab-panel-1" role="tabpanel" aria-labelledby="tab-link-tab-panel-1" aria-hidden="false">
  <div>
    Content for first tab goes here.
  </div>
</div>
<div id="tab-panel-2" role="tabpanel" aria-labelledby="tab-link-tab-panel-2" aria-hidden="true" hidden="">
  <div>
    Content for second tab goes here.
  </div>
</div>
<div id="tab-panel-3" role="tabpanel" aria-labelledby="tab-link-tab-panel-3" aria-hidden="true" hidden="">
  <div>
    Content for third tab goes here.
  </div>
</div>
<div id="tab-panel-4" role="tabpanel" aria-labelledby="tab-link-tab-panel-4" aria-hidden="true" hidden="">
  <div>
    Content for fourth tab goes here.
  </div>
</div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_container(self):
        template = """
{% load carbondesign %}
{% Tabs container=True %}
  {% Slot 'header' %}
    {% TabItem target="tab-panel-1" active=True %}
      Tab label 1
    {% endTabItem %}
    {% TabItem target="tab-panel-2" %}
      Tab label 2
    {% endTabItem %}
    {% TabItem target="tab-panel-3" %}
      Tab label 3
    {% endTabItem %}
    {% TabItem target="tab-panel-4" disabled=True %}
      Tab label 4
    {% endTabItem %}
  {% endSlot %}

  {% TabContent id="tab-panel-1" active=True %}
    Content for first tab goes here.
  {% endTabContent %}
  {% TabContent id="tab-panel-2" %}
    Content for second tab goes here.
  {% endTabContent %}
  {% TabContent id="tab-panel-3" %}
    Content for third tab goes here.
  {% endTabContent %}
  {% TabContent id="tab-panel-4" %}
    Content for fourth tab goes here.
  {% endTabContent %}
{% endTabs %}
"""
        expected = """
<div data-tabs class="bx--tabs bx--tabs--container">
  <div class="bx--tabs-trigger" tabindex="0">
    <a href="javascript:void(0)" class="bx--tabs-trigger-text" tabindex="-1"></a>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
    </svg>
  </div>
  <ul class="bx--tabs__nav bx--tabs__nav--hidden" role="tablist">
<li class="bx--tabs__nav-item bx--tabs__nav-item--selected" data-target="#tab-panel-1"
    role="tab" aria-selected="true">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-1" id="tab-link-tab-panel-1">
      Tab label 1
  </a>
</li>
<li class="bx--tabs__nav-item" data-target="#tab-panel-2"
    role="tab">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-2" id="tab-link-tab-panel-2">
      Tab label 2
  </a>
</li>
<li class="bx--tabs__nav-item" data-target="#tab-panel-3"
    role="tab">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-3" id="tab-link-tab-panel-3">
      Tab label 3
  </a>
</li>
<li class="bx--tabs__nav-item bx--tabs__nav-item--disabled" data-target="#tab-panel-4"
    role="tab" aria-disabled="true">
  <a tabindex="0" class="bx--tabs__nav-link" href="javascript:void(0)"
      role="tab" aria-controls="tab-panel-4" id="tab-link-tab-panel-4">
      Tab label 4
  </a>
</li>
  </ul>
</div>
<div class="bx--tab-content">
<div id="tab-panel-1" role="tabpanel" aria-labelledby="tab-link-tab-panel-1" aria-hidden="false">
  <div>
    Content for first tab goes here.
  </div>
</div>
<div id="tab-panel-2" role="tabpanel" aria-labelledby="tab-link-tab-panel-2" aria-hidden="true" hidden="">
  <div>
    Content for second tab goes here.
  </div>
</div>
<div id="tab-panel-3" role="tabpanel" aria-labelledby="tab-link-tab-panel-3" aria-hidden="true" hidden="">
  <div>
    Content for third tab goes here.
  </div>
</div>
<div id="tab-panel-4" role="tabpanel" aria-labelledby="tab-link-tab-panel-4" aria-hidden="true" hidden="">
  <div>
    Content for fourth tab goes here.
  </div>
</div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
