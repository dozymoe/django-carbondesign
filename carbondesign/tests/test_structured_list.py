# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class StructuredListTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% StructuredList %}
{% endStructuredList %}
"""
        expected = """
<section class="bx--structured-list">
  <div class="bx--structured-list-thead">
    <div class="bx--structured-list-row bx--structured-list-row--header-row">
    </div>
  </div>
  <div class="bx--structured-list-tbody">
  </div>
</section>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class StructuredListTrTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% StructuredListTr %}
{% endStructuredListTr %}
"""
        expected = """
<div class="bx--structured-list-row">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class StructuredListThTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% StructuredListTh %}
{% endStructuredListTh %}
"""
        expected = """
<div class="bx--structured-list-th">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class StructuredListTdTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% StructuredListTd %}
{% endStructuredListTd %}
"""
        expected = """
<div class="bx--structured-list-td">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class StructuredListSelectTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% StructuredListSelect form.choice %}
{% endStructuredListSelect %}
"""
        expected = """
<section class="bx--structured-list bx--structured-list--selection"
    data-structured-list>
  <div class="bx--structured-list-thead">
    <div class="bx--structured-list-row bx--structured-list-row--header-row">
    </div>
  </div>
  <div class="bx--structured-list-tbody">
  </div>
</section>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
