"""
Notification
============

See: https://www.carbondesignsystem.com/components/notification/usage/

Notifications are messages that communicate information to the user. The two
main variants of notifications are toast notifications and inline notifications.

Overview
--------

Use notifications to inform users of updates or changes to system status.
Communicating with users and providing immediate feedback are important for
building trust. While notifications are an effective method of communicating
with users, they are disruptive and should be used sparingly.

For more context on when to use each notification variant, including modals,
refer to the notifications pattern. Carbon only supports inline, toast, and
modal notification variants, although some product teams also support banners
and notification centers.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.contrib.messages import constants
from django.utils.translation import gettext as _
#-
from .base import Node

class Notification(Node):
    """Notification component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('action',)
    "Named children."
    MODES = ('inline', 'toast')
    "Available variants."
    NODE_PROPS = ('variant', 'low_contrast')
    "Extended Template Tag arguments."
    TEMPLATES = ('icon', 'close')
    "Conditional templates."
    POSSIBLE_VARIANT = ('info', 'success', 'warning', 'error')
    "Documentation only."

    variant = None

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_close'] = _("close")

        self.variant = self.eval(self.kwargs.get('variant', 'info'), context)
        if self.variant in (constants.DEBUG, constants.INFO):
            self.variant = 'info'
        elif self.variant == constants.SUCCESS:
            self.variant = 'success'
        elif self.variant == constants.WARNING:
            self.variant = 'warning'
        elif self.variant == constants.ERROR:
            self.variant = 'error'

        values['class'].append(f'bx--{self.mode}-notification--{self.variant}')

        if self.eval(self.kwargs.get('low_contrast'), context):
            values['class'].append(f'bx--{self.mode}-notification--low-contrast')

        context['mode'] = self.mode


    def render_inline(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-notification class="bx--inline-notification {class}" role="alert">
  <div class="bx--inline-notification__details">
    {tmpl_icon}
    <div class="bx--inline-notification__text-wrapper">
      {child}
    </div>
  </div>
  {slot_action}
  {tmpl_close}
</div>
"""
        return self.format(template, values, context)


    def render_toast(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-notification class="bx--toast-notification {class}" role="alert">
  {tmpl_icon}
  <div class="bx--toast-notification__details">
    {child}
  </div>
  {tmpl_close}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.variant == 'info':
            template = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--{mode}-notification__icon" width="20" height="20"
    viewBox="0 0 32 32" aria-hidden="true">
  <path fill="none" d="M16,8a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,13.875H17.125v-8H13v2.25h1.875v5.75H12v2.25h8Z" data-icon-path="inner-path"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,6a1.5,1.5,0,1,1-1.5,1.5A1.5,1.5,0,0,1,16,8Zm4,16.125H12v-2.25h2.875v-5.75H13v-2.25h4.125v8H20Z"></path>
</svg>
"""
        elif self.variant == 'error':
            template = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--{mode}-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z"></path>
  <path d="M13.5,14.5l-8-8l1-1l8,8L13.5,14.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
"""
        elif self.variant == 'success':
            template = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--{mode}-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-4.9,0-9,4.1-9,9s4.1,9,9,9s9-4,9-9S15,1,10,1z M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z"></path>
  <path fill="none" d="M8.7,13.5l-3.2-3.2l1-1l2.2,2.2l4.8-4.8l1,1L8.7,13.5z" data-icon-path="inner-path" opacity="0"></path>
</svg>
"""
        elif self.variant == 'warning':
            template = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--{mode}-notification__icon" width="20" height="20"
    viewBox="0 0 20 20" aria-hidden="true">
  <path d="M10,1c-5,0-9,4-9,9s4,9,9,9s9-4,9-9S15,1,10,1z M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1  s1,0.4,1,1S10.6,16,10,16z"></path>
  <path d="M9.2,5h1.5v7H9.2V5z M10,16c-0.6,0-1-0.4-1-1s0.4-1,1-1s1,0.4,1,1S10.6,16,10,16z" data-icon-path="inner-path" opacity="0"></path>
</svg>
"""
        return self.format(template, values)


    def render_tmpl_close(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<button data-notification-btn class="bx--{mode}-notification__close-button"
    type="button" aria-label="{txt_close}">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--{mode}-notification__close-icon" width="20" height="20"
      viewBox="0 0 32 32" aria-hidden="true">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</button>
"""
        return self.format(template, values)


class NotificationButton(Node):
    """Notification button component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} tabindex="0"
    class="bx--inline-notification__action-button bx--btn bx--btn--sm bx--btn--ghost {class}"
    {props}>
  {child}
</{astag}>
"""
        return self.format(template, values)


class NotificationTitle(Node):
    """Notification title component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'h3'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        values['mode'] = context.get('mode', 'inline')
        template = """
<{astag} class="bx--{mode}-notification__title {class}" {props}>{child}</{astag}>
"""
        return self.format(template, values)


class NotificationSubtitle(Node):
    """Notification subtitle component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'p'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        values['mode'] = context.get('mode', 'inline')
        template = """
<{astag} class="bx--{mode}-notification__subtitle {class}" {props}>{child}</{astag}>
"""
        return self.format(template, values)


class NotificationCaption(Node):
    """Notification caption component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'p'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        values['mode'] = context.get('mode', 'inline')
        template = """
<{astag} class="bx--{mode}-notification__caption {class}" {props}>{child}</{astag}>
"""
        return self.format(template, values)


components = {
    'Notification': Notification,
    'NotificationButton': NotificationButton,
    'NotificationTitle': NotificationTitle,
    'NotificationSubtitle': NotificationSubtitle,
    'NotificationCaption': NotificationCaption,
}
