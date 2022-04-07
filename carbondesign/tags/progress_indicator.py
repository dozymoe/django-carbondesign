"""
Progress Indicator
==================

See: https://www.carbondesignsystem.com/components/progress-indicator/usage/

A progress indicator is a visual representation of a user’s progress through
a set of steps, guiding toward the completion of a specified process.

Overview
--------

Use progress indicators to keep the user on track when completing a specific
task. By dividing the end goal into smaller, sub-tasks, it increases the
percentage of completeness as each task is completed.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class ProgressIndicator(Node):
    """Progress Indicator component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('vertical',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('vertical'), context):
            values['class'].append('bx--progress--vertical')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<ul data-progress data-progress-current class="bx--progress {class}" {props}>
  {child}
</ul>
"""
        return self.format(template, values, context)


class ProgressIndicatorItem(Node):
    """Progress Indicator item component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('help', 'optional')
    "Named children."
    NODE_PROPS = ('id', 'variant',)
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('list',)
    "Prepare xxx_class and xxx_props values."
    POSSIBLE_VARIANT = ('current', 'complete', 'incomplete', 'invalid',
            'disabled')
    "Documentation only."

    variant = None

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        self.variant = variant = self.eval(
                self.kwargs.get('variant', 'current'), context)

        if variant == 'invalid':
            values['list_class'].append('bx--progress-step--incomplete')
            values['list_props'].append(('data-invalid', True))
        else:
            values['list_class'].append(f'bx--progress-step--{variant}')

        if variant == 'disabled':
            values['list_class'].append('bx--progress-step--incomplete')
            values['list_props'].append(('aria-disabled', 'true'))

        if 'help' in self.slots:
            values['props'].append(('aria-describedby', f'hint-{self._id}'))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--progress-step {list_class}" {list_props}>
  {tmpl_icon}
  <p tabindex="0" class="bx--progress-label {class}" id="{id}" {props}>
    {child}
  </p>
  {slot_help}
  {slot_optional}
  <span class="bx--progress-line"></span>
</li>
"""
        return self.format(template, values, context)


    def render_slot_help(self, values, context):
        """Render html of the slot.
        """
        template = """
<div id="hint-{id}" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip {class}" data-avoid-focus-on-open {props}>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text">{child}</p>
</div>
"""
        return self.format(template, values)


    def render_slot_optional(self, values, context):
        """Render html of the slot.
        """
        template = """
<p class="bx--progress-optional {class}" {props}>{child}</p>
"""
        return self.format(template, values)


    def render_tmpl_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.variant == 'current':
            return """
<svg>
  <path d="M 7, 7 m -7, 0 a 7,7 0 1,0 14,0 a 7,7 0 1,0 -14,0"></path>
</svg>
"""
        if self.variant == 'complete':
            return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
    height="16" viewBox="0 0 32 32" aria-hidden="true">
  <path d="M14 21.414L9 16.413 10.413 15 14 18.586 21.585 11 23 12.415 14 21.414z"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,26A12,12,0,1,1,28,16,12,12,0,0,1,16,28Z"></path>
</svg>
"""
        if self.variant == 'incomplete':
            return """
<svg>
  <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
</svg>
"""
        if self.variant == 'invalid':
            return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--progress__warning" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.1,1,1,4.1,1,8s3.1,7,7,7s7-3.1,7-7S11.9,1,8,1z M8,14c-3.3,0-6-2.7-6-6s2.7-6,6-6s6,2.7,6,6S11.3,14,8,14z"></path>
  <path d="M7.5 4H8.5V9H7.5zM8 10.2c-.4 0-.8.3-.8.8s.3.8.8.8c.4 0 .8-.3.8-.8S8.4 10.2 8 10.2z"></path>
</svg>
"""
        if self.variant == 'disabled':
            return """
<svg>
  <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
</svg>
"""
        return ''


components = {
    'ProgressIndicator': ProgressIndicator,
    'Progress': ProgressIndicatorItem,
}
