"""
Button
======

See: https://www.carbondesignsystem.com/components/button/usage/

Buttons are used to initialize an action. Button labels express what action
will occur when the user interacts with it.

Overview
--------

Buttons are clickable elements that are used to trigger actions. They
communicate calls to action to the user and allow users to interact with pages
in a variety of ways. Button labels express what action will occur when
the user interacts with it.
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
    NODE_PROPS = ('disabled', 'variant', 'field', 'small', 'icon_size')
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
            if context.get('button_set'):
                values['class'].append('bx--btn--disabled')

        if self.eval(self.kwargs.get('field'), context):
            values['class'].append('bx--btn--field')

        if self.eval(self.kwargs.get('small'), context):
            values['class'].append('bx--btn--sm')

        if values['label']:
            values['props'].append(('aria-label',
                    values['label'] + values['label_suffix']))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--btn {class}" {props}>
  {child}
  {slot_icon}
</{astag}>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        size = self.eval(self.kwargs.get('icon_size', 16), context)
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '%spx' % size,
                'height': '%spx' % size,
            },
            'aria-hidden': 'true',
            'class': 'bx--btn__icon ' + values['class'],
        })


class IconButton(Button):
    """Button icon only component.
    """
    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        super().prepare(values, context)
        values['class'].extend([
                'bx--btn--icon-only',
                'bx--tooltip__trigger',
                'bx--tooltip--a11y',
                'bx--tooltip--bottom',
                'bx--tooltip--align-center'])


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--btn {class}" {props}>
  <span class="bx--assistive-text">{child}</span>
  {slot_icon}
</{astag}>
"""
        return self.format(template, values, context)


class ButtonSet(Node):
    """Button set component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        context['button_set'] = True


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--btn-set {class}" {props}>
  {child}
</{astag}>
"""
        return self.format(template, values)


components = {
    'Button': Button,
    'ButtonSet': ButtonSet,
    'IconButton': IconButton,
}
