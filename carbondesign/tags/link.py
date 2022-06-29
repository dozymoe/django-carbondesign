"""
Link
====

See: https://www.carbondesignsystem.com/components/link/usage/

Links are used as navigational elements. They may appear on their own, within
a sentence or paragraph, or directly following the content.

Overview
--------

Links are used as navigational elements and can be used on their own or inline
with text. They provide a lightweight option for navigation but like other
interactive elements, too many links will clutter a page and make it difficult
for users to identify their next steps. This is especially true for inline
links, which should be used sparingly.
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
    DEFAULT_TAG = 'a'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        is_a = values['astag'] == 'a'

        if is_a:
            values['class'].append('bx--link')

        if self.eval(self.kwargs.get('visited', False), context):
            values['class'].append('bx--link--visited')

        if self.eval(self.kwargs.get('disabled', False), context):
            if is_a:
                values['props'].append(('aria-disabled', 'true'))
            else:
                values['class'].append('bx--link--disabled')

        if self.eval(self.kwargs.get('inline', False), context):
            values['class'].append('bx--link--inline')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = '<{astag} class="{class}" {props}>{child}</{astag}>'
        return self.format(template, values)


components = {
    'Link': Link,
}
