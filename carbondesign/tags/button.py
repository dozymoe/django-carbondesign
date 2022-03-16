"""Implements Carbon Design Component: Button
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node, modify_svg

class Button(Node):
    """Button component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."
    NODE_PROPS = ('disabled', 'variant', 'icon_only', 'field', 'small',
            'icon_size')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    CATCH_PROPS = ('button_props',)

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        variant = self.eval(self.kwargs.get('variant', 'primary'), context)
        values['class'].append(f'bx--btn--{variant}')

        if self.eval(self.kwargs.get('disabled'), context):
            values['props'].append(('disabled', 'disabled'))

        if self.eval(self.kwargs.get('icon_only'), context):
            values['class'].extend([
                    'bx--btn--icon-only',
                    'bx--tooltip__trigger',
                    'bx--tooltip--a11y',
                    'bx--tooltip--bottom',
                    'bx--tooltip--align-center'])

        if self.eval(self.kwargs.get('field'), context):
            values['class'].append('bx--btn--field')

        if self.eval(self.kwargs.get('small'), context):
            values['class'].append('bx--btn--sm')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.eval(self.kwargs.get('icon_only'), context):
            template = """
<{tag} class="bx--btn {class}" {props}>
  <span class="bx--assistive-text">{child}</span>
  {slot_icon}
</{tag}>
"""
        else:
            template = """
<{tag} class="bx--btn {class}" {props}>
  {child}
  {slot_icon}
</{tag}>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        size = self.eval(self.kwargs.get('icon_size', 16), context)
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'style': {
                'will-change': 'transform',
                'width': size,
                'height': size,
            },
            'aria-hidden': 'true',
            'class': 'bx--btn__icon ' + values['class'],
        })


class ButtonSet(Node):
    """Button set component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{tag} class="bx--btn-set {class}" {props}>
  {child}
</{tag}>
"""
        return self.format(template, values)


components = {
    'Button': Button,
    'ButtonSet': ButtonSet,
}
