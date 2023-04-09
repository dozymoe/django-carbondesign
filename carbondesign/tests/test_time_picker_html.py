# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TimePickerHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm label="Select a time" id="time-picker-1" %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-1" class="bx--label">
  Select a time
</label>
  <div class="bx--time-picker">
    <div class="bx--time-picker__input"><input type="text" name="time_tm" id="time-picker-1" class="bx--text-input bx--time-picker__input-field" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5"></div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_invalid(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing label="Select a time" id="time-picker-2" %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-2" class="bx--label">
  Select a time
</label>
  <div class="bx--time-picker" data-invalid>
    <div class="bx--time-picker__input"><input type="text" name="time_tm_missing" id="time-picker-2" class="bx--text-input bx--time-picker__input-field" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5" required></div>
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
{% TimePicker form.time_tm label="Select a time" id="time-picker-3" disabled=True %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-3" class="bx--label bx--label--disabled">
  Select a time
</label>
  <div class="bx--time-picker">
    <div class="bx--time-picker__input"><input type="text" name="time_tm" id="time-picker-3" disabled class="bx--text-input bx--time-picker__input-field" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5"></div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_invalid_disabled(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing label="Select a time" id="time-picker-4" disabled=True %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-4" class="bx--label bx--label--disabled">
  Select a time
</label>
  <div class="bx--time-picker" data-invalid>
    <div class="bx--time-picker__input"><input type="text" name="time_tm_missing" id="time-picker-4" disabled class="bx--text-input bx--time-picker__input-field" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5" required></div>
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
{% TimePicker form.time_tm label="Select a time" id="time-picker-5" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="time-picker-5" class="bx--label">
  Select a time
</label>
  <div class="bx--time-picker bx--time-picker--light">
    <div class="bx--time-picker__input"><input type="text" name="time_tm" id="time-picker-5" class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5"></div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_light_invalid(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing label="Select a time" id="time-picker-6" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--time-picker bx--time-picker--light" data-invalid>
    <div class="bx--time-picker__input">
<label for="time-picker-6" class="bx--label">
  Select a time
</label>
      <input type="text" name="time_tm_missing" id="time-picker-6" class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5" required>
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
{% TimePicker form.time_tm label="Select a time" id="time-picker-7" disabled=True light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--time-picker bx--time-picker--light">
    <div class="bx--time-picker__input">
<label for="time-picker-7" class="bx--label bx--label--disabled">
  Select a time
</label>
      <input type="text" name="time_tm" id="time-picker-7" disabled class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5">
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_light_invalid_disabled(self):
        template = """
{% load carbondesign %}
{% TimePicker form.time_tm_missing label="Select a time" id="time-picker-8" disabled=True light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--time-picker bx--time-picker--light" data-invalid>
    <div class="bx--time-picker__input">
<label for="time-picker-8" class="bx--label bx--label--disabled">
  Select a time
</label>
      <input type="text" name="time_tm_missing" id="time-picker-8" disabled class="bx--text-input bx--time-picker__input-field bx--text-input--light" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5" required>
    </div>
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
