"""
Time Picker
===========

See: https://the-carbon-components.netlify.app/?nav=time-picker

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines
from itertools import chain
#-
from .base import FormNode

class BaseSelectFormNode(FormNode):
    """Base form for select form
    """
    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        required = self.bound_field.field.required and\
                self.bound_field.form.use_required_attribute
        if required:
            values['props'].append(('required', True))

        values['label_class'].append('bx--visually-hidden')
        values['props'].append(('name', self.bound_field.name))


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
        item_tmpl = """
<option class="bx--select-option" value="{value}" {props}>{child}</option>
"""
        items = []
        for _, value, label in self.choices():
            options = {'value': value, 'child': label}
            props = []
            if self.bound_value and value in self.bound_value:
                props.append('selected')
            options['props'] = ' '.join(props)
            items.append(self.format(item_tmpl, options))

        return '\n'.join(items)


class AmPmPicker(BaseSelectFormNode):
    """AM/PM Picker component

    To be used within TimePicker
    """
    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--time-picker__select bx--select bx--select--invalid {class}"
    data-invalid>
  {tmpl_label}
  <select id="{id}" class="bx--select-input" {props}>
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
"""
        else:
            template = """
<div class="bx--time-picker__select bx--select {class}">
  {tmpl_label}
  <select id="{id}" class="bx--select-input" {props}>
    {tmpl_items}
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


class TimezonePicker(BaseSelectFormNode):
    """Timezone Picker component

    To be used within TimePicker
    """
    def render_default(self, values, context):
        """Default html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--time-picker__select bx--select bx--select--invalid {class}"
    data-invalid>
  {tmpl_label}
  <select id="{id}" class="bx--select-input" {props}>
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
"""
        else:
            template = """
<div class="bx--time-picker__select bx--select {class}">
  {tmpl_label}
  <select id="{id}" class="bx--select-input" {props}>
    {tmpl_items}
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


class TimePicker(FormNode):
    """Time Picker component.

    The props ampm and tzinfo must be Django form fields
    """
    NODE_PROPS = ('light', 'ampm', 'tzinfo')
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        child_class = []
        child_props = {}

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            child_props['disabled'] = True

        if self.eval(self.kwargs.get('light'), context):
            values['class'].append('bx--time-picker--light')
            child_class.append('bx--select--light')

        if child_class:
            child_props['class'] = ' '.join(child_class)

        # This is apparently needed
        self.nodelist.clear()

        ampm = self.eval(self.kwargs.get('ampm'), context)
        if ampm:
            self.nodelist.append(AmPmPicker(ampm, **child_props))

        tzinfo = self.eval(self.kwargs.get('tzinfo'), context)
        if tzinfo:
            self.nodelist.append(TimezonePicker(tzinfo, **child_props))


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('bx--text-input')
        props['class'].append('bx--time-picker__input-field')
        props['pattern'] = r'(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?'
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
    {child}
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
    {child}
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
    {child}
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
    {child}
  </div>
  {tmpl_help}
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_errors(self, values, context):
        """Dynamically render a part of the component's template.
        """
        tmpl_t = '<div class="bx--form-requirement__title">{title}.</div>'
        tmpl_s = '<p class="bx--form-requirement__supplement">{supplement}</p>'

        error_list = [self.bound_field.errors]
        ampm = self.eval(self.kwargs.get('ampm'), context)
        if ampm and ampm.errors:
            error_list.append(ampm.errors)
        tzinfo = self.eval(self.kwargs.get('tzinfo'), context)
        if tzinfo and tzinfo.errors:
            error_list.append(tzinfo.errors)

        items = []
        for error in chain(*error_list):
            title, supplement = error.split('.', 1)
            supplement = supplement.strip()
            items.append(tmpl_t.format(title=title))
            if supplement:
                items.append(tmpl_s.format(supplement=supplement.strip()))
        return '\n'.join(items)


components = {
    'TimePicker': TimePicker,
}
