# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class AccordionTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Accordion %}
{% endAccordion %}
"""
        expected = """
<ul data-accordion class="bx--accordion">
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class AccordionItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% AccordionItem id="uid" %}
{% endAccordionItem %}
"""
        expected = """
<li data-accordion-item class="bx--accordion__item">
  <button class="bx--accordion__heading" aria-expanded="false"
      aria-controls="uid">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
  </button>
  <div id="uid" class="bx--accordion__content">
  </div>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class AccordionHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_accordion(self):
        template = """
{% load carbondesign %}
{% Accordion %}
  {% AccordionItem id="pane1" label="Section 1 title" %}
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  {% endAccordionItem %}

  {% AccordionItem id="pane2" label="Section 2 title" %}
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  {% endAccordionItem %}

  {% AccordionItem id="pane3" label="Section 3 title" %}
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  {% endAccordionItem %}

  {% AccordionItem id="pane4" label="Section 4 title" %}
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  {% endAccordionItem %}
{% endAccordion %}
"""
        expected = """
<ul data-accordion class="bx--accordion">
<li data-accordion-item class="bx--accordion__item">
  <button class="bx--accordion__heading" aria-expanded="false"
      aria-controls="pane1">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
<div class="bx--accordion__title">
  Section 1 title
</div>
  </button>
  <div id="pane1" class="bx--accordion__content">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  </div>
</li>
<li data-accordion-item class="bx--accordion__item">
  <button class="bx--accordion__heading" aria-expanded="false"
      aria-controls="pane2">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
<div class="bx--accordion__title">
  Section 2 title
</div>
  </button>
  <div id="pane2" class="bx--accordion__content">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  </div>
</li>
<li data-accordion-item class="bx--accordion__item">
  <button class="bx--accordion__heading" aria-expanded="false"
      aria-controls="pane3">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
<div class="bx--accordion__title">
  Section 3 title
</div>
  </button>
  <div id="pane3" class="bx--accordion__content">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  </div>
</li>
<li data-accordion-item class="bx--accordion__item">
  <button class="bx--accordion__heading" aria-expanded="false"
      aria-controls="pane4">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
<div class="bx--accordion__title">
  Section 4 title
</div>
  </button>
  <div id="pane4" class="bx--accordion__content">
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat.</p>
  </div>
</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
