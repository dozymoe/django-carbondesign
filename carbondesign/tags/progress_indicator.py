"""Implements Carbon Design Component: Progress Indicator
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
        if self.eval(self.kwargs.get('vertical'), context):
            values['class'].append('bx--progress--vertical')


    def render_default(self, values, context):
        template = """
<ul data-progress data-progress-current class="bx--progress {class}" {props}>
  {child}
</ul>
"""
        return self.format(template, values, context)


class ProgressIndicatorItem(Node):
    """Progress Indicator item component.
    """
    SLOTS = ('optional',)
    "Named children."
    MODES = ('default', 'completed', 'incomplete', 'invalid', 'disabled')
    "Available variants."

    def render_default(self, values, context):
        template = """
<li class="bx--progress-step bx--progress-step--current">
  <svg>
    <path d="M 7, 7 m -7, 0 a 7,7 0 1,0 14,0 a 7,7 0 1,0 -14,0"></path>
  </svg>
  <p tabindex="0" class="bx--progress-label {label_class}"
      aria-describedby="{id}" {label_props}>
    {label}
  </p>
  <div id="{id}" role="tooltip" data-floating-menu-direction="bottom"
      class="bx--tooltip" data-avoid-focus-on-open>
    <span class="bx--tooltip__caret"></span>
    <p class="bx--tooltip__text">{child}</p>
  </div>
  {slot_optional}
  <span class="bx--progress-line"></span>
</li>
"""
        return self.format(template, values)


    def render_completed(self, values, context):
        template = """
<li class="bx--progress-step bx--progress-step--complete">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
      height="16" viewBox="0 0 32 32" aria-hidden="true">
    <path d="M14 21.414L9 16.413 10.413 15 14 18.586 21.585 11 23 12.415 14 21.414z"></path>
    <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,26A12,12,0,1,1,28,16,12,12,0,0,1,16,28Z"></path>
  </svg>
  <p tabindex="0" class="bx--progress-label {label_class}"
      aria-describedby="{id}" {label_props}>
    {label}
  </p>
  <div id="{id}" role="tooltip" data-floating-menu-direction="bottom"
      class="bx--tooltip" data-avoid-focus-on-open>
    <span class="bx--tooltip__caret"></span>
    <p class="bx--tooltip__text">{child}</p>
  </div>
  {slot_optional}
  <span class="bx--progress-line"></span>
</li>
"""
        return self.format(template, values)


    def render_incomplete(self, values, context):
        template = """
<li class="bx--progress-step bx--progress-step--incomplete">
  <svg>
    <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
  </svg>
  <p tabindex="0" class="bx--progress-label {label_class}"
      aria-describedby="{id}" {label_props}>
    {label}
  </p>
  <div id="{id}" role="tooltip" data-floating-menu-direction="bottom"
      class="bx--tooltip" data-avoid-focus-on-open>
    <span class="bx--tooltip__caret"></span>
    <p class="bx--tooltip__text">{child}</p>
  </div>
  {slot_optional}
  <span class="bx--progress-line"></span>
</li>
"""
        return self.format(template, values)


    def render_invalid(self, values, context):
        template = """
<li class="bx--progress-step bx--progress-step--incomplete" data-invalid>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--progress__warning" width="16" height="16" viewBox="0 0 16 16"
      aria-hidden="true">
    <path d="M8,1C4.1,1,1,4.1,1,8s3.1,7,7,7s7-3.1,7-7S11.9,1,8,1z M8,14c-3.3,0-6-2.7-6-6s2.7-6,6-6s6,2.7,6,6S11.3,14,8,14z"></path>
    <path d="M7.5 4H8.5V9H7.5zM8 10.2c-.4 0-.8.3-.8.8s.3.8.8.8c.4 0 .8-.3.8-.8S8.4 10.2 8 10.2z"></path>
  </svg>
  <p tabindex="0" class="bx--progress-label {label_class}"
      aria-describedby="{id}" {label_props}>
    {label}
  </p>
  <div id="{id}" role="tooltip" data-floating-menu-direction="bottom"
      class="bx--tooltip" data-avoid-focus-on-open>
    <span class="bx--tooltip__caret"></span>
    <p class="bx--tooltip__text">{child}</p>
  </div>
  {slot_optional}
  <span class="bx--progress-line"></span>
</li>
"""
        return self.format(template, values)


    def render_disabled(self, values, context):
        template = """
<li class="bx--progress-step bx--progress-step--incomplete bx--progress-step--disabled"
    aria-disabled="true">
  <svg>
    <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
  </svg>
  <p tabindex="0" class="bx--progress-label {label_class}"
      aria-describedby="{id}" {label_props}>
    {label}
  </p>
  <div id="{id}" role="tooltip" data-floating-menu-direction="bottom"
      class="bx--tooltip" data-avoid-focus-on-open>
    <span class="bx--tooltip__caret"></span>
    <p class="bx--tooltip__text">{child}</p>
  </div>
  {slot_optional}
  <span class="bx--progress-line"></span>
</li>
"""
        return self.format(template, values)


    def render_slot_optional(self, values, context):
        template = """
<p class="bx--progress-optional {class}" {props}>{child}</p>
"""
        return self.format(template, values)


components = {
    'ProgressIndicator': ProgressIndicator,
    'Progress': ProgressIndicatorItem,
}
