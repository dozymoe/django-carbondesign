# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class BreadcrumbTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Breadcrumb %}
{% endBreadcrumb %}
"""
        expected = """
<nav class="bx--breadcrumb" aria-label="breadcrumb">
</nav>
"""
        rendered = compare_template(template, expected)
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
<div class="bx--breadcrumb-item">
  <a href="#" class="bx--link">
  </a>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class BreadcrumbHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_breadcrumb(self):
        template = """
{% load carbondesign %}
{% Breadcrumb %}
  {% BreadcrumbItem href="#" %}
    Breadcrumb 1
  {% endBreadcrumbItem %}

  {% BreadcrumbItem href="#" %}
    Breadcrumb 2
  {% endBreadcrumbItem %}

  {% BreadcrumbItem href="#" %}
    Breadcrumb 3
  {% endBreadcrumbItem %}
{% endBreadcrumb %}
"""
        expected = """
<nav class="bx--breadcrumb" aria-label="breadcrumb">
<div class="bx--breadcrumb-item">
  <a href="#" class="bx--link">
    Breadcrumb 1
  </a>
</div>
<div class="bx--breadcrumb-item">
  <a href="#" class="bx--link">
    Breadcrumb 2
  </a>
</div>
<div class="bx--breadcrumb-item">
  <a href="#" class="bx--link">
    Breadcrumb 3
  </a>
</div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_current_page(self):
        template = """
{% load carbondesign %}
{% Breadcrumb current=True %}
  {% BreadcrumbItem href="#" %}
    Breadcrumb 1
  {% endBreadcrumbItem %}

  {% BreadcrumbItem href="#" %}
    Breadcrumb 2
  {% endBreadcrumbItem %}

  {% BreadcrumbItem href="#" current=True %}
    Breadcrumb 3
  {% endBreadcrumbItem %}
{% endBreadcrumb %}
"""
        expected = """
<nav class="bx--breadcrumb bx--breadcrumb--no-trailing-slash" aria-label="breadcrumb">
<div class="bx--breadcrumb-item">
  <a href="#" class="bx--link">
    Breadcrumb 1
  </a>
</div>
<div class="bx--breadcrumb-item">
  <a href="#" class="bx--link">
    Breadcrumb 2
  </a>
</div>
<div class="bx--breadcrumb-item bx--breadcrumb-item--current">
  <a href="#" class="bx--link" aria-current="page">
    Breadcrumb 3
  </a>
</div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_enabled(self):
        template = """
{% load carbondesign %}
{% Breadcrumb %}
  {% BreadcrumbItem href="#" %}
    Breadcrumb 1
  {% endBreadcrumbItem %}
{% endBreadcrumb %}
"""
        expected = """
<nav class="bx--breadcrumb" aria-label="breadcrumb">
<div class="bx--breadcrumb-item">
  <a href="#" class="bx--link">
    Breadcrumb 1
  </a>
</div>
</nav>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
