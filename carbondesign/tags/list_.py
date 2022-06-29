"""
List
====

See: https://www.carbondesignsystem.com/components/list/usage/

Lists are vertical groupings of related content. List items begin with either
a number or a bullet.

Overview
--------

Lists consist of related content grouped together and organized vertically.

Use bulleted lists when you don’t need to convey a specific order for list
items.

Use numbered lists when you need to convey a priority, hierarchy, or sequence
between list items.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class List(Node):
    """List component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('native',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['astag'] == 'ul':
            values['class'].append('bx--list--unordered')
        elif self.eval(self.kwargs.get('native'), context):
            values['class'].append('bx--list--ordered--native')
        else:
            values['class'].append('bx--list--ordered')

        if context.get('list_nested'):
            values['class'].append('bx--list--nested')
        context['list_nested'] = True


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="{class}" {props}>
  {child}
</{astag}>
"""
        return self.format(template, values)


class ListItem(Node):
    """List item component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--list__item {class}" {props}>
  {child}
</li>
"""
        return self.format(template, values)


components = {
    'List': List,
    'Li': ListItem,
}
