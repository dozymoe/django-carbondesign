"""Implements Carbon Design Component: Button
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

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

    def prepare(self, values, context):
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

        values['icon_size'] = self.eval(self.kwargs.get('icon_size', 16),
                context)


    def render_default(self, values, context):
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
        template = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
    class="bx--btn__icon {class}" width="{icon_size}" height="{icon_size}"
    viewBox="0 0 {icon_size} {icon_size}"
    aria-hidden="true" {props}>
  {child}
</svg>
"""
        return self.format(template, values)


class ButtonSet(Node):
    """Button set component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
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
