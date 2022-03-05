"""Implements Carbon Design Component: List
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class List(Node):
    """List component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."


    def prepare(self, values, context):
        if values['tag'] == 'ul':
            values['class'].append('bx--list--unordered')
        else:
            values['class'].append('bx--list--ordered')

        if context.get('list_nested'):
            values['class'].append('bx--list--nested')
        else:
            context['list_nested'] = True


    def render_default(self, values, context):
        template = """
<{tag} class="{class}" {props}>
  {child}
</{tag}>
"""
        return self.format(template, values)


class ListItem(Node):
    """List item component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ()
    "Extended Template Tag arguments."

    def render_default(self, values, context):
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
