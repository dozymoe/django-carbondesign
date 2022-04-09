# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class RadioHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Radio form.choice2 exclude="blue" label="Radio button label" %}
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Radio button label</legend>
  <div class="bx--form-item">
    <div class="bx--radio-button-group">
<div class="bx--radio-button-wrapper">
  <input id="id_choice2-1" class="bx--radio-button" type="radio" value="red"
      name="choice2" tabindex="0" checked>
  <label for="id_choice2-1" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper">
  <input id="id_choice2-2" class="bx--radio-button" type="radio" value="green"
      name="choice2" tabindex="0">
  <label for="id_choice2-2" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper">
  <input id="id_choice2-3" class="bx--radio-button" type="radio" value="blue"
      name="choice2" tabindex="0" disabled>
  <label for="id_choice2-3" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
    </div>
  </div>
</fieldset>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_horizonal_left(self):
        template = """
{% load carbondesign %}
{% Radio form.choice2 exclude="blue" label="Radio button label" left=True %}
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Radio button label</legend>
  <div class="bx--form-item">
    <div class="bx--radio-button-group ">
<div class="bx--radio-button-wrapper bx--radio-button-wrapper--label-left">
  <input id="id_choice2-1" class="bx--radio-button" type="radio" value="red"
      name="choice2" tabindex="0" checked>
  <label for="id_choice2-1" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper bx--radio-button-wrapper--label-left">
  <input id="id_choice2-2" class="bx--radio-button" type="radio" value="green"
      name="choice2" tabindex="0">
  <label for="id_choice2-2" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper bx--radio-button-wrapper--label-left">
  <input id="id_choice2-3" class="bx--radio-button" type="radio" value="blue"
      name="choice2" tabindex="0" disabled>
  <label for="id_choice2-3" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
    </div>
  </div>
</fieldset>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_vertical(self):
        template = """
{% load carbondesign %}
{% Radio form.choice2 exclude="blue" label="Radio button label" vertical=True %}
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Radio button label</legend>
  <div class="bx--form-item">
    <div class="bx--radio-button-group bx--radio-button-group--vertical">
<div class="bx--radio-button-wrapper">
  <input id="id_choice2-1" class="bx--radio-button" type="radio" value="red"
      name="choice2" tabindex="0" checked>
  <label for="id_choice2-1" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper">
  <input id="id_choice2-2" class="bx--radio-button" type="radio" value="green"
      name="choice2" tabindex="0">
  <label for="id_choice2-2" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper">
  <input id="id_choice2-3" class="bx--radio-button" type="radio" value="blue"
      name="choice2" tabindex="0" disabled>
  <label for="id_choice2-3" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
    </div>
  </div>
</fieldset>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_vertical_left(self):
        template = """
{% load carbondesign %}
{% Radio form.choice2 exclude="blue" label="Radio button label" vertical=True left=True %}
"""
        expected = """
<fieldset class="bx--fieldset">
  <legend class="bx--label">Radio button label</legend>
  <div class="bx--form-item">
    <div class="bx--radio-button-group bx--radio-button-group--vertical">
<div class="bx--radio-button-wrapper bx--radio-button-wrapper--label-left">
  <input id="id_choice2-1" class="bx--radio-button" type="radio" value="red"
      name="choice2" tabindex="0" checked>
  <label for="id_choice2-1" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper bx--radio-button-wrapper--label-left">
  <input id="id_choice2-2" class="bx--radio-button" type="radio" value="green"
      name="choice2" tabindex="0">
  <label for="id_choice2-2" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
<div class="bx--radio-button-wrapper bx--radio-button-wrapper--label-left">
  <input id="id_choice2-3" class="bx--radio-button" type="radio" value="blue"
      name="choice2" tabindex="0" disabled>
  <label for="id_choice2-3" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    <span class="bx--radio-button__label-text">Radio button label</span>
  </label>
</div>
    </div>
  </div>
</fieldset>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
