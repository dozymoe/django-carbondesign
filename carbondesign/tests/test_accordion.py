# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class AccordionTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Accordion %}
{% endAccordion %}
"""
        expected = """
<ul data-accordion class="bx--accordion " >
</ul>
"""
        rendered = compare_template(template, expected, {})
        self.assertEqual(*rendered)


class AccordionItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% AccordionItem id='id' %}
{% endAccordionItem %}
"""
        expected = """
<li data-accordion-item class="bx--accordion__item " id="id">
  <button class="bx--accordion__heading" aria-expanded="false"
      aria-controls="pane-id">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
    <div class="bx--accordion__title " >
      None
    </div>
  </button>
  <div id="pane-id" class="bx--accordion__content">
  </div>
</li>
"""
        rendered = compare_template(template, expected, {})
        self.assertEqual(*rendered)
