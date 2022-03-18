# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
from django.test import SimpleTestCase
#-
from .base import compare_template

class DummyForm(forms.Form):
    text = forms.CharField(
            label="Combo box label",
            required=False,
            help_text="Optional helper text here")
    text_missing = forms.CharField(
            label="Combo box label",
            required=True)
    number = forms.IntegerField(
            label="Combo box label",
            required=False)


class ComboBoxHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_empty(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.text id="downshift-input-2" placeholder="Filter..." %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
<label for="downshift-input-2" class="bx--label">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box">
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-haspopup="listbox" aria-expanded="false">
        <input type="text" name="text" id="downshift-input-2" placeholder="Filter..." class="bx--text-input" aria-controls="downshift-input-2-hint" aria-describedby="downshift-input-2-hint" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="false">
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
      </ul>
    </div>
<div class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_has_value(self):
        form = DummyForm(data={'text': "This is not a value."})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.text id="downshift-input-2" placeholder="Filter..." %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
<label for="downshift-input-2" class="bx--label">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box">
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-haspopup="listbox" aria-expanded="false">
        <input type="text" name="text" value="This is not a value." id="downshift-input-2" placeholder="Filter..." class="bx--text-input" aria-controls="downshift-input-2-hint" aria-describedby="downshift-input-2-hint" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="false">
<div class="bx--list-box__selection" role="button" title="Clear all">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear all" width="16" height="16" viewBox="0 0 32 32"
      role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
      </ul>
    </div>
<div class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_missing(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.text_missing id="downshift-input-2" placeholder="Filter..." %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
<label for="downshift-input-2" class="bx--label">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box" data-invalid>
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-haspopup="listbox" aria-expanded="false">
        <input type="text" name="text_missing" id="downshift-input-2" placeholder="Filter..." class="bx--text-input" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="false" required>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--list-box__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
      </ul>
    </div>
    <div class="bx--form-requirement">
      * This field is required.
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_invalid(self):
        form = DummyForm(data={'number': "This is not a values."})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.number id="downshift-input-2" placeholder="Filter..." %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
<label for="downshift-input-2" class="bx--label">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box" data-invalid>
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-haspopup="listbox" aria-expanded="false">
        <input type="number" name="number" value="This is not a values." id="downshift-input-2" placeholder="Filter..." class="bx--text-input" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="false">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--list-box__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
<div class="bx--list-box__selection" role="button" title="Clear all">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear all" width="16" height="16" viewBox="0 0 32 32"
      role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
      </ul>
    </div>
    <div class="bx--form-requirement">
      * Enter a whole number.
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_missing_disabled(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.text_missing id="downshift-input-2" placeholder="Filter..." disabled=True %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
<label for="downshift-input-2" class="bx--label bx--label--disabled">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box bx--list-box--disabled" data-invalid>
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-haspopup="true" disabled="" aria-expanded="false">
        <input type="text" name="text_missing" id="downshift-input-2" placeholder="Filter..." disabled="" class="bx--text-input" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="false" required>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--list-box__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
      </ul>
    </div>
    <div class="bx--form-requirement">
      * This field is required.
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_invalid_disabled(self):
        form = DummyForm(data={'number': "This is not a values."})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.number id="downshift-input-2" placeholder="Filter..." disabled=True %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
<label for="downshift-input-2" class="bx--label bx--label--disabled">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box bx--list-box--disabled" data-invalid>
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-haspopup="true" disabled="" aria-expanded="false">
        <input type="number" name="number" value="This is not a values." id="downshift-input-2" placeholder="Filter..." disabled="" class="bx--text-input" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="false">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--list-box__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
<div class="bx--list-box__selection" role="button" title="Clear all">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear all" width="16" height="16" viewBox="0 0 32 32"
      role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
      </ul>
    </div>
    <div class="bx--form-requirement">
      * Enter a whole number.
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_options_empty(self):
        form = DummyForm(data={})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.text id="downshift-input-2" placeholder="Filter..." expanded=True %}
  {% ComboBoxItem id="downshift-1-item-0" %}
    Option 1
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-1" %}
    Option 2
  {% endComboBoxItem %}
  {% ComboBoxItem active=True id="downshift-1-item-2" %}
    Option 3
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-3" %}
    Option 4
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-4" %}
    An example option that is really long to show what should be done to
    handle long text
  {% endComboBoxItem %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
<label for="downshift-input-2" class="bx--label">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box bx--list-box--expanded">
      <div role="combobox" class="bx--list-box__field" aria-label="Close menu"
          aria-haspopup="listbox" aria-expanded="true">
        <input type="text" name="text" id="downshift-input-2" placeholder="Filter..." class="bx--text-input" aria-controls="downshift-input-2-hint" aria-describedby="downshift-input-2-hint" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="true">
<div class="bx--list-box__menu-icon bx--list-box__menu-icon--open">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Close menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
<li class="bx--list-box__menu-item" id="downshift-1-item-0">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 1
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-1">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 2
  </div>
</li>
<li class="bx--list-box__menu-item bx--list-box__menu-item--highlighted" id="downshift-1-item-2">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 3
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-3">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 4
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-4">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    An example option that is really long to show what should be done to
    handle long text
  </div>
</li>
      </ul>
    </div>
<div class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_options(self):
        form = DummyForm(data={'text': "Option 3"})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.text id="downshift-input-2" placeholder="Filter..." expanded=True %}
  {% ComboBoxItem id="downshift-1-item-0" %}
    Option 1
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-1" %}
    Option 2
  {% endComboBoxItem %}
  {% ComboBoxItem active=True id="downshift-1-item-2" %}
    Option 3
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-3" %}
    Option 4
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-4" %}
    An example option that is really long to show what should be done to
    handle long text
  {% endComboBoxItem %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
<label for="downshift-input-2" class="bx--label">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box bx--list-box--expanded">
      <div role="combobox" class="bx--list-box__field" aria-label="Close menu"
          aria-haspopup="listbox" aria-expanded="true">
        <input type="text" name="text" value="Option 3" id="downshift-input-2" placeholder="Filter..." class="bx--text-input" aria-controls="downshift-input-2-hint" aria-describedby="downshift-input-2-hint" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="true">
<div class="bx--list-box__selection" role="button" title="Clear all">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear all" width="16" height="16" viewBox="0 0 32 32"
      role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
<div class="bx--list-box__menu-icon bx--list-box__menu-icon--open">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Close menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
<li class="bx--list-box__menu-item" id="downshift-1-item-0">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 1
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-1">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 2
  </div>
</li>
<li class="bx--list-box__menu-item bx--list-box__menu-item--highlighted" id="downshift-1-item-2">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 3
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-3">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 4
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-4">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    An example option that is really long to show what should be done to
    handle long text
  </div>
</li>
      </ul>
    </div>
<div class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_options_invalid(self):
        form = DummyForm(data={'number': "Option 3"})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% ComboBox form.number id="downshift-input-2" placeholder="Filter..." %}
  {% ComboBoxItem id="downshift-1-item-0" %}
    Option 1
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-1" %}
    Option 2
  {% endComboBoxItem %}
  {% ComboBoxItem active=True id="downshift-1-item-2" %}
    Option 3
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-3" %}
    Option 4
  {% endComboBoxItem %}
  {% ComboBoxItem id="downshift-1-item-4" %}
    An example option that is really long to show what should be done to
    handle long text
  {% endComboBoxItem %}
{% endComboBox %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
<label for="downshift-input-2" class="bx--label">
  Combo box label
</label>
    <div class="bx--combo-box bx--list-box" data-invalid>
      <div role="combobox" class="bx--list-box__field" aria-label="Open menu"
          aria-haspopup="listbox" aria-expanded="false">
        <input type="number" name="number" value="Option 3" id="downshift-input-2" placeholder="Filter..." class="bx--text-input" aria-autocomplete="list" autocomplete="off" aria-owns="menu-downshift-input-2" aria-expanded="false">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--list-box__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
<div class="bx--list-box__selection" role="button" title="Clear all">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear all" width="16" height="16" viewBox="0 0 32 32"
      role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-downshift-input-2"
          aria-label="Combo box label">
<li class="bx--list-box__menu-item" id="downshift-1-item-0">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 1
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-1">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 2
  </div>
</li>
<li class="bx--list-box__menu-item bx--list-box__menu-item--highlighted" id="downshift-1-item-2">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 3
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-3">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    Option 4
  </div>
</li>
<li class="bx--list-box__menu-item" id="downshift-1-item-4">
  <div class="bx--list-box__menu-item__option" tabindex="0">
    An example option that is really long to show what should be done to
    handle long text
  </div>
</li>
      </ul>
    </div>
    <div class="bx--form-requirement">
      * Enter a whole number.
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
