"""
Time Picker
===========

See: https://the-carbon-components.netlify.app/?nav=time-picker

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
import pytz
#-
from .base import FormNode

class TimePicker(FormNode):
    """Time Picker component.
    """
    NODE_PROPS = ('light', 'zones')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'select')
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_select_ampm'] = _("Select AM/PM")
        values['txt_select_zone'] = _("Select time zone")

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['select_props'].append(('disabled', True))

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--time-picker--light')
            values['select_class'].append('bx--select--light')


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('bx--text-input')
        props['class'].append('bx--time-picker__input-field')
        props['pattern'] = r'(1[012]|[1-9]):[0-5][0-9](\\s)?'
        props['placeholder'] = 'hh:mm'
        props['maxlength'] = "5"

        if self.eval(self.kwargs.get('light'), context):
            props['class'].append('bx--text-input--light')


    def render_default(self, values, context):
        """Output html of the component.
        """
        light = self.eval(self.kwargs.get('light'), context)
        if self.bound_field.errors:
            if light:
                template = """
<div class="bx--form-item">
  <div class="bx--time-picker {class}" data-invalid>
    <div class="bx--time-picker__input">
      {tmpl_label}
      {tmpl_element}
    </div>
    {tmpl_select_ampm}
    {tmpl_select_zone}
  </div>
  <div class="bx--form-requirement">
    {tmpl_errors}
  </div>
  {tmpl_help}
</div>
"""
            else:
                template = """
<div class="bx--form-item">
  {tmpl_label}
  <div class="bx--time-picker {class}" data-invalid>
    <div class="bx--time-picker__input">{tmpl_element}</div>
    {tmpl_select_ampm}
    {tmpl_select_zone}
  </div>
  <div class="bx--form-requirement">
    {tmpl_errors}
  </div>
  {tmpl_help}
</div>
"""
        elif light and self.eval(self.kwargs.get('disabled'), context):
            template = """
<div class="bx--form-item">
  <div class="bx--time-picker {class}">
    <div class="bx--time-picker__input">
      {tmpl_label}
      {tmpl_element}
    </div>
    {tmpl_select_ampm}
    {tmpl_select_zone}
  </div>
  {tmpl_help}
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  {tmpl_label}
  <div class="bx--time-picker {class}">
    <div class="bx--time-picker__input">{tmpl_element}</div>
    {tmpl_select_ampm}
    {tmpl_select_zone}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_select_ampm(self, values, context):
        """Dynamically render a part of the component's template.
        """
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
        """Dynamically render a part of the component's template.
        """
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
        """Dynamically render a part of the component's template.
        """
        template = """
<option class="bx--select-option" value="{value}">{label}</option>
"""
        timezones = self.eval(self.kwargs.get('zones',
                pytz.common_timezones), context)
        items = []
        for zone in timezones:
            if isinstance(zone, str):
                value = label = zone
            else:
                value, label = zone
            items.append(template.format(value=value, label=label))
        return '\n'.join(items)


components = {
    'TimePicker': TimePicker,
}
