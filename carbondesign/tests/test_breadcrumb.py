# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class BreadcrumbTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Breadcrumb %}
{% endBreadcrumb %}
"""
        expected = """
<nav class="bx--breadcrumb " aria-label="breadcrumb" >
</nav>
"""
        rendered = compare_template(template, expected, {})
        self.assertEqual(*rendered)


class BreadcrumbItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% BreadcrumbItem %}
{% endBreadcrumbItem %}
"""
        expected = """
<div class="bx--breadcrumb-item " >
  <a href="{href}" class="bx--link">
  </a>
</div>
"""
        rendered = compare_template(template, expected, {})
        self.assertEqual(*rendered)
