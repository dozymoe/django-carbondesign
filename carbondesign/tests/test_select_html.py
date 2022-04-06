# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    select = forms.ChoiceField(
            required=False,
            choices=(
                ('solong', "A much longer option that is worth having around "
                    "to check how text flows"),
                ("Category 1", (
                    ('option1', "Option 1"),
                    ('option2', "Option 2"),
                )),
                ("Category 2", (
                    ('option1', "Option 1"),
                    ('option2', "Option 2"),
                )),
            ))
    select_help = forms.ChoiceField(
            required=False,
            choices=(
                ('solong', "A much longer option that is worth having around "
                    "to check how text flows"),
                ("Category 1", (
                    ('option1', "Option 1"),
                    ('option2', "Option 2"),
                )),
                ("Category 2", (
                    ('option1', "Option 1"),
                    ('option2', "Option 2"),
                )),
            ),
            help_text="Optional helper text.")


class SelectTestHtml(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select label="Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select">
<label for="id_select" class="bx--label">
  Select label
</label>
    <div class="bx--select-input__wrapper">
      <select class="bx--select-input" id="id_select" name="select">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
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
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_disabled(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select label="Select label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--disabled">
<label for="id_select" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input__wrapper" >
      <select class="bx--select-input" id="id_select" name="select" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
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
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select mode="inline" label="Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline">
<label for="id_select" class="bx--label">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" >
        <select class="bx--select-input" id="id_select" name="select">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
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
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_disabled(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select mode="inline" label="Select label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--disabled">
<label for="id_select" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" >
        <select class="bx--select-input" id="id_select" name="select" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
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
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select_help label="Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select">
<label for="id_select_help" class="bx--label">
  Select label
</label>
    <div class="bx--select-input__wrapper" >
      <select class="bx--select-input" id="id_select_help" name="select_help">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
<div id="hint-id_select_help" class="bx--form__helper-text">
  Optional helper text.
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_help_disabled(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select_help label="Select label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--disabled">
<label for="id_select_help" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input__wrapper" >
      <select class="bx--select-input" id="id_select_help" name="select_help" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
<div id="hint-id_select_help" class="bx--form__helper-text">
  Optional helper text.
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_help(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select_help mode="inline" label="Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline">
<label for="id_select_help" class="bx--label">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" >
        <select class="bx--select-input" id="id_select_help" name="select_help">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
      </div>
    </div>
<div id="hint-id_select_help" class="bx--form__helper-text">
  Optional helper text.
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_help_disabled(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select_help mode="inline" label="Select label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--disabled">
<label for="id_select_help" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" >
        <select class="bx--select-input" id="id_select_help" name="select_help" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
      </div>
    </div>
<div id="hint-id_select_help" class="bx--form__helper-text">
  Optional helper text.
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_invalid(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select mode="inline" label="Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid">
<label for="id_select" class="bx--label">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" data-invalid>
        <select class="bx--select-input" id="id_select" name="select">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--select__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_invalid_disabled(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select mode="inline" label="Select label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid bx--select--disabled">
<label for="id_select" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" data-invalid>
        <select class="bx--select-input" id="id_select" name="select" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_help_invalid(self):
        form = DummyForm(data={'select_help': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select_help mode="inline" label="Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid">
<label for="id_select_help" class="bx--label">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" data-invalid>
        <select class="bx--select-input" id="id_select_help" name="select_help">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--select__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
      </div>
    </div>
<div id="hint-id_select_help" class="bx--form__helper-text">
  Optional helper text.
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_help_invalid_disabled(self):
        form = DummyForm(data={'select_help': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select_help mode="inline" label="Select label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid bx--select--disabled">
<label for="id_select_help" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" data-invalid>
        <select class="bx--select-input" id="id_select_help" name="select_help" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
      </div>
    </div>
<div id="hint-id_select_help" class="bx--form__helper-text">
  Optional helper text.
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_invalid_light(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select mode="inline" label="Select label" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid bx--select--light">
<label for="id_select" class="bx--label">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" data-invalid>
        <select class="bx--select-input" id="id_select" name="select">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--select__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_invalid_disabled_light(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select mode="inline" label="Select label" disabled=True light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--inline bx--select--invalid bx--select--disabled bx--select--light">
<label for="id_select" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input--inline__wrapper">
      <div class="bx--select-input__wrapper" data-invalid>
        <select class="bx--select-input" id="id_select" name="select" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
        </select>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
            aria-hidden="true">
          <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
        </svg>
      </div>
      <div class="bx--form-requirement">
        <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_invalid(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select label="Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--invalid">
<label for="id_select" class="bx--label">
  Select label
</label>
    <div class="bx--select-input__wrapper" data-invalid>
      <select class="bx--select-input" id="id_select" name="select">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--select__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_invalid_disabled(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select label="Select label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--invalid bx--select--disabled">
<label for="id_select" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input__wrapper" data-invalid>
      <select class="bx--select-input" id="id_select" name="select" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
    </div>
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
{% Select form.select label="Select label" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--light">
<label for="id_select" class="bx--label">
  Select label
</label>
    <div class="bx--select-input__wrapper" >
      <select class="bx--select-input" id="id_select" name="select">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
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
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_disabled_light(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select label="Select label" disabled=True light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--disabled bx--select--light">
<label for="id_select" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input__wrapper">
      <select class="bx--select-input" id="id_select" name="select" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
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
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_invalid_light(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select label="Select label" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--invalid bx--select--light">
<label for="id_select" class="bx--label">
  Select label
</label>
    <div class="bx--select-input__wrapper" data-invalid>
      <select class="bx--select-input" id="id_select" name="select">
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--select__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_invalid_disabled_light(self):
        form = DummyForm(data={'select': 'a'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Select form.select label="Select label" disabled=True light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--select bx--select--invalid bx--select--disabled bx--select--light">
<label for="id_select" class="bx--label bx--label--disabled">
  Select label
</label>
    <div class="bx--select-input__wrapper" data-invalid>
      <select class="bx--select-input" id="id_select" name="select" disabled>
<option class="bx--select-option" value="">Choose an option</option>
<option class="bx--select-option" value="solong">A much longer option that is worth having around to check how text flows</option>
<optgroup class="bx--select-optgroup" label="Category 1">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
<optgroup class="bx--select-optgroup" label="Category 2">
<option class="bx--select-option" value="option1">Option 1</option>
<option class="bx--select-option" value="option2">Option 2</option>
</optgroup>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <div class="bx--form-requirement">
      <div class="bx--form-requirement__title">Select a valid choice.</div>
<p class="bx--form-requirement__supplement">a is not one of the available choices.</p>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
