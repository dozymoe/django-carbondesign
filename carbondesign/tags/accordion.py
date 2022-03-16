"""Implements Carbon Design Component: Accordion
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class Accordion(Node):
    """Accordion component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{tag} data-accordion class="bx--accordion {class}" {props}>
  {child}
</{tag}>
"""
        return self.format(template, values)


class AccordionItem(Node):
    """Accordion item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('expanded',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'li'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('expanded', False), context):
            values['expanded'] = 'true'
            values['class'].append('bx--accordion__item--active')
        else:
            values['expanded'] = 'false'


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{tag} data-accordion-item class="bx--accordion__item {class}" {props}>
  <button class="bx--accordion__heading" aria-expanded="{expanded}"
      aria-controls="pane-{id}">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
    <div class="bx--accordion__title {label_class}" {label_props}>
      {label}
    </div>
  </button>
  <div id="pane-{id}" class="bx--accordion__content">
    {child}
  </div>
</{tag}>
"""
        return self.format(template, values)


components = {
    'Accordion': Accordion,
    'AccordionItem': AccordionItem,
}
