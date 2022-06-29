"""
Breadcrumb
==========

See: https://www.carbondesignsystem.com/components/breadcrumb/usage/

The breadcrumb is a secondary navigation pattern that helps a user understand
the hierarchy among levels and navigate back through them.

Overview
--------

Breadcrumbs show users their current location relative to the information
architecture and enable them to quickly move up to a parent level or previous
step.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class Breadcrumb(Node):
    """Breadcrumb component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('current',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'nav'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_breadcrumb'] = _("breadcrumb")

        if self.eval(self.kwargs.get('current', False), context):
            values['class'].append('bx--breadcrumb--no-trailing-slash')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--breadcrumb {class}" aria-label="{txt_breadcrumb}" {props}>
  {child}
</{astag}>
"""
        return self.format(template, values)


class BreadcrumbItem(Node):
    """Breadcrumb item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('href', 'current')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('wrapper',)
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['href'] = self.eval(self.kwargs.get('href', '#'), context)

        if self.eval(self.kwargs.get('current', False), context):
            values['wrapper_class'].append('bx--breadcrumb-item--current')
            values['props'].append(('aria-current', 'page'))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--breadcrumb-item {wrapper_class}" {wrapper_props}>
  <a href="{href}" class="bx--link {class}" {props}>
    {child}
  </a>
</{astag}>
"""
        return self.format(template, values)


components = {
    'Breadcrumb': Breadcrumb,
    'BreadcrumbItem': BreadcrumbItem,
}
