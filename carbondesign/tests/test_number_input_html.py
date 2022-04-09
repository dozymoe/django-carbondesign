# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long
from .base import compare_template, SimpleTestCase

class NumberInputHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number label="Number input label" min="0" max="100" %}
"""
        expected = """
<div class="bx--form-item">
  <div data-numberinput class="bx--number">
<label for="id_number" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number" value="24" min="0" max="100" class="" required id="id_number">
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_invalid(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid min="0" max="100" %}
"""
        expected = """
<div class="bx--form-item">
  <div data-invalid data-numberinput class="bx--number">
<label for="id_number_invalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_invalid" value="a" min="0" max="100" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--number__invalid" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_nolabel(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid nolabel=True min="0" max="100" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-invalid data-numberinput class="bx--number bx--number--nolabel">
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_invalid" value="a" min="0" max="100" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--number__invalid" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_help(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_help min="0" max="100" %}
"""
        expected = """
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--helpertext">
<label for="id_number_help" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_help" value="1" min="0" max="100" class="" aria-controls="hint-id_number_help" aria-describedby="hint-id_number_help" id="id_number_help">
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
<div id="hint-id_number_help" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_help_invalid(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_helpinvalid min="0" max="100" %}
"""
        expected = """
<div class="bx--form-item">
  <div data-invalid data-numberinput class="bx--number bx--number--helpertext">
<label for="id_number_helpinvalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_helpinvalid" value="a" min="0" max="100" class="" aria-controls="hint-id_number_helpinvalid" aria-describedby="hint-id_number_helpinvalid" role="alert" aria-atomic="true" id="id_number_helpinvalid">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--number__invalid" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
<div id="hint-id_number_helpinvalid" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number label="Number input label" min="0" max="100" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--light">
<label for="id_number" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number" value="24" min="0" max="100" class="" required id="id_number">
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_invalid_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid min="0" max="100" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div data-invalid data-numberinput class="bx--number bx--number--light">
<label for="id_number_invalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_invalid" value="a" min="0" max="100" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--number__invalid" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_nolabel_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid nolabel=True min="0" max="100" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div data-invalid data-numberinput class="bx--number bx--number--nolabel bx--number--light">
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_invalid" value="a" min="0" max="100" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--number__invalid" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_help_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_help min="0" max="100" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--light bx--number--helpertext">
<label for="id_number_help" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_help" value="1" min="0" max="100" class="" aria-controls="hint-id_number_help" aria-describedby="hint-id_number_help" id="id_number_help">
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
<div id="hint-id_number_help" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_help_invalid_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_helpinvalid min="0" max="100" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div data-invalid data-numberinput class="bx--number bx--number--light bx--number--helpertext">
<label for="id_number_helpinvalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
      <input type="number" name="number_helpinvalid" value="a" min="0" max="100" class="" aria-controls="hint-id_number_helpinvalid" aria-describedby="hint-id_number_helpinvalid" role="alert" aria-atomic="true" id="id_number_helpinvalid">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--number__invalid" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2    c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      <div class="bx--number__controls">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      </div>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
<div id="hint-id_number_helpinvalid" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number mode="mobile" label="Number input label" min="0" max="100" pattern="\\d*" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--mobile bx--number--light">
<label for="id_number" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number" value="24" min="0" max="100" pattern="\d*" class="" required id="id_number">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_invalid_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid mode="mobile" min="0" max="100" pattern="\\d*" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-invalid data-numberinput
      class="bx--number bx--number--mobile bx--number--light">
<label for="id_number_invalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_invalid" value="a" min="0" max="100" pattern="\d*" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_nolabel_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid mode="mobile" nolabel=True min="0" max="100" pattern="\\d*" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-invalid data-numberinput
      class="bx--number bx--number--mobile bx--number--nolabel bx--number--light">
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_invalid" value="a" min="0" max="100" pattern="\d*" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_help_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_help mode="mobile" min="0" max="100" pattern="\\d*" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--mobile bx--number--light bx--number--helpertext">
<label for="id_number_help" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_help" value="1" min="0" max="100" pattern="\d*" class="" aria-controls="hint-id_number_help" aria-describedby="hint-id_number_help" id="id_number_help">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
<div id="hint-id_number_help" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_help_invalid_light(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_helpinvalid mode="mobile" min="0" max="100" pattern="\\d*" light=True %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-invalid data-numberinput
      class="bx--number bx--number--mobile bx--number--light bx--number--helpertext">
<label for="id_number_helpinvalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_helpinvalid" value="a" min="0" max="100" pattern="\d*" class="" aria-controls="hint-id_number_helpinvalid" aria-describedby="hint-id_number_helpinvalid" role="alert" aria-atomic="true" id="id_number_helpinvalid">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
<div id="hint-id_number_helpinvalid" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number mode="mobile" label="Number input label" min="0" max="100" pattern="\\d*" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--mobile">
<label for="id_number" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number" value="24" min="0" max="100" pattern="\d*" class="" required id="id_number">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_invalid(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid mode="mobile" min="0" max="100" pattern="\\d*" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-invalid data-numberinput
      class="bx--number bx--number--mobile">
<label for="id_number_invalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_invalid" value="a" min="0" max="100" pattern="\d*" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_nolabel(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_invalid mode="mobile" nolabel=True min="0" max="100" pattern="\\d*" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-invalid data-numberinput
      class="bx--number bx--number--mobile bx--number--nolabel">
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_invalid" value="a" min="0" max="100" pattern="\d*" class="" role="alert" aria-atomic="true" id="id_number_invalid">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_help(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_help mode="mobile" min="0" max="100" pattern="\\d*" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-numberinput class="bx--number bx--number--mobile bx--number--helpertext">
<label for="id_number_help" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_help" value="1" min="0" max="100" pattern="\d*" class="" aria-controls="hint-id_number_help" aria-describedby="hint-id_number_help" id="id_number_help" >
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
<div id="hint-id_number_help" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_mobile_help_invalid(self):
        template = """
{% load carbondesign %}
{% NumberInput form.number_helpinvalid mode="mobile" min="0" max="100" pattern="\\d*" %}
"""
        expected = r"""
<div class="bx--form-item">
  <div data-invalid data-numberinput
      class="bx--number bx--number--mobile bx--number--helpertext">
<label for="id_number_helpinvalid" class="bx--label">
  Number input label
</label>
    <div class="bx--number__input-wrapper">
<button aria-label="decrease number input" class="bx--number__control-btn down-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M8 0L4 4 0 0z"></path>
  </svg>
</button>
      <input type="number" name="number_helpinvalid" value="a" min="0" max="100" pattern="\d*" class="" aria-controls="hint-id_number_helpinvalid" aria-describedby="hint-id_number_helpinvalid" role="alert" aria-atomic="true" id="id_number_helpinvalid">
<button aria-label="increase number input" class="bx--number__control-btn up-icon"
    type="button" aria-live="polite" aria-atomic="true">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="8"
      height="4" viewBox="0 0 8 4" aria-hidden="true">
    <path d="M0 4L4 0 8 4z"></path>
  </svg>
</button>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Enter a whole number.</div>
    </div>
<div id="hint-id_number_helpinvalid" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
