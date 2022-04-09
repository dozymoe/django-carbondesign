# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TimePickerHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm zones=timezones label="Select a time" id="time-picker-1" %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-1" class="bx--label">
  Select a time
</label>
  <div class="bx--time-picker">
    <div class="bx--time-picker__input"><input type="text" name="time_tm" id="time-picker-1" class="bx--text-input bx--time-picker__input-field" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5"></div>
<div class="bx--time-picker__select bx--select">
  <label for="select-ampm-time-picker-1" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-1" class="bx--select-input">
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
<div class="bx--time-picker__select bx--select">
  <label for="select-zone-time-picker-1" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-1" class="bx--select-input">
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_invalid(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing zones=timezones label="Select a time" id="time-picker-2" %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-2" class="bx--label">
  Select a time
</label>
  <div class="bx--time-picker" data-invalid>
    <div class="bx--time-picker__input"><input type="text" name="time_tm_missing" id="time-picker-2" class="bx--text-input bx--time-picker__input-field" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5" required></div>
<div class="bx--time-picker__select bx--select">
  <label for="select-ampm-time-picker-2" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-2" class="bx--select-input">
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
<div class="bx--time-picker__select bx--select">
  <label for="select-zone-time-picker-2" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-2" class="bx--select-input">
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_disabled(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm zones=timezones label="Select a time" id="time-picker-3" disabled=True %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-3" class="bx--label bx--label--disabled">
  Select a time
</label>
  <div class="bx--time-picker">
    <div class="bx--time-picker__input"><input type="text" name="time_tm" id="time-picker-3" disabled class="bx--text-input bx--time-picker__input-field" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5"></div>
<div class="bx--time-picker__select bx--select">
  <label for="select-ampm-time-picker-3" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-3" class="bx--select-input" disabled>
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
<div class="bx--time-picker__select bx--select">
  <label for="select-zone-time-picker-3" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-3" class="bx--select-input" disabled>
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_invalid_disabled(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing zones=timezones label="Select a time" id="time-picker-4" disabled=True %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-4" class="bx--label bx--label--disabled">
  Select a time
</label>
  <div class="bx--time-picker" data-invalid>
    <div class="bx--time-picker__input"><input type="text" name="time_tm_missing" id="time-picker-4" disabled class="bx--text-input bx--time-picker__input-field" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5" required></div>
<div class="bx--time-picker__select bx--select">
  <label for="select-ampm-time-picker-4" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-4" class="bx--select-input" disabled>
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
<div class="bx--time-picker__select bx--select">
  <label for="select-zone-time-picker-4" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-4" class="bx--select-input" disabled>
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_light(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm zones=timezones label="Select a time" id="time-picker-5" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-5" class="bx--label">
  Select a time
</label>
  <div class="bx--time-picker bx--time-picker--light">
    <div class="bx--time-picker__input"><input type="text" name="time_tm" id="time-picker-5" class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5"></div>
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-ampm-time-picker-5" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-5" class="bx--select-input">
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
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-zone-time-picker-5" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-5" class="bx--select-input">
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_light_invalid(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing zones=timezones label="Select a time" id="time-picker-6" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--time-picker bx--time-picker--light" data-invalid>
    <div class="bx--time-picker__input">
<label for="time-picker-6" class="bx--label">
  Select a time
</label>
      <input type="text" name="time_tm_missing" id="time-picker-6" class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5" required>
    </div>
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-ampm-time-picker-6" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-6" class="bx--select-input">
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
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-zone-time-picker-6" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-6" class="bx--select-input">
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_light_disabled(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm zones=timezones label="Select a time" id="time-picker-7" disabled=True light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--time-picker bx--time-picker--light">
    <div class="bx--time-picker__input">
<label for="time-picker-7" class="bx--label bx--label--disabled">
  Select a time
</label>
      <input type="text" name="time_tm" id="time-picker-7" disabled class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5">
    </div>
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-ampm-time-picker-7" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-7" class="bx--select-input" disabled>
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
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-zone-time-picker-7" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-7" class="bx--select-input" disabled>
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_light_invalid_disabled(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing zones=timezones label="Select a time" id="time-picker-8" disabled=True light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--time-picker bx--time-picker--light" data-invalid>
    <div class="bx--time-picker__input">
<label for="time-picker-8" class="bx--label bx--label--disabled">
  Select a time
</label>
      <input type="text" name="time_tm_missing" id="time-picker-8" disabled class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(1[012]|[1-9]):[0-5][0-9](\\s)?" placeholder="hh:mm" maxlength="5" required>
    </div>
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-ampm-time-picker-8" class="bx--label bx--visually-hidden">
    Select AM/PM
  </label>
  <select id="select-ampm-time-picker-8" class="bx--select-input" disabled>
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
<div class="bx--time-picker__select bx--select bx--select--light">
  <label for="select-zone-time-picker-8" class="bx--label bx--visually-hidden">
    Select time zone
  </label>
  <select id="select-zone-time-picker-8" class="bx--select-input" disabled>
<option class="bx--select-option" value="option-1">Time zone 1</option>
<option class="bx--select-option" value="option-2">Time zone 2</option>
<option class="bx--select-option" value="option-3">Time zone 3</option>
  </select>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
