# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TimePickerTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TimePicker form.started_at %}
"""
        expected = r"""
<div class="bx--form-item">
<label for="id_started_at" class="bx--label">
  Started at
</label>
  <div class="bx--time-picker">
    <div class="bx--time-picker__input"><input type="text" name="started_at" value="2022-02-03 01:02:03" class="bx--text-input bx--time-picker__input-field" pattern="(2[0-3]|1[0-9]|0?[0-9]):([1-5][0-9]|0?[0-9])(\\s)?" placeholder="hh:mm" maxlength="5" required id="id_started_at"></div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
