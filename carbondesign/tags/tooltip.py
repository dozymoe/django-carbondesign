"""
Tooltip
=======

See: https://www.carbondesignsystem.com/components/tooltip/usage/

Tooltips display additional information upon click, hover, or focus. The
information should be contextual, useful, and nonessential.

Overview
--------

A tooltip is a message box that is displayed when a user hovers over, clicks
or gives focus to a UI element such as an icon, a highlighted word, or a button.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node, modify_svg

class Tooltip(Node):
    """Tooltip component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon', 'footer')
    "Named children."
    MODES = ('interactive', 'definition', 'icon')
    "Available variants."
    NODE_PROPS = ('id', 'align', 'position')
    "Extended Template Tag arguments."
    REQUIRED_PROPS = ('label',)
    "Will raise Exception if not set."
    CLASS_AND_PROPS = ('label',)
    "Prepare xxx_class and xxx_props values."
    POSSIBLE_ALIGN = ('start', 'center', 'end')
    "Documentation only."
    POSSIBLE_POSITION = ('top', 'right', 'bottom', 'left')
    "Documentation only."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['label'] = self.eval(self.kwargs['label'], context)

        align = self.eval(self.kwargs.get('align'), context)
        if align and align in self.POSSIBLE_ALIGN:
            values['class'].append(f'bx--tooltip--align-{align}')

        position = self.eval(self.kwargs.get('position'), context)
        if position and position in self.POSSIBLE_POSITION:
            values['class'].append(f'bx--tooltip--{position}')


    def render_interactive(self, values, context):
        """Output html of the component.
        """
        template = """
<div id="label-{id}" class="bx--tooltip__label">
  {label}
  <button aria-expanded="false" aria-labelledby="label-{id}"
      data-tooltip-trigger data-tooltip-target="#{id}"
      class="bx--tooltip__trigger {class}" aria-controls="{id}" {props}>
    {slot_icon}
  </button>
</div>
<div id="{id}" aria-hidden="true" data-floating-menu-direction="bottom"
    class="bx--tooltip">
  <span class="bx--tooltip__caret"></span>
  <div class="bx--tooltip__content" tabindex="-1" role="dialog"
      aria-describedby="body-{id}" aria-labelledby="label-{id}">
    <div id="body-{id}">{child}</div>
    {slot_footer}
  </div>
  <span tabindex="0"></span>
</div>
"""
        return self.format(template, values, context)


    def render_definition(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--tooltip--definition bx--tooltip--a11y" data-tooltip-definition>
  <button aria-describedby="{id}"
      class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip__trigger--definition {class}"
      {props}>
    {label}
  </button>
  <div class="bx--assistive-text" id="{id}" role="tooltip">
    {child}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_icon(self, values, context):
        """Output html of the component.
        """
        template = """
<button class="bx--tooltip__trigger bx--tooltip--a11y {class}"
    data-tooltip-icon {props}>
  <span class="bx--assistive-text">{child}</span>
  {slot_icon}
</button>
"""
        return self.format(template, values)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': 16,
                'height': 16,
            },
            'aria-hidden': 'true',
        })


    def render_slot_footer(self, values, context):
        """Render html of the slot.
        """
        template = """
<div class="bx--tooltip__footer {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


class TooltipHeading(Node):
    """Tooltip heading.
    """
    WANT_CHILDREN = True
    DEFAULT_TAG = 'h4'

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{tag} class="bx--tooltip__heading {class}" {props}>
  {child}
</{tag}>
"""
        return self.format(template, values)


components = {
    'Tooltip': Tooltip,
    'TooltipHeading': TooltipHeading,
}
