# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ToggleHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle id="toggle1" label="Toggle with visible label" %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="toggle1" class="bx--toggle-input">
  <label class="bx--toggle-input__label" for="toggle1">
    Toggle with visible label
    <span class="bx--toggle__switch">
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_nolabel(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle mode="nolabel" id="toggle0" %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="toggle0" class="bx--toggle-input">
  <label class="bx--toggle-input__label" for="toggle0" aria-label="example toggle with state indicator text">
    <span class="bx--toggle__switch">
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_disabled(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle id="toggle4" label="Toggle with visible label" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="toggle4" disabled class="bx--toggle-input">
  <label class="bx--toggle-input__label" for="toggle4">
    Toggle with visible label
    <span class="bx--toggle__switch">
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_nolabel_disabled(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle mode="nolabel" id="toggle3" disabled=True %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="toggle3" disabled class="bx--toggle-input">
  <label class="bx--toggle-input__label" for="toggle3" aria-label="example toggle with state indicator text">
    <span class="bx--toggle__switch">
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_small(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle id="smalltoggle2" label="Toggle with visible label" small=True %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="smalltoggle2" class="bx--toggle-input bx--toggle-input--small">
  <label class="bx--toggle-input__label" for="smalltoggle2">
    Toggle with visible label
    <span class="bx--toggle__switch">
<svg class="bx--toggle__check" width="6px" height="5px" viewBox="0 0 6 5">
  <path d="M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z" />
</svg>
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_nolabel_small(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle mode="nolabel" id="smalltoggle1" small=True %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="smalltoggle1" class="bx--toggle-input bx--toggle-input--small">
  <label class="bx--toggle-input__label" for="smalltoggle1" aria-label="example toggle with state indicator text">
    <span class="bx--toggle__switch">
<svg class="bx--toggle__check" width="6px" height="5px" viewBox="0 0 6 5">
  <path d="M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z" />
</svg>
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_default_small_disabled(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle id="smalltoggle5" label="Toggle with visible label" disabled=True small=True %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="smalltoggle5" disabled class="bx--toggle-input bx--toggle-input--small">
  <label class="bx--toggle-input__label" for="smalltoggle5">
    Toggle with visible label
    <span class="bx--toggle__switch">
<svg class="bx--toggle__check" width="6px" height="5px" viewBox="0 0 6 5">
  <path d="M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z" />
</svg>
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_nolabel_small_disabled(self):
        template = """
{% load carbondesign %}
{% Toggle form.toggle mode="nolabel" id="smalltoggle4" disabled=True small=True %}
"""
        expected = """
<div class="bx--form-item">
  <input type="checkbox" name="toggle" id="smalltoggle4" disabled class="bx--toggle-input bx--toggle-input--small">
  <label class="bx--toggle-input__label" for="smalltoggle4" aria-label="example toggle with state indicator text">
    <span class="bx--toggle__switch">
<svg class="bx--toggle__check" width="6px" height="5px" viewBox="0 0 6 5">
  <path d="M2.2 2.7L5 0 6 1 2.2 5 0 2.7 1 1.5z" />
</svg>
      <span class="bx--toggle__text--off" aria-hidden="true">Off</span>
      <span class="bx--toggle__text--on" aria-hidden="true">On</span>
    </span>
  </label>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
