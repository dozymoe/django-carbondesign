# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class ListHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_nesting(self):
        template = """
{% load carbondesign %}
{% List tag="ol" %}
  {% Li %}
    Ordered List level 1
    {% List %}
      {% Li %}Unordered List level 2{% endLi %}
      {% Li %}
        Unordered List level 2
        {% List tag="ol" %}
          {% Li %}Ordered List level 3{% endLi %}
          {% Li %}
            Ordered List level 3
            {% List %}
              {% Li %}
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
                venenatis aliquet odio ut viverra. Integer sollicitudin sed mi
                a finibus. Etiam massa ipsum, suscipit vitae nisl ut, semper
                euismod ante.
              {% endLi %}
              {% Li %}Unordered List level 4{% endLi %}
              {% Li %}Unordered List level 4{% endLi %}
            {% endList %}
          {% endLi %}
          {% Li %}Ordered List level 3{% endLi %}
        {% endList %}
      {% endLi %}
      {% Li %}Unordered List level 2{% endLi %}
    {% endList %}
  {% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
{% endList %}
<br>
{% List %}
  {% Li %}
    Unordered List level 1
    {% List tag="ol" %}
      {% Li %}Ordered List level 2{% endLi %}
      {% Li %}
        Ordered List level 2
        {% List %}
          {% Li %}Unordered List level 3{% endLi %}
          {% Li %}
            Unordered List level 3
            {% List tag="ol" %}
              {% Li %}
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
                venenatis aliquet odio ut viverra. Integer sollicitudin sed mi
                a finibus. Etiam massa ipsum, suscipit vitae nisl ut, semper
                euismod ante.
              {% endLi %}
              {% Li %}Ordered List level 4{% endLi %}
              {% Li %}Ordered List level 4{% endLi %}
            {% endList %}
          {% endLi %}
          {% Li %}Unordered List level 3{% endLi %}
        {% endList %}
      {% endLi %}
      {% Li %}Ordered List level 2{% endLi %}
    {% endList %}
  {% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
{% endList %}
"""
        expected = """
<ol class="bx--list--ordered">
<li class="bx--list__item">
    Ordered List level 1
<ul class="bx--list--unordered bx--list--nested">
<li class="bx--list__item">
  Unordered List level 2
</li>
<li class="bx--list__item">
        Unordered List level 2
<ol class="bx--list--ordered bx--list--nested">
<li class="bx--list__item">
  Ordered List level 3
</li>
<li class="bx--list__item">
            Ordered List level 3
<ul class="bx--list--unordered bx--list--nested">
<li class="bx--list__item">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
                venenatis aliquet odio ut viverra. Integer sollicitudin sed mi
                a finibus. Etiam massa ipsum, suscipit vitae nisl ut, semper
                euismod ante.
</li>
<li class="bx--list__item">
  Unordered List level 4
</li>
<li class="bx--list__item">
  Unordered List level 4
</li>
</ul>
</li>
<li class="bx--list__item">
  Ordered List level 3
</li>
</ol>
</li>
<li class="bx--list__item">
  Unordered List level 2
</li>
</ul>
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
</ol>
<br>
<ul class="bx--list--unordered">
<li class="bx--list__item">
    Unordered List level 1
<ol class="bx--list--ordered bx--list--nested">
<li class="bx--list__item">
  Ordered List level 2
</li>
<li class="bx--list__item">
        Ordered List level 2
<ul class="bx--list--unordered bx--list--nested">
<li class="bx--list__item">
  Unordered List level 3
</li>
<li class="bx--list__item">
            Unordered List level 3
<ol class="bx--list--ordered bx--list--nested">
<li class="bx--list__item">
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam
                venenatis aliquet odio ut viverra. Integer sollicitudin sed mi
                a finibus. Etiam massa ipsum, suscipit vitae nisl ut, semper
                euismod ante.
</li>
<li class="bx--list__item">
  Ordered List level 4
</li>
<li class="bx--list__item">
  Ordered List level 4
</li>
</ol>
</li>
<li class="bx--list__item">
  Unordered List level 3
</li>
</ul>
</li>
<li class="bx--list__item">
  Ordered List level 2
</li>
</ol>
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_ordered_native(self):
        template = """
{% load carbondesign %}
{% List tag="ol" native=True %}
  {% Li %}
    Ordered List level 1
    {% List tag="ol" native=True %}
      {% Li %}Ordered List level 2{% endLi %}
      {% Li %}Ordered List level 2{% endLi %}
      {% Li %}Ordered List level 2{% endLi %}
      {% Li %}Ordered List level 2{% endLi %}
    {% endList %}
  {% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
{% endList %}
"""
        expected = """
<ol class="bx--list--ordered--native">
<li class="bx--list__item">
    Ordered List level 1
<ol class="bx--list--ordered--native bx--list--nested">
<li class="bx--list__item">
  Ordered List level 2
</li>
<li class="bx--list__item">
  Ordered List level 2
</li>
<li class="bx--list__item">
  Ordered List level 2
</li>
<li class="bx--list__item">
  Ordered List level 2
</li>
</ol>
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
</ol>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_ordered(self):
        template = """
{% load carbondesign %}
{% List tag="ol" %}
  {% Li %}
    Ordered List level 1
    {% List tag="ol" %}
      {% Li %}Ordered List level 2{% endLi %}
      {% Li %}Ordered List level 2{% endLi %}
      {% Li %}Ordered List level 2{% endLi %}
      {% Li %}Ordered List level 2{% endLi %}
    {% endList %}
  {% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
  {% Li %}Ordered List level 1{% endLi %}
{% endList %}
"""
        expected = """
<ol class="bx--list--ordered">
<li class="bx--list__item">
    Ordered List level 1
<ol class="bx--list--ordered bx--list--nested">
<li class="bx--list__item">
  Ordered List level 2
</li>
<li class="bx--list__item">
  Ordered List level 2
</li>
<li class="bx--list__item">
  Ordered List level 2
</li>
<li class="bx--list__item">
  Ordered List level 2
</li>
</ol>
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
<li class="bx--list__item">
  Ordered List level 1
</li>
</ol>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_unordered(self):
        template = """
{% load carbondesign %}
{% List %}
  {% Li %}
    Unordered List level 1
    {% List %}
      {% Li %}Unordered List level 2{% endLi %}
      {% Li %}Unordered List level 2{% endLi %}
      {% Li %}Unordered List level 2{% endLi %}
      {% Li %}Unordered List level 2{% endLi %}
    {% endList %}
  {% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
  {% Li %}Unordered List level 1{% endLi %}
{% endList %}
"""
        expected = """
<ul class="bx--list--unordered">
<li class="bx--list__item">
    Unordered List level 1
<ul class="bx--list--unordered bx--list--nested">
<li class="bx--list__item">
  Unordered List level 2
</li>
<li class="bx--list__item">
  Unordered List level 2
</li>
<li class="bx--list__item">
  Unordered List level 2
</li>
<li class="bx--list__item">
  Unordered List level 2
</li>
</ul>
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
<li class="bx--list__item">
  Unordered List level 1
</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
