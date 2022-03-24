# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class LinkHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Link href="#" %}Link{% endLink %}
"""
        expected = """
<a class="bx--link" href="#">Link</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_visited(self):
        template = """
{% load carbondesign %}
{% Link href="http://www.google.com" visited=True %}Link{% endLink %}
"""
        expected = """
<a class="bx--link bx--link--visited" href="http://www.google.com">Link</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_disabled(self):
        template = """
{% load carbondesign %}
{% Link disabled=True %}Placeholder link{% endLink %}
"""
        expected = """
<a class="bx--link" aria-disabled="true">Placeholder link</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_disabled_p(self):
        template = """
{% load carbondesign %}
{% Link tag="p" disabled=True %}Disabled Link{% endLink %}
"""
        expected = """
<p class="bx--link--disabled">Disabled Link</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default_example(self):
        template = """
{% load carbondesign %}
<div style="width:200px">
  {% Link href="#" %}Text wrap example for
    hover, focus, and active state testing.{% endLink %}
</div>
"""
        expected = """
<div style="width:200px">
  <a class="bx--link" href="#">Text wrap example for
    hover, focus, and active state testing.</a>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_inline(self):
        template = """
{% load carbondesign %}
{% Link href="#" inline=True %}Link{% endLink %}
"""
        expected = """
<a class="bx--link bx--link--inline" href="#">Link</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_inline_visited(self):
        template = """
{% load carbondesign %}
{% Link href="http://www.google.com" inline=True visited=True %}Link{% endLink %}
"""
        expected = """
<a class="bx--link bx--link--visited bx--link--inline" href="http://www.google.com">Link</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_inline_disabled(self):
        template = """
{% load carbondesign %}
{% Link inline=True disabled=True %}Placeholder link{% endLink %}
"""
        expected = """
<a class="bx--link bx--link--inline" aria-disabled="true">Placeholder link</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_inline_p_disabled(self):
        template = """
{% load carbondesign %}
{% Link tag="p" inline=True disabled=True %}Disabled Link{% endLink %}
"""
        expected = """
<p class="bx--link--disabled bx--link--inline">Disabled Link</p>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_inline_example(self):
        template = """
{% load carbondesign %}
<div style="width:200px">
  {% Link href="#" inline=True %}Text wrap example for
    hover, focus, and active state testing.{% endLink %}
</div>
"""
        expected = """
<div style="width:200px">
  <a class="bx--link bx--link--inline" href="#">Text wrap example for
    hover, focus, and active state testing.</a>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
