"""Implements Carbon Design Component: Date Picker
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import FormNode, FormNodes

class DatePicker(FormNode):
    """Date Picker component.
    """
    MODES = ('default', 'basic', 'nolabel')
    "Available variants."
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        if self.eval(self.kwargs.get('light'), context):
            values['wrapper_class'].append('bx--date-picker--light')


    def prepare_element_props(self, props, default, context):
        props['class'].append('bx--date-picker__input')
        props['data-date-picker-input'] = ''
        props['pattern'] = r'\d{1,2}/\d{1,2}/\d{4}'
        props['placeholder'] = 'mm/dd/yyyy'

        if self.bound_field.errors:
            props['data-invalid'] = ''


    def render_default(self, values, context):
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single {wrapper_class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <label for="{id}" class="bx--label {label_class}" {label_props}>
        {label}
      </label>
      <div class="bx--date-picker-input__wrapper">
        {element}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        {form_errors}
      </div>
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single {wrapper_class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <label for="{id}" class="bx--label {label_class}" {label_props}>
        {label}
      </label>
      <div class="bx--date-picker-input__wrapper">
        {element}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
    </div>
  </div>
</div>
"""
        return self.format(template, values)


    def render_nolabel(self, values, context):
        """ Basic with calendar but without label.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--nolabel {wrapper_class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <div class="bx--date-picker-input__wrapper">
        {element}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        {form_errors}
      </div>
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--nolabel {wrapper_class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <div class="bx--date-picker-input__wrapper">
        {element}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
    </div>
  </div>
</div>
"""
        return self.format(template, values)


    def render_basic(self, values, context):
        """ Basic without calendar (mm/yy only).
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div class="bx--date-picker bx--date-picker--simple {wrapper_class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <label for="{id}" class="bx--label {label_class}" {label_props}>
        {label}
      </label>
      {element}
      <div class="bx--form-requirement">
        {form_errors}
      </div>
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--date-picker bx--date-picker--simple bx--date-picker--short {wrapper_class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <label for="{id}" class="bx--label {label_class}" {label_props}>
        {label}
      </label>
      {element}
    </div>
  </div>
</div>
"""
        return self.format(template, values)


class RangeDatePicker(FormNodes):
    """Date Picker component with range inputs.
    """
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        if self.eval(self.kwargs.get('light'), context):
            values['wrapper_class'].append('bx--date-picker--light')


    def prepare_element_props(self, field, props, default, context):
        index = self.bound_fields.index(field)

        props['class'].append('bx--date-picker__input')
        props['pattern'] = r'\d{1,2}/\d{1,2}/\d{4}'
        props['placeholder'] = 'mm/dd/yyyy'
        if index:
            props['data-date-picker-input-to'] = ''
        else:
            props['data-date-picker-input-from'] = ''

        if field.errors:
            props['data-invalid'] = ''


    def render_default(self, values, context):
        has_errors = any(x.errors for x in self.bound_fields)
        if has_errors:
            template = """
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="range"
      class="bx--date-picker bx--date-picker--range {wrapper-class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <label for="{id_0}" class="bx--label {label_class}" {label_props}>
        {label_0}
      </label>
      <div class="bx--date-picker-input__wrapper">
        {element_0}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        {form_errors_0}
      </div>
    </div>
    <div class="bx--date-picker-container">
      <label for="{id_1}" class="bx--label {label_class}" {label_props}>
        {label_1}
      </label>
      <div class="bx--date-picker-input__wrapper">
        {element_1}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        {form_errors_1}
      </div>
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="range"
      class="bx--date-picker bx--date-picker--range {wrapper-class}"
      {wrapper_props}>

    <div class="bx--date-picker-container">
      <label for="{id_0}" class="bx--label {label_class}" {label_props}>
        {label_0}
      </label>
      <div class="bx--date-picker-input__wrapper">
        {element_0}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
    </div>
    <div class="bx--date-picker-container">
      <label for="{id_1}" class="bx--label {label_class}" {label_props}>
        {label_1}
      </label>
      <div class="bx--date-picker-input__wrapper">
        {element_1}
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
    </div>
  </div>
</div>
"""
        return self.format(template, values)


components = {
    'DatePicker': DatePicker,
    'RangeDatePicker': RangeDatePicker,
}
