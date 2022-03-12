"""Implements Carbon Design Component: Link
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class Link(Node):
    """Link component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('visited', 'disabled', 'inline')
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('visited', False), context):
            values['class'].append('bx--link--visited')

        if self.eval(self.kwargs.get('disabled', False), context):
            values['class'].append('bx--link--disabled')
            values['props'].append(('aria-disabled', 'true'))

        if self.eval(self.kwargs.get('inline', False), context):
            values['class'].append('bx--link--inline')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<a class="bx--link {class}" {props}>
  {child}
</a>
"""
        return self.format(template, values)


components = {
    'Link': Link,
}
