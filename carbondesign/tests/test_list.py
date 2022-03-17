# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class ListTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% List %}
{% endList %}
"""
        expected = """
<ul class="bx--list--unordered">
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class LiTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Li %}
{% endLi %}
"""
        expected = """
<li class="bx--list__item">
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
