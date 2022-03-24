# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
from django.test import SimpleTestCase
#-
from .base import compare_template

class DummyForm(forms.Form):
    choice1 = forms.ChoiceField(
            required=False,
            help_text="Optional helper text here")
    choice2 = forms.ChoiceField(
            required=False,
            choices=(
                ('one', 'Option 1'), ('two', 'Option 2'),
                ('three', 'Option 3'), ('four', 'Option 4'),
                ('five', "An example option that is really long to show what "
                         "should be done to handle long text"),
            ),
            help_text="Optional helper text here")

class MultiSelectHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_filterable(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice1 mode="filterable" label="Multi-Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box bx--combo-box bx--multi-select--filterable">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Open menu" aria-haspopup="true" aria-expanded="false">
        <input class="bx--text-input" placeholder="Filter...">
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
      </fieldset>
    </div>
<div id="hint-id_choice1" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_filterable_expanded(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice2 mode="filterable" label="Multi-Select label" expanded=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box bx--combo-box bx--multi-select--filterable bx--list-box--expanded bx--multi-select--selected">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Close menu" aria-haspopup="true" aria-expanded="true">
<div role="button"
    class="bx--list-box__selection bx--list-box__selection--multi bx--tag--filter"
    tabindex="0" title="Clear all selected items">
  1
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear selection" width="16" height="16"
      viewBox="0 0 32 32" role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
        <input class="bx--text-input" placeholder="Filter...">
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Close menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 5L13 10 12.3 10.7 8 6.4 3.7 10.7 3 10z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 1" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-0" value="one" checked>
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 1
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 2" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-1" value="two">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 2
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 3" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-2" value="three">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 3
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 4" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-3" value="four">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 4
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="An example option that is really long to show what should be done to handle long text" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-4" value="five" >
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          An example option that is really long to show what should be done to handle long text
        </span>
      </label>
    </div>
  </div>
</div>
      </fieldset>
    </div>
<div id="hint-id_choice2" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice1 mode="inline" label="Multi-Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper bx--list-box__wrapper--inline">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box bx--list-box--inline">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Open menu" aria-haspopup="true" aria-expanded="false">
        <span class="bx--list-box__label">Multi select options</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
      </fieldset>
    </div>
<div id="hint-id_choice1" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_inline_expanded(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice2 mode="inline" label="Multi-Select label" expanded=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper bx--list-box__wrapper--inline">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box bx--list-box--inline bx--list-box--expanded bx--multi-select--selected">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Close menu" aria-haspopup="true" aria-expanded="true">
<div role="button"
    class="bx--list-box__selection bx--list-box__selection--multi bx--tag--filter"
    tabindex="0" title="Clear all selected items">
  1
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear selection" width="16" height="16"
      viewBox="0 0 32 32" role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
        <span class="bx--list-box__label">Multi select options</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Close menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 5L13 10 12.3 10.7 8 6.4 3.7 10.7 3 10z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 1" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-0" value="one" checked>
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 1
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 2" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-1" value="two">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 2
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 3" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-2" value="three">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 3
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 4" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-3" value="four">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 4
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="An example option that is really long to show what should be done to handle long text" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-4" value="five">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          An example option that is really long to show what should be done to handle long text
        </span>
      </label>
    </div>
  </div>
</div>
      </fieldset>
    </div>
<div id="hint-id_choice2" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_light(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice1 label="Multi-Select label" light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box bx--list-box--light">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Open menu" aria-haspopup="true" aria-expanded="false">
        <span class="bx--list-box__label">Multi select options</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
      </fieldset>
    </div>
<div id="hint-id_choice1" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_light_expanded(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice2 label="Multi-Select label" expanded=True light=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box bx--list-box--light bx--list-box--expanded bx--multi-select--selected">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Close menu" aria-haspopup="true" aria-expanded="true">
<div role="button"
    class="bx--list-box__selection bx--list-box__selection--multi bx--tag--filter"
    tabindex="0" title="Clear all selected items">
  1
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear selection" width="16" height="16"
      viewBox="0 0 32 32" role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
        <span class="bx--list-box__label">Multi select options</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Close menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 5L13 10 12.3 10.7 8 6.4 3.7 10.7 3 10z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 1" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-0" value="one" checked>
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 1
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 2" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-1" value="two">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 2
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 3" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-2" value="three">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 3
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 4" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-3" value="four">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 4
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="An example option that is really long to show what should be done to handle long text" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-4" value="five" >
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          An example option that is really long to show what should be done to handle long text
        </span>
      </label>
    </div>
  </div>
</div>
      </fieldset>
    </div>
<div id="hint-id_choice2" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice1 label="Multi-Select label" %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper ">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Open menu" aria-haspopup="true" aria-expanded="false">
        <span class="bx--list-box__label">Multi select options</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Open menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
      </fieldset>
    </div>
<div id="hint-id_choice1" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_default_expanded(self):
        form = DummyForm(data={'choice2': ['one']})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% MultiSelect form.choice2 label="Multi-Select label" expanded=True %}
"""
        expected = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    <label class="bx--label">
      Multi-Select label
    </label>
    <div class="bx--multi-select bx--list-box bx--list-box--expanded bx--multi-select--selected">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="Close menu" aria-haspopup="true" aria-expanded="true">
<div role="button"
    class="bx--list-box__selection bx--list-box__selection--multi bx--tag--filter"
    tabindex="0" title="Clear all selected items">
  1
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Clear selection" width="16" height="16"
      viewBox="0 0 32 32" role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
        <span class="bx--list-box__label">Multi select options</span>
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="Close menu" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 5L13 10 12.3 10.7 8 6.4 3.7 10.7 3 10z"></path>
  </svg>
</div>
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          Multi-Select label
        </legend>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 1" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-0" value="one" checked>
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 1
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 2" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-1" value="two">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 2
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 3" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-2" value="three">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 3
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="Option 4" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-3" value="four">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          Option 4
        </span>
      </label>
    </div>
  </div>
</div>
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="An example option that is really long to show what should be done to handle long text" class="bx--checkbox-label">
        <input type="checkbox" name="choice2" readonly class="bx--checkbox"
            id="id_choice2-4" value="five">
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          An example option that is really long to show what should be done to handle long text
        </span>
      </label>
    </div>
  </div>
</div>
      </fieldset>
    </div>
<div id="hint-id_choice2" class="bx--form__helper-text">
  Optional helper text here
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
