"""
Select
======

See: https://www.carbondesignsystem.com/components/select/usage/

The select component allows users to choose one option from a list. It is used
in forms for users to submit data.

Overview
--------

Select is a type of input that is used in forms, where a user is submitting
data and chooses one option from a list.
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
    NODE_PROPS = ('light', 'with_empty')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'help', 'select')
    "Prepare xxx_class and xxx_props values."

    required = False

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_choose'] = _("Choose an option")

        values['props'].append(('id', values['id']))
        values['props'].append(('name', self.bound_field.name))

        self.required = self.bound_field.field.required and\
                self.bound_field.form.use_required_attribute
        if self.required:
            values['props'].append(('required', True))

        if self.eval(self.kwargs.get('disabled'), context):
            values['props'].append(('disabled', True))
            values['label_class'].append('bx--label--disabled')
            values['select_class'].append('bx--select--disabled')

        if self.eval(self.kwargs.get('light'), context):
            values['select_class'].append('bx--select--light')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div class="bx--select bx--select--invalid {select_class}" {select_props}>
    {tmpl_label}
    <div class="bx--select-input__wrapper" data-invalid>
      <select class="bx--select-input {class}" {props}>
        {tmpl_items}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
      {tmpl_icon_error}
    </div>
    <div class="bx--form-requirement">
      {tmpl_errors}
    </div>
    {tmpl_help}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--select {select_class}" {select_props}>
    {tmpl_label}
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
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid {select_class}"
      {select_props}>
    {tmpl_label}
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" data-invalid>
        <select class="bx--select-input {class}" {props}>
          {tmpl_items}
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
        {tmpl_icon_error}
      </div>
      <div class="bx--form-requirement">
        {tmpl_errors}
      </div>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline {select_class}" {select_props}>
    {tmpl_label}
    <div class="bx--select-input--inline__wrapper">
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
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_icon_error(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.eval(self.kwargs.get('disabled'), context):
            return ''
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--select__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
"""


    def render_tmpl_items(self, values, context):
        """Dynamically render a part of the component's template.
        """
        group_begin_tmpl = """
<optgroup class="bx--select-optgroup" label="{label}">
"""
        group_end_tmpl = '</optgroup>'
        item_tmpl = """
<option class="bx--select-option" value="{value}" {props}>{child}</option>
"""
        items = []
        if self.eval(self.kwargs.get('with_empty', True), context):
            items.append(item_tmpl.format(value='', child=values['txt_choose'],
                    props=''))

        current_group = None
        for group, value, label in self.choices():
            if group != current_group:
                if current_group:
                    items.append(group_end_tmpl)
                current_group = group
                items.append(group_begin_tmpl.format(label=group))

            options = {'value': value, 'child': label}
            props = []
            if self.bound_value and value in self.bound_value:
                props.append('selected')
            options['props'] = ' '.join(props)
            items.append(self.format(item_tmpl, options))
        if current_group:
            items.append(group_end_tmpl)

        return '\n'.join(items)


components = {
    'Select': Select,
}
