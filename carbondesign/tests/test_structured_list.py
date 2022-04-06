# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class StructuredListTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Sl %}
{% endSl %}
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
{% SlTr %}
{% endSlTr %}
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
{% SlTh %}
{% endSlTh %}
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
{% SlTd %}
{% endSlTd %}
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
{% SlSelect form.choice %}
{% endSlSelect %}
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
