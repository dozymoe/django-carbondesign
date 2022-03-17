# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class NotificationTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Notification %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--info" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 32 32" aria-hidden="true">
  <path fill="none" d="M16,8a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,13.875H17.125v-8H13v2.25h1.875v5.75H12v2.25h8Z" data-icon-path="inner-path"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,6a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,16.125H12v-2.25h2.875v-5.75H13v-2.25h4.125v8H20Z"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
    </div>
  </div>
<button data-notification-btn class="bx--inline-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--inline-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class NotificationButtonTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% NotificationButton %}
{% endNotificationButton %}
"""
        expected = """
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost">
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class NotificationTitleTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% NotificationTitle %}
{% endNotificationTitle %}
"""
        expected = """
<h3 class="bx--inline-notification__title">
</h3>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class NotificationSubtitleTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% NotificationSubtitle %}
{% endNotificationSubtitle %}
"""
        expected = """
<p class="bx--inline-notification__subtitle">
</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class NotificationCaptionTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% NotificationCaption %}
{% endNotificationCaption %}
"""
        expected = """
<p class="bx--inline-notification__caption">
</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
