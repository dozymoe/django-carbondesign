"""Implements Carbon Design Component: Modal
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

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_close'] = _("close modal")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-modal id="{id}" class="bx--modal {class}" role="dialog"
    aria-modal="true" aria-labelledby="{id}-label"
    aria-describedby="{id}-heading" tabindex="-1" {props}>
  <div class="bx--modal-container">
    <div class="bx--modal-header">
      {slot_label}
      {slot_heading}
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="{txt_close}">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 16 16" aria-hidden="true">
          <path d="M12 4.7L11.3 4 8 7.3 4.7 4 4 4.7 7.3 8 4 11.3 4.7 12 8 8.7 11.3 12 12 11.3 8.7 8z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" tabindex="0">
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
<p class="bx--modal-header__label bx--type-delta {class}" id="{id}-label"
    {props}>
  {child}
</p>
"""
        return self.format(template, values)


    def render_slot_heading(self, values, context):
        """Render html of the slot.
        """
        template = """
<p class="bx--modal-header__heading bx--type-beta {class}" id="{id}-heading"
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
