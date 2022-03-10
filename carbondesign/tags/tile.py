"""Implements Carbon Design Component: Tile
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class Tile(Node):
    """Tile component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('above',)
    "Named children."
    MODES = ('default', 'clickable', 'selectable', 'expandable')
    "Available variants."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_tile'] = _("tile")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--tile {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


    def render_clickable(self, values, context):
        """Output html of the component.
        """
        template = """
<a data-tile="clickable" class="bx--tile bx--tile--clickable {class}"
    tabindex="0" {props}>
  {child}
</a>
"""
        return self.format(template, values)


    def render_selectable(self, values, context):
        """Output html of the component.
        """
        template = """
<input tabindex="-1" data-tile-input id="{id}" class="bx--tile-input {class}"
    type="checkbox" {props}/>
<label for="{id}" aria-label="{label}"
    class="bx--tile bx--tile--selectable {label_class}"
    data-tile="selectable" tabindex="0" {label_props}>
  <div class="bx--tile__checkmark">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
  </div>
  <div class="bx--tile-content">
    {child}
  </div>
</label>
"""
        return self.format(template, values)


    def render_expandable(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-tile="expandable" class="bx--tile bx--tile--expandable {class}"
    tabindex="0" {props}>
  <button aria-label="expand menu" class="bx--tile__chevron">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
    </svg>
  </button>
  <div class="bx--tile-content">
    <span data-tile-atf class="bx--tile-content__above-the-fold">
      {slot_above}
    </span>
    <span class="bx--tile-content__below-the-fold">
      {child}
    </span>
  </div>
</div>
"""
        return self.format(template, values)


class TileGrid(Node):
    """Tile grid.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--grid {class}" {props}>
  <div class="bx--tile-container" style="width: 100%">
    {child}
  </div>
</div>
"""
        return self.format(template, values)


components = {
    'Tile': Tile,
    'TileGrid': TileGrid,
}
