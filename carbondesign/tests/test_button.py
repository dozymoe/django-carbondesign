# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class ButtonTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Button %}
{% endButton %}
"""
        expected = """
<button class="bx--btn bx--btn--primary">
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class ButtonSetTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% ButtonSet %}
{% endButtonSet %}
"""
        expected = """
<div class="bx--btn-set">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
