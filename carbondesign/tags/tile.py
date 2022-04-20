"""
Tile
====

See: https://www.carbondesignsystem.com/components/tile/usage/

Tiles are a highly flexible component for displaying a wide variety of
content, including information, getting started, how-to, next steps, and more.

Overview
--------

Carbon ships a basic tile structure that responds to the grid. Based on the
layout structure, tiles can contain type, images and/or a block of color.
As tiles have no pre-set styles for the content within them, the tile
component usage guidance is purposefully high-level. It focuses specifically
on the tile itself, not the structure of the information or interactive
elements that the tile contains—that type of information will be found in
the card pattern.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import ChoiceFormNode, Node

class Tile(Node):
    """Tile component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('above', 'icon')
    "Named children."
    MODES = ('default', 'clickable', 'expandable')
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


    def render_expandable(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-tile="expandable" class="bx--tile bx--tile--expandable {class}"
    tabindex="0" {props}>
  <button aria-label="expand menu" class="bx--tile__chevron">
    {tmpl_icon}
  </button>
  <div class="bx--tile-content">
    {slot_above}
    <span class="bx--tile-content__below-the-fold">
      {child}
    </span>
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_slot_above(self, values, context):
        """Render html of the slot.
        """
        template = """
<span data-tile-atf class="bx--tile-content__above-the-fold {class}" {props}>
  {child}
</span>
"""
        return self.format(template, values)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if 'icon' in self.slots:
            return self.format('{slot_icon}', values, context)
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
    height="16" viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
</svg>
"""


class TileSelectable(ChoiceFormNode):
    """Tile selectable component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'inside')
    "Available variants."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['label']:
            label = values['label'] + values['label_suffix']
            values['props'].append(('title', label))
            values['label_props'].append(('aria-label', label))


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['tabindex'] = '-1'
        props['data-tile-input'] = True
        props['class'].append('bx--tile-input')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
{tmpl_element}
<label for="{id}" class="bx--tile bx--tile--selectable {label_class}"
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
        return self.format(template, values, context)


    def render_inside(self, values, context):
        """Output html of the component.
        """
        template = """
<label class="bx--tile bx--tile--selectable {label_class}"
    data-tile="selectable" tabindex="0" {label_props}>
  {tmpl_element}
  <div class="bx--tile__checkmark">
    <svg width="16" height="16" viewBox="0 0 16 16">
      <path d="M8 16A8 8 0 1 1 8 0a8 8 0 0 1 0 16zm3.646-10.854L6.75 10.043 4.354 7.646l-.708.708 3.104 3.103 5.604-5.603-.708-.708z"
        fill-rule="evenodd" />
    </svg>
  </div>
  <div class="bx--tile-content">
    {child}
  </div>
</label>
"""
        return self.format(template, values, context)


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
    'TileSelect': TileSelectable,
    'TileGrid': TileGrid,
}
