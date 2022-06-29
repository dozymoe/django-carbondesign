"""
Accordion
=========

See: https://www.carbondesignsystem.com/components/accordion/usage/

An accordion is a vertically stacked list of headers that reveal or hide
associated sections of content.

Overview
--------

The accordion component delivers large amounts of content in a small space
through progressive disclosure. The header title give the user a high level
overview of the content allowing the user to decide which sections to read.

Accordions can make information processing and discovering more effective.
However, it does hide content from users and it’s important to account for
a user not noticing or reading all of the included content. If a user is
likely to read all of the content then don’t use an accordion as it adds
the burden of an extra click; instead use a full scrolling page with normal
headers.
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
<{astag} data-accordion class="bx--accordion {class}" {props}>
  {child}
</{astag}>
"""
        return self.format(template, values)


class AccordionItem(Node):
    """Accordion item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('id', 'expanded')
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
<{astag} data-accordion-item class="bx--accordion__item {class}" {props}>
  <button class="bx--accordion__heading" aria-expanded="{expanded}"
      aria-controls="{id}">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--accordion__arrow" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
    {tmpl_label}
  </button>
  <div id="{id}" class="bx--accordion__content">
    {child}
  </div>
</{astag}>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''
        template = """
<div class="bx--accordion__title">
  {label}{label_suffix}
</div>
"""
        return self.format(template, values)


components = {
    'Accordion': Accordion,
    'AccordionItem': AccordionItem,
}
