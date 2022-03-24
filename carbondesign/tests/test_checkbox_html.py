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

    def test_default(self):
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
  <input name="checkbox" value="new" type="checkbox" id="bx--checkbox-new"
      class="bx--checkbox" checked="">
<label for="bx--checkbox-new" class="bx--checkbox-label">
  Checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input name="checkbox" value="ind" type="checkbox" id="bx--checkbox-ind"
      class="bx--checkbox" aria-checked="mixed">
<label for="bx--checkbox-ind" class="bx--checkbox-label">
  Indeterminate checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input name="checkbox" value="new" type="checkbox" id="bx--checkbox-new--disabled"
      class="bx--checkbox" disabled="" checked="">
<label for="bx--checkbox-new--disabled" class="bx--checkbox-label">
  Checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input name="checkbox" value="ind" type="checkbox" id="bx--checkbox-ind--disabled"
      class="bx--checkbox" disabled="" aria-checked="mixed">
<label for="bx--checkbox-ind--disabled" class="bx--checkbox-label">
  Indeterminate checkbox
</label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <input name="checkbox" value="new" type="checkbox" id="bx--checkbox-disabled"
      class="bx--checkbox" disabled="" checked="">
<label for="bx--checkbox-disabled" class="bx--checkbox-label">
  Disabled checkbox
</label>
</div>
</fieldset>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)


    def test_inside(self):
        form = DummyFormInside(initial={'checkbox': 'yellow'})
        context = {'form': form}

        template = """
{% load carbondesign %}
<fieldset class="bx--fieldset">
  <legend class="bx--label">{{form.checkbox.label}}</legend>

  {% CheckBox mode="inside" form.checkbox value="yellow" id="bx--checkbox-new2" %}
  {% CheckBox mode="inside" form.checkbox value="ind" id="bx--checkbox-ind2" mixed=True %}
  {% CheckBox mode="inside" form.checkbox value="yellow" id="bx--checkbox-new2--disabled" disabled=True %}
  {% CheckBox mode="inside" form.checkbox value="ind" id="bx--checkbox-ind2--disabled" mixed=True disabled=True %}
  {% CheckBox mode="inside" form.checkbox value="yellow" id="bx--checkbox-disabled2" label="Disabled checkbox" disabled=True %}
</fieldset>
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Checkbox (label &gt; input)</legend>
<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-new2" class="bx--checkbox-label">
    <input name="checkbox" value="yellow" type="checkbox" id="bx--checkbox-new2"
        class="bx--checkbox" checked="">
    Checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-ind2" class="bx--checkbox-label" data-contained-checkbox-state="mixed">
    <input name="checkbox" value="ind" type="checkbox" id="bx--checkbox-ind2"
        class="bx--checkbox" aria-checked="mixed">
    Indeterminate checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-new2--disabled" class="bx--checkbox-label">
    <input name="checkbox" value="yellow" type="checkbox" id="bx--checkbox-new2--disabled"
        class="bx--checkbox" disabled="" checked="">
    Checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-ind2--disabled" class="bx--checkbox-label" data-contained-checkbox-state="mixed">
    <input name="checkbox" value="ind" type="checkbox" id="bx--checkbox-ind2--disabled"
        class="bx--checkbox" disabled="" aria-checked="mixed">
    Indeterminate checkbox
  </label>
</div>

<div class="bx--form-item bx--checkbox-wrapper">
  <label for="bx--checkbox-disabled2" class="bx--checkbox-label">
    <input name="checkbox" value="yellow" type="checkbox" id="bx--checkbox-disabled2"
        class="bx--checkbox" disabled="" checked="">
    Disabled checkbox
  </label>
</div>
</fieldset>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
