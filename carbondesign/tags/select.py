"""Implements Carbon Design Component: Select
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class Select(FormNode):
    """Select component.
    """
    MODES = ('default', 'inline')
    "Available variants."
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."
    TEMPLATES = ('items', *FormNode.TEMPLATES)
    "Conditional templates."
    RENDER_ELEMENT = False
    "Render the form field widget."

    required = False

    def prepare(self, values, context):
        values['txt_choose'] = _("Choose an option")

        values['props'].append(('id', values['id']))
        values['props'].append(('name', self.bound_field.name))

        self.required = self.bound_field.field.required and\
                self.bound_field.form.use_required_attribute
        if self.required:
            values['props'].append(('required', ''))

        if self.bound_field.field.disabled:
            values['props'].append(('disabled', ''))
            values['label_class'].append('bx--label--disabled')
            values['wrapper_class'].append('bx--select--disabled')

        if self.eval(self.kwargs.get('light'), context):
            values['wrapper_class'].append('bx--select--light')


    def render_default(self, values, context):
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div class="bx--select bx--select--invalid {wrapper_class}">
    <label for="{id}" class="bx--label {label_class}">
      {label}
    </label>
    <div class="bx--select-input__wrapper">
      <select class="bx--select-input {class}" {props}>
        {tmpl_items}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__invalid-icon" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2 c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
        <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
      </svg>
    </div>
    <div class="bx--form-requirement">
      {form_errors}
    </div>
    {tmpl_help}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--select {wrapper_class}">
    <label for="{id}" class="bx--label {label_class}">
      {label}
    </label>
    <div class="bx--select-input__wrapper">
      <select class="bx--select-input {class}" {props}>
        {tmpl_items}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_inline(self, values, context):
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid {wrapper_class}">
    <label for="{id}" class="bx--label {label_class}">
      {label}
    </label>
    <div class="bx--select-input--inline__wrapper">
      <select class="bx--select-input {class}" {props}>
        {tmpl_items}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__invalid-icon" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2 c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
        <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
      </svg>
    </div>
    <div class="bx--form-requirement">
      {form_errors}
    </div>
    {tmpl_help}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline {wrapper_class}">
    <label for="{id}" class="bx--label {label_class}">
      {label}
    </label>
    <div class="bx--select-input--inline__wrapper">
      <select class="bx--select-input {class}" {props}>
        {tmpl_items}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_items(self, values, context):
        group_begin_tmpl = """
<optgroup class="bx--select-optgroup" label="{label}">
"""
        group_end_tmpl = '</optgroup>'
        item_tmpl = """
<option class="bx--select-option" value="{value}" {props}>
  {child}
</option>
"""
        values = self.bound_field.value()

        items = []
        if not self.required:
            items.append(item_tmpl, {
                'value': '',
                'child': values['txt_choose'],
            })

        current_group = None
        for group, value, label in self.choices(context):
            if group != current_group:
                if current_group:
                    items.append(group_end_tmpl)
                current_group = group
                items.append(group_begin_tmpl.format(label=group))

            options = {'value': value, 'child': label}
            props = []
            if value in values:
                props.append('selected')
            options['props'] = ' '.join(props)
            items.append(self.format(item_tmpl, options))
        if current_group:
            items.append(group_end_tmpl)

        return '\n'.join(items)


components = {
    'Select': Select,
}
