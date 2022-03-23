# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class DatePickerHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_basic_short(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_empty mode="basic" short=True label="Date Picker label" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--date-picker bx--date-picker--simple bx--date-picker--short">
    <div class="bx--date-picker-container">
<label for="id_started_at_empty" class="bx--label">
  Date Picker label
</label>
      <input type="text" name="started_at_empty" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{4,4}" placeholder="mm/yyyy" id="id_started_at_empty">
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_basic_invalid(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_missing mode="basic" label="Date Picker label" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--date-picker bx--date-picker--simple">
    <div class="bx--date-picker-container">
<label for="id_started_at_missing" class="bx--label">
  Date Picker label
</label>
      <input type="text" name="started_at_missing" value="" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-invalid="" required id="id_started_at_missing">
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">This field is required.</div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_basic_short_light(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_empty mode="basic" short=True label="Date Picker label" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--date-picker bx--date-picker--simple bx--date-picker--light bx--date-picker--short">
    <div class="bx--date-picker-container">
<label for="id_started_at_empty" class="bx--label">
  Date Picker label
</label>
      <input type="text" name="started_at_empty" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{4,4}" placeholder="mm/yyyy" id="id_started_at_empty">
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_basic_invalid_light(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_missing mode="basic" label="Date Picker label" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div class="bx--date-picker bx--date-picker--simple bx--date-picker--light">
    <div class="bx--date-picker-container">
<label for="id_started_at_missing" class="bx--label">
  Date Picker label
</label>
      <input type="text" name="started_at_missing" value="" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-invalid="" required id="id_started_at_missing">
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">This field is required.</div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_range(self):
        template = """
{% load carbondesign %}
{% RangeDatePicker form.started_at form.stopped_at %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="range"
      class="bx--date-picker bx--date-picker--range">
    <div class="bx--date-picker-container">
      <label for="id_started_at" class="bx--label">
        Started at
      </label>
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at" value="2022-02-03 01:02:03" class="bx--date-picker__input" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-date-picker-input-from="" required id="id_started_at">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
    </div>
    <div class="bx--date-picker-container">
      <label for="id_stopped_at" class="bx--label">
        Stopped at
      </label>
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="stopped_at" value="2022-10-04 11:30:40" class="bx--date-picker__input" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-date-picker-input-to="" required id="id_stopped_at">
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
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_range_light(self):
        template = """
{% load carbondesign %}
{% RangeDatePicker form.started_at form.stopped_at light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="range"
      class="bx--date-picker bx--date-picker--range bx--date-picker--light">
    <div class="bx--date-picker-container">
      <label for="id_started_at" class="bx--label">
        Started at
      </label>
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at" value="2022-02-03 01:02:03" class="bx--date-picker__input" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-date-picker-input-from="" required id="id_started_at">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
    </div>
    <div class="bx--date-picker-container">
      <label for="id_stopped_at" class="bx--label">
        Stopped at
      </label>
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="stopped_at" value="2022-10-04 11:30:40" class="bx--date-picker__input" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-date-picker-input-to="" required id="id_stopped_at">
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
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nolabel_light(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_empty mode="nolabel" label="Date Picker label" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--nolabel bx--date-picker--light">
    <div class="bx--date-picker-container">
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at_empty" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" id="id_started_at_empty">
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
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nolabel_invalid_light(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_missing mode="nolabel" label="Date Picker label" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--nolabel bx--date-picker--light">
    <div class="bx--date-picker-container">
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at_missing" value="" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-invalid="" required id="id_started_at_missing">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">This field is required.</div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_single_light(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_empty label="Date Picker label" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--light">
    <div class="bx--date-picker-container">
<label for="id_started_at_empty" class="bx--label">
  Date Picker label
</label>
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at_empty" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" id="id_started_at_empty">
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
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_single_invalid_light(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_missing label="Date Picker label" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--light">
    <div class="bx--date-picker-container">
<label for="id_started_at_missing" class="bx--label">
  Date Picker label
</label>
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at_missing" value="" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-invalid="" required id="id_started_at_missing">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">This field is required.</div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nolabel(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_empty mode="nolabel" label="Date Picker label" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--nolabel">
    <div class="bx--date-picker-container">
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at_empty" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" id="id_started_at_empty">
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
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nolabel_invalid(self):
        template = """
{% load carbondesign %}
{% DatePicker form.started_at_missing mode="nolabel" label="Date Picker label" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-date-picker data-date-picker-type="single"
      class="bx--date-picker bx--date-picker--single bx--date-picker--nolabel">
    <div class="bx--date-picker-container">
      <div class="bx--date-picker-input__wrapper">
        <input type="text" name="started_at_missing" value="" class="bx--date-picker__input" data-date-picker-input="" pattern="\d{1,2}/\d{1,2}/\d{4,4}" placeholder="mm/dd/yyyy" data-invalid="" required id="id_started_at_missing">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            data-date-picker-icon="true" class="bx--date-picker__icon"
            width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
          <path d="M26,4h-4V2h-2v2h-8V2h-2v2H6C4.9,4,4,4.9,4,6v20c0,1.1,0.9,2,2,2h20c1.1,0,2-0.9,2-2V6C28,4.9,27.1,4,26,4z M26,26H6V12h20  V26z M26,10H6V6h4v2h2V6h8v2h2V6h4V10z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">This field is required.</div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
