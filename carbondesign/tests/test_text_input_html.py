# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long
from django import forms
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    text = forms.CharField(
            label="Text Input label",
            required=False)
    text_missing = forms.CharField(
            label="Text Input label",
            required=True)
    text_help = forms.CharField(
            label="Text Input label",
            required=False,
            help_text="Optional helper text goes here")
    text_help2 = forms.CharField(
            label="Text Input label",
            required=False,
            help_text="Optional helper text here; if message is more than one "
                "line text should wrap (~100 character count maximum)")


class TextInputHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text placeholder="Placeholder text" %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text" placeholder="Placeholder text" class="bx--text-input" id="id_text">
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_invalid(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_missing placeholder="Placeholder text" %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_missing" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper" data-invalid>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--text-input__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <input type="text" name="text_missing" placeholder="Placeholder text" class="bx--text-input bx--text-input--invalid" required id="id_text_missing">
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_help placeholder="Placeholder text" %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_help" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text_help" placeholder="Placeholder text" class="bx--text-input" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help2(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_help2 placeholder="Placeholder text" %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_help2" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text_help2" placeholder="Placeholder text" class="bx--text-input" aria-controls="hint-id_text_help2" aria-describedby="hint-id_text_help2" id="id_text_help2">
  </div>
<div id="hint-id_text_help2" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_disabled(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_help placeholder="Placeholder text" disabled=True %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_help" class="bx--label bx--label--disabled">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text_help" placeholder="Placeholder text" disabled class="bx--text-input" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text bx--form__helper-text--disabled">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text placeholder="Placeholder text" light=True %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text" placeholder="Placeholder text" class="bx--text-input bx--text-input--light" id="id_text">
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_invalid_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_missing placeholder="Placeholder text" light=True %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_missing" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper" data-invalid>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--text-input__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <input type="text" name="text_missing" placeholder="Placeholder text" class="bx--text-input bx--text-input--light bx--text-input--invalid" required id="id_text_missing">
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>

"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_help placeholder="Placeholder text" light=True %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_help" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text_help" placeholder="Placeholder text" class="bx--text-input bx--text-input--light" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text">
  Optional helper text goes here
</div>
</div>

"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help2_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_help2 placeholder="Placeholder text" light=True %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_help2" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text_help2" placeholder="Placeholder text" class="bx--text-input bx--text-input--light" aria-controls="hint-id_text_help2" aria-describedby="hint-id_text_help2" id="id_text_help2">
  </div>
<div id="hint-id_text_help2" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
</div>

"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_disabled_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextInput form.text_help placeholder="Placeholder text" disabled=True light=True %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_help" class="bx--label bx--label--disabled">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text_help" placeholder="Placeholder text" disabled class="bx--text-input bx--text-input--light" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text bx--form__helper-text--disabled">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)


class PasswordInputHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text placeholder="Placeholder text" %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text" placeholder="Placeholder text" class="bx--text-input bx--password-input" data-toggle-password-visibility="" id="id_text">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_invalid(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_missing placeholder="Placeholder text" %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_missing" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper" data-invalid>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--text-input__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <input type="password" name="text_missing" placeholder="Placeholder text" class="bx--text-input bx--text-input--invalid bx--password-input" data-toggle-password-visibility="" required id="id_text_missing">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_help placeholder="Placeholder text" %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_help" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text_help" placeholder="Placeholder text" class="bx--text-input bx--password-input" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" data-toggle-password-visibility="" id="id_text_help">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help2(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_help2 placeholder="Placeholder text" %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_help2" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text_help2" placeholder="Placeholder text" class="bx--text-input bx--password-input" aria-controls="hint-id_text_help2" aria-describedby="hint-id_text_help2" data-toggle-password-visibility="" id="id_text_help2">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
<div id="hint-id_text_help2" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_disabled(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_help placeholder="Placeholder text" disabled=True %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_help" class="bx--label bx--label--disabled">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text_help" placeholder="Placeholder text" disabled class="bx--text-input bx--password-input" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" data-toggle-password-visibility="" id="id_text_help">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text bx--form__helper-text--disabled">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text placeholder="Placeholder text" light=True %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text" placeholder="Placeholder text" class="bx--text-input bx--text-input--light bx--password-input" data-toggle-password-visibility="" id="id_text">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_invalid_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_missing placeholder="Placeholder text" light=True %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_missing" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper" data-invalid>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--text-input__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <input type="password" name="text_missing" placeholder="Placeholder text" class="bx--text-input bx--text-input--light bx--text-input--invalid bx--password-input" data-toggle-password-visibility="" required id="id_text_missing">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
  <div class="bx--form-requirement">
    <div class="bx--form-requirement__title">This field is required.</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_help placeholder="Placeholder text" light=True %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_help" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text_help" placeholder="Placeholder text" class="bx--text-input bx--text-input--light bx--password-input" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" data-toggle-password-visibility="" id="id_text_help">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help2_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_help2 placeholder="Placeholder text" light=True %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_help2" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text_help2" placeholder="Placeholder text" class="bx--text-input bx--text-input--light bx--password-input" aria-controls="hint-id_text_help2" aria-describedby="hint-id_text_help2" data-toggle-password-visibility="" id="id_text_help2">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
<div id="hint-id_text_help2" class="bx--form__helper-text">
  Optional helper text here; if message is more than one line text should wrap (~100 character count maximum)
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_disabled_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% PasswordInput form.text_help placeholder="Placeholder text" disabled=True light=True %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text_help" class="bx--label bx--label--disabled">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text_help" placeholder="Placeholder text" disabled class="bx--text-input bx--text-input--light bx--password-input" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" data-toggle-password-visibility="" id="id_text_help">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text bx--form__helper-text--disabled">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
