# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    checkbox = forms.ChoiceField(
            label="Checkbox (input + label)",
            required=False,
            choices=(
                ('new', "Checkbox"),
                ('ind', "Indeterminate checkbox")))


class DummyFormInside(forms.Form):
    checkbox = forms.ChoiceField(
            label="Checkbox (label > input)",
            required=False,
            choices=(
                ('yellow', "Checkbox"),
                ('ind', "Indeterminate checkbox")))


class CheckBoxHtmlTest(SimpleTestCase):
    maxDiff = None

    def atest_default(self):
        form = DummyForm(initial={'checkbox': 'new'})
        context = {'form': form}

        template = """
{% load carbondesign %}
<fieldset class="bx--fieldset">
  <legend class="bx--label">{{form.checkbox.label}}</legend>

  {% CheckBox form.checkbox value="new" id="bx--checkbox-new" %}
  {% CheckBox form.checkbox value="ind" id="bx--checkbox-ind" mixed=True %}
  {% CheckBox form.checkbox value="new" id="bx--checkbox-new--disabled" disabled=True %}
  {% CheckBox form.checkbox value="ind" id="bx--checkbox-ind--disabled" mixed=True disabled=True %}
  {% CheckBox form.checkbox value="new" id="bx--checkbox-disabled" label="Disabled checkbox" disabled=True %}
</fieldset>
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Checkbox (input + label)</legend>
<div class="bx--form-item bx--checkbox-wrapper">
  <input type="checkbox" name="checkbox" value="new" id="bx--checkbox-new" class="bx--checkbox" checked>
<label for="bx--checkbox-new" class="bx--checkbox-label">
  Checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input type="checkbox" name="checkbox" value="ind" id="bx--checkbox-ind" aria-checked="mixed" class="bx--checkbox">
<label for="bx--checkbox-ind" class="bx--checkbox-label">
  Indeterminate checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input type="checkbox" name="checkbox" value="new" id="bx--checkbox-new--disabled" disabled class="bx--checkbox" checked>
<label for="bx--checkbox-new--disabled" class="bx--checkbox-label">
  Checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input type="checkbox" name="checkbox" value="ind" id="bx--checkbox-ind--disabled" disabled aria-checked="mixed" class="bx--checkbox">
<label for="bx--checkbox-ind--disabled" class="bx--checkbox-label">
  Indeterminate checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input type="checkbox" name="checkbox" value="new" id="bx--checkbox-disabled" disabled class="bx--checkbox" checked>
<label for="bx--checkbox-disabled" class="bx--checkbox-label">
  Disabled checkbox
</label>
</div>
</fieldset>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)


    def atest_inside(self):
        form = DummyFormInside(initial={'checkbox': 'yellow'})
        context = {'form': form}

        template = """
{% load carbondesign %}
<fieldset class="bx--fieldset">
  <legend class="bx--label">{{form.checkbox.label}}</legend>

  {% CheckBox mode="inside" form.checkbox value="yellow" id="bx--checkbox-new2" %}
  {% CheckBox mode="inside" form.checkbox value="ind" id="bx--checkbox-ind2" mixed=True label="Indeterminate checkbox" %}
  {% CheckBox mode="inside" form.checkbox value="yellow" id="bx--checkbox-new2--disabled" label="Checkbox (label &gt; input)" disabled=True %}
  {% CheckBox mode="inside" form.checkbox value="ind" id="bx--checkbox-ind2--disabled" mixed=True disabled=True label="Indeterminate checkbox" %}
  {% CheckBox mode="inside" form.checkbox value="yellow" id="bx--checkbox-disabled2" label="Disabled checkbox" disabled=True %}
</fieldset>
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Checkbox (label &gt; input)</legend>
<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-new2" class="bx--checkbox-label">
    <input type="checkbox" name="checkbox" value="yellow" id="bx--checkbox-new2" class="bx--checkbox" checked>
    Checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-ind2" class="bx--checkbox-label" data-contained-checkbox-state="mixed">
    <input type="checkbox" name="checkbox" value="ind" id="bx--checkbox-ind2" aria-checked="mixed" class="bx--checkbox">
    Indeterminate checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-new2--disabled" class="bx--checkbox-label">
    <input type="checkbox" name="checkbox" value="yellow" id="bx--checkbox-new2--disabled" disabled class="bx--checkbox" checked>
    Checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-ind2--disabled" class="bx--checkbox-label" data-contained-checkbox-state="mixed">
    <input type="checkbox" name="checkbox" value="ind" id="bx--checkbox-ind2--disabled" disabled aria-checked="mixed" class="bx--checkbox">
    Indeterminate checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-disabled2" class="bx--checkbox-label">
    <input type="checkbox" name="checkbox" value="yellow" id="bx--checkbox-disabled2" disabled class="bx--checkbox" checked>
    Disabled checkbox
  </label>
</div>
</fieldset>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
