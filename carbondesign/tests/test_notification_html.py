# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class NotificationHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_inline(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
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
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Subtitle text goes here.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_inline_error(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" variant="error" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--error" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z"></path>
  <path d="M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Subtitle text goes here.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_inline_success(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" variant="success" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--success" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-4.9,0-9,4.1-9,9s4.1,9,9,9s9-4,9-9S15,1,10,1z M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z"></path>
  <path fill="none" d="M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_inline_warning(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" variant="warning" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--warning" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1  s1,0.4,1,1S10.6,16,10,16z"></path>
  <path d="M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1s1,0.4,1,1S10.6,16,10,16z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Subtitle text goes here.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_inline_low_contrast_info(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" low_contrast=True %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--info bx--inline-notification--low-contrast" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 32 32" aria-hidden="true">
  <path fill="none" d="M16,8a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,13.875H17.125v-8H13v2.25h1.875v5.75H12v2.25h8Z" data-icon-path="inner-path"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,6a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,16.125H12v-2.25h2.875v-5.75H13v-2.25h4.125v8H20Z"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Subtitle text goes here.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_inline_low_contrast_error(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" low_contrast=True variant="error" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--error bx--inline-notification--low-contrast" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z"></path>
  <path d="M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Subtitle text goes here.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_inline_low_contrast_success(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" low_contrast=True variant="success" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--success bx--inline-notification--low-contrast" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-4.9,0-9,4.1-9,9s4.1,9,9,9s9-4,9-9S15,1,10,1z M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z"></path>
  <path fill="none" d="M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_inline_low_contrast_warning(self):
        template = """
{% load carbondesign %}
{% Notification mode="inline" low_contrast=True variant="warning" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--inline-notification bx--inline-notification--warning bx--inline-notification--low-contrast" role="alert">
  <div class="bx--inline-notification__details">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--inline-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1  s1,0.4,1,1S10.6,16,10,16z"></path>
  <path d="M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1s1,0.4,1,1S10.6,16,10,16z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <div class="bx--inline-notification__text-wrapper">
<h3 class="bx--inline-notification__title">
    Notification title
  </h3>
<p class="bx--inline-notification__subtitle">
    Subtitle text goes here.
  </p>
    </div>
  </div>
<button tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost"
    type="button">
      Action
</button>
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

    def test_toast_low_contrast_info(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" low_contrast=True %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--info bx--toast-notification--low-contrast" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 32 32" aria-hidden="true">
  <path fill="none" d="M16,8a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,13.875H17.125v-8H13v2.25h1.875v5.75H12v2.25h8Z" data-icon-path="inner-path"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,6a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,16.125H12v-2.25h2.875v-5.75H13v-2.25h4.125v8H20Z"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Subtitle text goes here.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_toast_low_contrast_error(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" low_contrast=True variant="error" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--error bx--toast-notification--low-contrast" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z"></path>
  <path d="M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Subtitle text goes here.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_toast_low_contrast_success(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" low_contrast=True variant="success" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--success bx--toast-notification--low-contrast" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-4.9,0-9,4.1-9,9s4.1,9,9,9s9-4,9-9S15,1,10,1z M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z"></path>
  <path fill="none" d="M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_toast_low_contrast_warning(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" low_contrast=True variant="warning" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--warning bx--toast-notification--low-contrast" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1  s1,0.4,1,1S10.6,16,10,16z"></path>
  <path d="M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1s1,0.4,1,1S10.6,16,10,16z" data-icon-path="inner-path" opacity="0"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Subtitle text goes here.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_toast(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--info" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 32 32" aria-hidden="true">
  <path fill="none" d="M16,8a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,13.875H17.125v-8H13v2.25h1.875v5.75H12v2.25h8Z" data-icon-path="inner-path"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,6a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,16.125H12v-2.25h2.875v-5.75H13v-2.25h4.125v8H20Z"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Subtitle text goes here.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_toast_error(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" variant="error" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--error" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z"></path>
  <path d="M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Subtitle text goes here.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_toast_success(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" variant="success" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--success" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-4.9,0-9,4.1-9,9s4.1,9,9,9s9-4,9-9S15,1,10,1z M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z"></path>
  <path fill="none" d="M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Our goal is to become better at our craft and raise our collective
    knowledge by sharing experiences, best practices, what we have recently
    learned or what we are working on.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_toast_warning(self):
        template = """
{% load carbondesign %}
{% Notification mode="toast" variant="warning" %}
  {% NotificationTitle %}
    Notification title
  {% endNotificationTitle %}
  {% NotificationSubtitle %}
    Subtitle text goes here.
  {% endNotificationSubtitle %}
  {% NotificationCaption %}
    Time stamp [00:00:00]
  {% endNotificationCaption %}

  {% Slot 'action' %}
    {% NotificationButton type="button" %}
      Action
    {% endNotificationButton %}
  {% endSlot %}
{% endNotification %}
"""
        expected = """
<div data-notification class="bx--toast-notification bx--toast-notification--warning" role="alert">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toast-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1  s1,0.4,1,1S10.6,16,10,16z"></path>
  <path d="M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1s1,0.4,1,1S10.6,16,10,16z" data-icon-path="inner-path" opacity="0"></path>
</svg>
  <div class="bx--toast-notification__details">
<h3 class="bx--toast-notification__title">
    Notification title
  </h3>
<p class="bx--toast-notification__subtitle">
    Subtitle text goes here.
  </p>
<p class="bx--toast-notification__caption">
    Time stamp [00:00:00]
  </p>
  </div>
<button data-notification-btn class="bx--toast-notification__close-button"
    type="button" aria-label="close">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toast-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)