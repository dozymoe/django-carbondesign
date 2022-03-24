# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class GridHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% Grid %}
  {% Row %}
    {% Col %}
      <p>Small (4 columns @ 320px)</p>
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col sm=1 %}1{% endCol %}
    {% Col sm=1 %}1{% endCol %}
    {% Col sm=1 %}1{% endCol %}
    {% Col sm=1 %}1{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col %}
      <p>Medium (8 columns @ 672px)</p>
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col md=1 %}1{% endCol %}
    {% Col md=1 %}1{% endCol %}
    {% Col md=1 %}1{% endCol %}
    {% Col md=1 %}1{% endCol %}
    {% Col md=1 %}1{% endCol %}
    {% Col md=1 %}1{% endCol %}
    {% Col md=1 %}1{% endCol %}
    {% Col md=1 %}1{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col %}
      <p>Large (12 columns @ 1312px)</p>
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
    {% Col lg=1 %}1{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col %}
      <p>X-Large (12 columns @ 1312px)</p>
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
    {% Col xlg=1 %}1{% endCol %}
  {% endRow %}
  {% Row %}
    {% Col %}
      <p>Max (12 columns @ 1584px)</p>
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
    {% Col max=1 %}1{% endCol %}
  {% endRow %}
{% endGrid %}
"""
        expected = """
<div class="bx--grid">
  <div class="bx--row">
    <div class="bx--col bx--col--auto">
      <p>Small (4 columns @ 320px)</p>
    </div>
  </div>
  <div class="bx--row">
<div class="bx--col-sm-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-sm-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-sm-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-sm-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
  </div>
  <div class="bx--row">
    <div class="bx--col bx--col--auto">
      <p>Medium (8 columns @ 672px)</p>
    </div>
  </div>
  <div class="bx--row">
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-md-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
  </div>
  <div class="bx--row">
    <div class="bx--col bx--col--auto">
      <p>Large (12 columns @ 1312px)</p>
    </div>
  </div>
  <div class="bx--row">
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-lg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
  </div>
  <div class="bx--row">
    <div class="bx--col bx--col--auto">
      <p>X-Large (12 columns @ 1312px)</p>
    </div>
  </div>
  <div class="bx--row">
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-xlg-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
  </div>
  <div class="bx--row">
    <div class="bx--col bx--col--auto">
      <p>Max (12 columns @ 1584px)</p>
    </div>
  </div>
  <div class="bx--row">
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
<div class="bx--col-max-1">
  <div class="outside">
    <div class="inside">
      1
    </div>
  </div>
</div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
