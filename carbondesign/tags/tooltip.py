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

class BaseTooltip(Node):
    """Base tooltip.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('id', 'align', 'position')
    "Extended Template Tag arguments."
    POSSIBLE_ALIGN = ('start', 'center', 'end')
    "Documentation only."
    POSSIBLE_POSITION = ('top', 'right', 'bottom', 'left')
    "Documentation only."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        align = self.eval(self.kwargs.get('align'), context)
        if align and align in self.POSSIBLE_ALIGN:
            values['class'].append(f'bx--tooltip--align-{align}')

        position = self.eval(self.kwargs.get('position'), context)
        if position and position in self.POSSIBLE_POSITION:
            values['class'].append(f'bx--tooltip--{position}')


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '%spx' % 16,
                'height': '%spx' % 16,
            },
            'aria-hidden': 'true',
        })


class Interactive(BaseTooltip):
    """Tooltip component.
    """
    SLOTS = ('icon', 'footer', 'heading')
    "Named children."
    MODES = ('interactive', 'nolabel')
    "Available variants."
    REQUIRED_PROPS = ('label',)
    "Will raise Exception if not set."
    CLASS_AND_PROPS = ('label', 'content')
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if 'heading' in self.slots:
            values['content_props'].append(
                    ('aria-labelledby', 'heading-' + self._id))
        elif self.mode == 'nolabel':
            values['content_props'].append(('aria-label',
                    values['label'] + values['label_suffix']))
        else:
            values['content_props'].append(
                    ('aria-labelledby', 'label-' + self._id))


    def render_interactive(self, values, context):
        """Output html of the component.
        """
        template = """
<div id="label-{id}" class="bx--tooltip__label">
  {label}{label_suffix}
  <button aria-expanded="false" aria-labelledby="label-{id}"
      data-tooltip-trigger data-tooltip-target="#{id}"
      class="bx--tooltip__trigger {class}" aria-controls="{id}" {props}>
    {slot_icon}
  </button>
</div>
<div id="{id}" aria-hidden="true" data-floating-menu-direction="bottom"
    class="bx--tooltip">
  <span class="bx--tooltip__caret"></span>
  <div class="bx--tooltip__content {content_class}" tabindex="-1" role="dialog"
      aria-describedby="body-{id}" {content_props}>
    {slot_heading}
    <p id="body-{id}">{child}</p>
    {slot_footer}
  </div>
  <span tabindex="0"></span>
</div>
"""
        return self.format(template, values, context)


    def render_nolabel(self, values, context):
        """Output html of the component.
        """
        template = """
<div id="label-{id}" class="bx--tooltip__label">
  {label}{label_suffix}
  <div tabindex="0" aria-expanded="false" aria-labelledby="label-{id}"
      data-tooltip-trigger data-tooltip-target="#{id}"
      role="button" class="bx--tooltip__trigger {class}" aria-controls="{id}" {props}>
    {slot_icon}
  </div>
</div>
<div id="{id}" aria-hidden="true" data-floating-menu-direction="bottom"
    class="bx--tooltip">
  <span class="bx--tooltip__caret"></span>
  <div class="bx--tooltip__content {content_class}" tabindex="-1" role="dialog"
      aria-describedby="body-{id}" {content_props}>
    {slot_heading}
    <p id="body-{id}">{child}</p>
    {slot_footer}
  </div>
  <span tabindex="0"></span>
</div>
"""
        return self.format(template, values, context)


    def render_slot_heading(self, values, context):
        """Render html of the slot.
        """
        template = """
<h4 id="heading-{id}" class="bx--tooltip__heading {class}" {props}>{child}</h4>
"""
        return self.format(template, values)


    def render_slot_footer(self, values, context):
        """Render html of the slot.
        """
        template = """
<div class="bx--tooltip__footer {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


class Definition(BaseTooltip):
    """Tooltip component.
    """
    REQUIRED_PROPS = ('label',)
    "Will raise Exception if not set."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--tooltip--definition bx--tooltip--a11y" data-tooltip-definition>
  <button aria-describedby="{id}"
      class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip__trigger--definition {class}"
      {props}>
    {label}{label_suffix}
  </button>
  <div class="bx--assistive-text" id="{id}" role="tooltip">
    {child}
  </div>
</div>
"""
        return self.format(template, values)


class Icon(BaseTooltip):
    """Tooltip component.
    """
    SLOTS = ('icon',)
    "Named children."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<button class="bx--tooltip__trigger bx--tooltip--a11y {class}"
    data-tooltip-icon {props}>
  <span class="bx--assistive-text">{child}</span>
  {slot_icon}
</button>
"""
        return self.format(template, values, context)


components = {
    'InteractiveTooltip': Interactive,
    'DefinitionTooltip': Definition,
    'IconTooltip': Icon,
}
