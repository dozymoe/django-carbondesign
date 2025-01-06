# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long
from django import forms
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    tiles = forms.ChoiceField(required=False,
            label="Number input label",
            choices=(
                ('tile', "tile"),
                ('tile-2', "tile-2"),
            ))


class TileHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Tile %}{% endTile %}
"""
        expected = """
<div class="bx--tile">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_clickable(self):
        template = """
{% load carbondesign %}
{% Tile mode="clickable" %}{% endTile %}
"""
        expected = """
<a data-tile="clickable" class="bx--tile bx--tile--clickable"
    tabindex="0">
</a>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_expandable(self):
        template = """
{% load carbondesign %}
{% Tile mode="expandable" %}
  {% Slot 'above' %}
    <!-- Above the fold content here -->
  {% endSlot %}

  <!-- Rest of the content here -->
{% endTile %}
"""
        expected = """
<div data-tile="expandable" class="bx--tile bx--tile--expandable"
    tabindex="0">
  <button aria-label="expand menu" class="bx--tile__chevron">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
    height="16" viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
</svg>
  </button>
  <div class="bx--tile-content">
<span data-tile-atf class="bx--tile-content__above-the-fold">
    <!-- Above the fold content here -->
</span>
    <span class="bx--tile-content__below-the-fold">
  <!-- Rest of the content here -->
    </span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_selectable(self):
        form = DummyForm(data={'tiles': ''})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TileSelect form.tiles value="tile" id="tile-id" %}
  <!-- Tile content here -->
{% endTileSelect %}
"""
        expected = """
<input type="checkbox" name="tiles" value="tile" id="tile-id" title="tile" class="bx--tile-input" tabindex="-1" data-tile-input aria-invalid="true">
<label for="tile-id" class="bx--tile bx--tile--selectable"
    data-tile="selectable" tabindex="0" aria-label="tile">
  <div class="bx--tile__checkmark">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
  </div>
  <div class="bx--tile-content">
  <!-- Tile content here -->
  </div>
</label>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def atest_grid(self):
        form = DummyForm(data={'tiles': ''})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% TileGrid %}
  {% Row %}
    {% Col md=12 %}
      {% Tile mode="expandable" %}
        {% Slot 'above' style="height: 200px" %}
          <!-- Above the fold content here -->
          <h2>Above the fold content here</h2>
        {% endSlot %}

        <!-- Rest of the content here -->
        <h2>Below the fold content here</h2>

        {% Slot 'icon' %}
          <svg width="12" height="7" viewBox="0 0 12 7">
            <path fill-rule="nonzero" d="M6.002 5.55L11.27 0l.726.685L6.003 7 0 .685.726 0z" />
          </svg>
        {% endSlot %}
      {% endTile %}
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col sm=2 %}
      {% TileSelect form.tiles mode="inside" value="tile" id="tile-id-1" %}
        <!-- Tile content here -->
      {% endTileSelect %}
    {% endCol %}
    {% Col sm=2 %}
      {% TileSelect form.tiles mode="inside" value="tile-2" id="tile-id-2" %}
        <!-- Tile content here -->
      {% endTileSelect %}
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col md=4 sm=4 %}
      {% Tile mode="clickable" %}{% endTile %}
    {% endCol %}
    {% Col md=4 sm=4 %}
      {% Tile mode="clickable" %}{% endTile %}
    {% endCol %}
    {% Col md=4 sm=4 %}
      {% Tile mode="clickable" %}{% endTile %}
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col md=4 sm=4 %}
      {% Tile %}{% endTile %}
    {% endCol %}
    {% Col md=4 sm=4 %}
      {% Tile %}{% endTile %}
    {% endCol %}
    {% Col md=4 sm=4 %}
      {% Tile %}{% endTile %}
    {% endCol %}
    {% Col md=4 sm=4 %}
      {% Tile %}{% endTile %}
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col lg=4 md=8 %}
      {% Tile %}{% endTile %}
    {% endCol %}
    {% Col lg=4 md=8 %}
      {% Tile %}{% endTile %}
    {% endCol %}
    {% Col lg=4 md=8 %}
      {% Tile %}{% endTile %}
    {% endCol %}
    {% Col lg=4 md=8 %}
      {% Tile %}{% endTile %}
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col lg=16 %}
      {% Tile %}{% endTile %}
    {% endCol %}
  {% endRow %}
  {% Row %}
    {% Col md=5 sm=2 %}
      {% Tile %}{% endTile %}
    {% endCol %}
    {% Col md=3 sm=2 %}
      {% Tile %}{% endTile %}
    {% endCol %}
  {% endRow %}
{% endTileGrid %}
"""
        expected = """
