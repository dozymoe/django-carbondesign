"""Implements Carbon Design Component: Time Picker
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
import pytz
#-
from .base import FormNode

class TimePicker(FormNode):
    """Time Picker component.
    """
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        values['txt_select_ampm'] = _("Select AM/PM")
        values['txt_select_zone'] = _("Select time zone")

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['props'].append(('disabled', ''))
            values['select_props'] = 'disabled'
        else:
            values['select_props'] = ''

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--time-picker--light')
            values['select_class'] = 'bx--select--light'
        else:
            values['select_class'] = ''


    def prepare_element_props(self, props, default, context):
        props['class'].append('bx--text-input')
        props['class'].append('bx--time-picker__input-field')
        props['pattern'] = r'(1[012]|[1-9]):[0-5][0-9](\\s)?'
        props['placeholder'] = 'hh:mm'
        props['maxlength'] = "5"

        if self.eval(self.kwargs.get('light'), context):
            props['class'].append('bx--text-input--light')


    def render_default(self, values, context):
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  <div class="bx--time-picker {class}" data-invalid>
    <div class="bx--time-picker__input">{element}</div>
    {tmpl_select_ampm}
    {tmpl_select_zone}
  </div>
  <div class="bx--form-requirement">
    {form_errors}
  </div>
  {tmpl_help}
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <label for="{id}" class="bx--label {label_class}" {label_props}>
    {label}
  </label>
  <div class="bx--time-picker {class}">
    <div class="bx--time-picker__input">{element}</div>
    {tmpl_select_ampm}
    {tmpl_select_zone}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_select_ampm(self, values, context):
        template = """
<div class="bx--time-picker__select bx--select {select_class}">
  <label for="select-ampm-{id}" class="bx--label bx--visually-hidden">
    {txt_select_ampm}
  </label>
  <select id="select-ampm-{id}" class="bx--select-input" {select_props}>
    <option class="bx--select-option" value="AM">AM</option>
    <option class="bx--select-option" value="PM">PM</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
"""
        return self.format(template, values)


    def render_tmpl_select_zone(self, values, context):
        template = """
<div class="bx--time-picker__select bx--select {select_class}">
  <label for="select-zone-{id}" class="bx--label bx--visually-hidden">
    {txt_select_zone}
  </label>
  <select id="select-zone-{id}" class="bx--select-input" {select_props}>
    {tmpl_timezones}
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_timezones(self, values, context):
        template = """
<option class="bx--select-option" value="{value}">{label}</option>
"""
        items = []
        for zone in pytz.common_timezones:
            items.append(template.format(value=zone, label=zone))
        return '\n'.join(items)


components = {
    'TimePicker': TimePicker,
}