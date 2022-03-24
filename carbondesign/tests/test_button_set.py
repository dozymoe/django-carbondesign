# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ButtonSetTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% ButtonSet %}
  {% Button variant="secondary" %}
    Secondary Button
  {% endButton %}

  {% Button variant="primary" %}
    Primary Button
  {% endButton %}
{% endButtonSet %}
"""
        expected = """
<div class="bx--btn-set">
<button class="bx--btn bx--btn--secondary">
    Secondary Button
</button>
<button class="bx--btn bx--btn--primary">
    Primary Button
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_disabled(self):
        template = """
{% load carbondesign %}
{% ButtonSet %}
  {% Button variant="secondary" disabled=True %}
    Secondary Button
  {% endButton %}

  {% Button variant="primary" disabled=True %}
    Primary Button
  {% endButton %}
{% endButtonSet %}
"""
        expected = """
<div class="bx--btn-set">
<button class="bx--btn bx--btn--secondary bx--btn--disabled" disabled="disabled">
    Secondary Button
</button>
<button class="bx--btn bx--btn--primary bx--btn--disabled" disabled="disabled">
    Primary Button
</button>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
