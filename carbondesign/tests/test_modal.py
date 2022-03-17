# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class ModalTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Modal id="uid" %}
{% endModal %}
"""
        expected = """
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" aria-labelledby="uid-label"
    aria-describedby="uid-heading" tabindex="-1" id="uid">
  <div class="bx--modal-container">
    <div class="bx--modal-header">
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 16 16" aria-hidden="true">
          <path d="M12 4.7L11.3 4 8 7.3 4.7 4 4 4.7 7.3 8 4 11.3 4.7 12 8 8.7 11.3 12 12 11.3 8.7 8z"></path>
        </svg>
      </button>
    </div>
    <div class="bx--modal-content" tabindex="0">
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ModalTriggerTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" %}
{% endModalTrigger %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" data-modal-target="#uid">
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
