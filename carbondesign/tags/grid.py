"""Implements Carbon Design Component: Grid
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class Grid(Node):
    """Grid wrapper component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'bleed')
    "Available variants."
    NODE_PROPS = ('full_width', 'gap')
    "Extended Template Tag arguments."
    GAP_SIZES = ('narrow', 'condensed')
    "Grid gap sizes."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('full_width'), context):
            values['class'].append('bx--grid--full-width')

        gap = self.eval(self.kwargs.get('gap'), context)
        if gap in self.GAP_SIZES:
            values['class'].append('bx--grid--%s' % gap)


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = '<{tag} class="bx--grid {class}" {props}>{child}</{tag}>'
        return self.format(template, values)


    def render_bleed(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bleed">
  <{tag} class="bx--grid {class}" {props}>{child}</{tag}>
</div>
"""
        return self.format(template, values)


class Row(Node):
    """Grid Row component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = '<{tag} class="bx--row {class}" {props}>{child}</{tag}>'
        return self.format(template, values)


class Column(Node):
    """Grid columns.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    COL_SIZES = ('sm', 'md', 'lg', 'xlg', 'max')
    "Column sizes."
    NODE_PROPS = (*COL_SIZES, *['offset_%s' % x for x in COL_SIZES])
    "Extended Template Tag arguments."

    has_size = False

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        for size in self.COL_SIZES:
            width = self.eval(self.kwargs.get(size), context)
            if width:
                self.has_size = True
                values['class'].append('bx--col-%s-%s' % (size, width))

            width = self.eval(self.kwargs.get('offset_%s' % size), context)
            if width:
                values['class'].append('bx--offset-%s-%s' % (size, width))

        if not self.has_size:
            values['class'].append('bx--col')
            values['class'].append('bx--col--auto')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.has_size:
            template = """
<{tag} class="{class}" {props}>
  <div class="outside">
    <div class="inside">
      {child}
    </div>
  </div>
</{tag}>
"""
        else:
            template = '<{tag} class="{class}" {props}>{child}</{tag}>'
        return self.format(template, values)


class AspectRatio(Node):
    """Grid aspect ratio.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('ratio',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        ratio = self.eval(self.kwargs.get('ratio'), context)
        if ratio:
            values['class'].append('bx--aspect-ratio--%s' % ratio)


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{tag} class="bx--aspect-ratio {class}" {props}>
  <div class="bx--aspect-ratio--object">
    {child}
  </div>
</{tag}>
"""
        return self.format(template, values)


components = {
    'Grid': Grid,
    'Row': Row,
    'Col': Column,
    'AspectRatio': AspectRatio,
}
