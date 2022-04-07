"""
Modal
=====

See: https://www.carbondesignsystem.com/components/modal/usage/

Modals focus the user’s attention exclusively on one task or piece of
information via a window that sits on top of the page content.

Overview
--------

Modals are a variant of dialog used to present critical information or request
user input needed to complete a user’s workflow. Modals interrupt a user’s
workflow by design. When active, a user is blocked from the on-page content
and cannot return to their previous workflow until the modal task is completed
or the user dismisses the modal. While effective when used correctly, modals
should be used sparingly to limit disruption to the user.

Modal dialogs are commonly used for short and non-frequent tasks, such as
editing or management tasks. If a user needs to repeatably preform a task,
consider making the task do-able from the main page.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node
from .button import Button

class Modal(Node):
    """Modal component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('label', 'heading', 'footer')
    "Named children."
    NODE_PROPS = ('id', 'variant', 'has_form', 'size', 'can_scroll')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('container', 'content', 'close')
    "Prepare xxx_class and xxx_props values."
    POSSIBLE_VARIANT = ('danger',)
    "Documentation only."
    POSSIBLE_SIZE = ('xs', 'sm', 'lg')
    "Documentation only."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_close'] = _("close modal")

        variant = self.eval(self.kwargs.get('variant'), context)
        if variant:
            values['class'].append(f'bx--modal--{variant}')

        id_ = values['id']
        if 'label' in self.slots:
            values['props'].append(('aria-labelledby', f'label-{id_}'))
        if 'heading' in self.slots:
            values['props'].append(('aria-describedby', f'heading-{id_}'))

        has_form = self.eval(self.kwargs.get('has_form'), context)
        if has_form:
            values['content_class'].append('bx--modal-content--with-form')

        size = self.eval(self.kwargs.get('size'), context)
        if size:
            values['container_class'].append(f'bx--modal-container--{size}')

        if not has_form and 'footer' not in self.slots:
            values['close_props'].append(('data-modal-primary-focus', True))

        if self.eval(self.kwargs.get('can_scroll'), context):
            values['content_props'].append(('tabindex', '0'))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-modal id="{id}" class="bx--modal {class}" role="dialog"
    aria-modal="true" tabindex="-1" {props}>
  <div class="bx--modal-container {container_class}" {container_props}>
    <div class="bx--modal-header">
      {slot_label}
      {slot_heading}
      <button class="bx--modal-close {close_class}" type="button" data-modal-close
          aria-label="{txt_close}" {close_props}>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content {content_class}" {content_props}>
      {child}
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    {slot_footer}
  </div>
  <span tabindex="0"></span>
</div>
"""
        return self.format(template, values, context)


    def render_slot_label(self, values, context):
        """Render html of the slot.
        """
        template = """
<p class="bx--modal-header__label bx--type-delta {class}" id="label-{id}"
    {props}>
  {child}
</p>
"""
        return self.format(template, values)


    def render_slot_heading(self, values, context):
        """Render html of the slot.
        """
        template = """
<p class="bx--modal-header__heading bx--type-beta {class}" id="heading-{id}"
    {props}>
  {child}
</p>
"""
        return self.format(template, values)


    def render_slot_footer(self, values, context):
        """Render html of the slot.
        """
        template = '<div class="bx--modal-footer {class}" {props}>{child}</div>'
        return self.format(template, values)


class ModalTrigger(Button):
    """Modal trigger button.
    """
    NODE_PROPS = ('target', *Button.NODE_PROPS)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        super().prepare(values, context)

        target = self.eval(self.kwargs['target'], context)
        values['props'].append(('data-modal-target', f'#{target}'))


    def after_prepare(self, values, context):
        """Simplifying values meant for rendering templates.
        """
        super().after_prepare(values, context)

        if not values['child']:
            values['child'] = _("Show modal")


components = {
    'Modal': Modal,
    'ModalTrigger': ModalTrigger,
}