<div class="bx--grid">
  <div class="bx--tile-container" style="width: 100%">
  <div class="bx--row">
    <div class="bx--col-md-12">
      <div class="outside">
        <div class="inside">
<div data-tile="expandable" class="bx--tile bx--tile--expandable"
    tabindex="0">
  <button aria-label="expand menu" class="bx--tile__chevron">
          <svg width="12" height="7" viewBox="0 0 12 7">
            <path fill-rule="nonzero" d="M6.002 5.55L11.27 0l.726.685L6.003 7 0 .685.726 0z" />
          </svg>
  </button>
  <div class="bx--tile-content">
<span data-tile-atf class="bx--tile-content__above-the-fold" style="height: 200px">
          <!-- Above the fold content here -->
          <h2>Above the fold content here</h2>
</span>
    <span class="bx--tile-content__below-the-fold">
        <!-- Rest of the content here -->
        <h2>Below the fold content here</h2>
    </span>
  </div>
</div>
        </div>
      </div>
    </div>
  </div>
  <div class="bx--row">
    <div class="bx--col-sm-2">
      <div class="outside">
        <div class="inside">
<label class="bx--tile bx--tile--selectable"
    data-tile="selectable" tabindex="0" aria-label="tile">
  <input type="checkbox" name="tiles" value="tile" id="tile-id-1" title="tile" class="bx--tile-input" tabindex="-1" data-tile-input aria-invalid="true">
  <div class="bx--tile__checkmark">
    <svg width="16" height="16" viewBox="0 0 16 16">
      <path d="M8 16A8 8 0 1 1 8 0a8 8 0 0 1 0 16zm3.646-10.854L6.75 10.043 4.354 7.646l-.708.708 3.104 3.103 5.604-5.603-.708-.708z"
        fill-rule="evenodd" />
    </svg>
  </div>
  <div class="bx--tile-content">
        <!-- Tile content here -->
  </div>
</label>
        </div>
      </div>
    </div>
    <div class="bx--col-sm-2">
      <div class="outside">
        <div class="inside">
<label class="bx--tile bx--tile--selectable"
    data-tile="selectable" tabindex="0" aria-label="tile-2">
  <input type="checkbox" name="tiles" value="tile-2" id="tile-id-2" title="tile-2" class="bx--tile-input" tabindex="-1" data-tile-input aria-invalid="true">
  <div class="bx--tile__checkmark">
    <svg width="16" height="16" viewBox="0 0 16 16">
      <path d="M8 16A8 8 0 1 1 8 0a8 8 0 0 1 0 16zm3.646-10.854L6.75 10.043 4.354 7.646l-.708.708 3.104 3.103 5.604-5.603-.708-.708z"
        fill-rule="evenodd" />
    </svg>
  </div>
  <div class="bx--tile-content">
        <!-- Tile content here -->
  </div>
</label>
        </div>
      </div>
    </div>
  </div>
  <div class="bx--row">
    <div class="bx--col-sm-4 bx--col-md-4">
      <div class="outside">
        <div class="inside">
<a data-tile="clickable" class="bx--tile bx--tile--clickable"
    tabindex="0">
</a>
        </div>
      </div>
    </div>
    <div class="bx--col-sm-4 bx--col-md-4">
      <div class="outside">
        <div class="inside">
<a data-tile="clickable" class="bx--tile bx--tile--clickable"
    tabindex="0">
</a>
        </div>
      </div>
    </div>
    <div class="bx--col-sm-4 bx--col-md-4">
      <div class="outside">
        <div class="inside">
<a data-tile="clickable" class="bx--tile bx--tile--clickable"
    tabindex="0">
</a>
        </div>
      </div>
    </div>
  </div>
  <div class="bx--row">
    <div class="bx--col-sm-4 bx--col-md-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
    <div class="bx--col-sm-4 bx--col-md-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
    <div class="bx--col-sm-4 bx--col-md-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
    <div class="bx--col-sm-4 bx--col-md-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
  </div>
  <div class="bx--row">
    <div class="bx--col-md-8 bx--col-lg-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
    <div class="bx--col-md-8 bx--col-lg-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
    <div class="bx--col-md-8 bx--col-lg-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
    <div class="bx--col-md-8 bx--col-lg-4">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
  </div>
  <div class="bx--row">
    <div class="bx--col-lg-16">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
  </div>
  <div class="bx--row">
    <div class="bx--col-sm-2 bx--col-md-5">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
    <div class="bx--col-sm-2 bx--col-md-3">
      <div class="outside">
        <div class="inside">
<div class="bx--tile">
</div>
        </div>
      </div>
    </div>
  </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
