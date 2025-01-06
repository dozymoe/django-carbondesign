# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long
from django import forms
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    text = forms.CharField(
            label="Text Area label",
            required=False)
    text_missing = forms.CharField(
            label="Text Area label",
            required=True)
    text_help = forms.CharField(
            label="Text Area label",
            required=False,
            help_text="Optional helper text goes here")


class TextAreaHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TextArea form.text placeholder="Placeholder text." cols=50 rows=4 %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text" class="bx--label">
  Text Area label
</label>
  <div class="bx--text-area__wrapper">
    <textarea name="text" cols="50" rows="4" placeholder="Placeholder text." class="bx--text-area bx--text-area--v2" id="id_text">
</textarea>
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
{% TextArea form.text_missing placeholder="Placeholder text." cols=50 rows=4 %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text_missing" class="bx--label">
  Text Area label
</label>
  <div class="bx--text-area__wrapper" data-invalid>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--text-area__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <textarea name="text_missing" cols="50" rows="4" placeholder="Placeholder text." class="bx--text-area bx--text-area--v2 bx--text-area--invalid" required id="id_text_missing" aria-invalid="true">
</textarea>
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
{% TextArea form.text_help placeholder="Placeholder text." cols=50 rows=4 %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text_help" class="bx--label">
  Text Area label
</label>
  <div class="bx--text-area__wrapper">
    <textarea name="text_help" cols="50" rows="4" placeholder="Placeholder text." class="bx--text-area bx--text-area--v2" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
</textarea>
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text">
  Optional helper text goes here
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
{% TextArea form.text_help placeholder="Placeholder text." cols=50 rows=4 disabled=True %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text_help" class="bx--label bx--label--disabled">
  Text Area label
</label>
  <div class="bx--text-area__wrapper">
    <textarea name="text_help" cols="50" rows="4" placeholder="Placeholder text." disabled class="bx--text-area bx--text-area--v2" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
</textarea>
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
{% TextArea form.text placeholder="Placeholder text." cols=50 rows=4 light=True %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text" class="bx--label">
  Text Area label
</label>
  <div class="bx--text-area__wrapper">
    <textarea name="text" cols="50" rows="4" placeholder="Placeholder text." class="bx--text-area bx--text-area--v2 bx--text-area--light" id="id_text">
</textarea>
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
{% TextArea form.text_missing placeholder="Placeholder text." cols=50 rows=4 light=True %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text_missing" class="bx--label">
  Text Area label
</label>
  <div class="bx--text-area__wrapper" data-invalid>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--text-area__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2	c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8	c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
    <textarea name="text_missing" cols="50" rows="4" placeholder="Placeholder text." class="bx--text-area bx--text-area--v2 bx--text-area--light bx--text-area--invalid" required id="id_text_missing" aria-invalid="true">
</textarea>
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
{% TextArea form.text_help placeholder="Placeholder text." cols=50 rows=4 light=True %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text_help" class="bx--label">
  Text Area label
</label>
  <div class="bx--text-area__wrapper">
    <textarea name="text_help" cols="50" rows="4" placeholder="Placeholder text." class="bx--text-area bx--text-area--v2 bx--text-area--light" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
</textarea>
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text">
  Optional helper text goes here
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
{% TextArea form.text_help placeholder="Placeholder text." cols=50 rows=4 disabled=True light=True %}
"""
        expected = """
<div class="bx--form-item">
<label for="id_text_help" class="bx--label bx--label--disabled">
  Text Area label
</label>
  <div class="bx--text-area__wrapper">
    <textarea name="text_help" cols="50" rows="4" placeholder="Placeholder text." disabled class="bx--text-area bx--text-area--v2 bx--text-area--light" aria-controls="hint-id_text_help" aria-describedby="hint-id_text_help" id="id_text_help">
</textarea>
  </div>
<div id="hint-id_text_help" class="bx--form__helper-text bx--form__helper-text--disabled">
  Optional helper text goes here
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
