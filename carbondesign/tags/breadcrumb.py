"""Implements Carbon Design Component: Breadcrumb
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
<{tag} class="bx--breadcrumb {class}" aria-label="{txt_breadcrumb}" {props}>
  {child}
</{tag}>
"""
        return self.format(template, values)


class BreadcrumbItem(Node):
    """Breadcrumb item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('href', 'current',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('current', False), context):
            values['props'].append(('aria-current', 'page'))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{tag} class="bx--breadcrumb-item {class}" {props}>
  <a href="{href}" class="bx--link">
    {child}
  </a>
</{tag}>
"""
        return self.format(template, values)


components = {
    'Breadcrumb': Breadcrumb,
    'BreadcrumbItem': BreadcrumbItem,
}
