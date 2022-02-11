"""Implements Carbon Design Component: Text input
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class TextInput(FormNode):
    """Text Input component.
    """
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['help_class'].append('bx--form__helper-text--disabled')
            values['props'].append(('disabled', 'disabled'))


    def render_default(self, values, context, slots):
        if self.bound_field.errors:
            template = """
<div class="bx--form-item bx--text-input-wrapper">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  {slot_help}
  <div class="bx--text-input__field-wrapper" data-invalid>
    {slot_icon}
    {element}
  </div>
  <div class="bx--form-requirement">
    {form_errors}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item bx--text-input-wrapper">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  {slot_help}
  <div class="bx--text-input__field-wrapper">
    {element}
  </div>
</div>
"""
        return self.format(template, values, slots)


    def render_slot_icon(self, values, context):
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
    class="bx--text-input__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z">
  </path><path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
"""


    def prepare_element_attributes(self, attrs, default, context):
        attrs['class'].append('bx--text-input')

        if self.eval(self.kwargs.get('light'), context):
            attrs['class'].append('bx--text-input--light')

        if self.bound_field.errors:
            attrs['class'].append('bx--text-input--invalid')


class PasswordInput(FormNode):
    """Password Input component.
    """
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        values['txt_show_password'] = _("Show password")

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['help_class'].append('bx--form__helper-text--disabled')
            values['props'].append(('disabled', 'disabled'))


    def render_default(self, values, context, slots):
        if self.bound_field.errors:
            template = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  {slot_help}}
  <div class="bx--text-input__field-wrapper" data-invalid>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
        class="bx--text-input__invalid-icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
      <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
    {element}
    <button type="button"
        class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
      <span class="bx--assistive-text">{txt_show_password}</span>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          hidden="true" class="bx--icon--visibility-off" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
        <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
      </svg>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          class="bx--icon--visibility-on" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5C13.4,10.5,10.6,12.5,8,12.5z"></path>
        <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
      </svg>
    </button>
  </div>
  <div class="bx--form-requirement">
    {form_errors}
  </div>
</div>
"""
        else:
            template = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  {slot_help}
  <div class="bx--text-input__field-wrapper">
    {element}
    <button type="button"
        class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
      <span class="bx--assistive-text">{txt_show_password}</span>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          hidden="true" class="bx--icon--visibility-off" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
        <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
      </svg>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          class="bx--icon--visibility-on" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5C13.4,10.5,10.6,12.5,8,12.5z"></path>
        <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        return self.format(template, values, slots)


    def prepare_element_attributes(self, attrs, default, context):
        attrs['class'].extend([
                'bx--text-input',
                'bx--password-input'])
        attrs['data-toggle-password-visibility'] = ''

        if self.eval(self.kwargs.get('light'), context):
            attrs['class'].append('bx--text-input--light')

        if self.bound_field.errors:
            attrs['class'].append('bx--text-input--invalid')


components = {
    'PasswordInput': PasswordInput,
    'TextInput': TextInput,
}
