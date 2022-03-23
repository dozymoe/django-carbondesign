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
    aria-modal="true" tabindex="-1">
  <div class="bx--modal-container">
    <div class="bx--modal-header">
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal" data-modal-primary-focus="">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>
    <div class="bx--modal-content">
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
