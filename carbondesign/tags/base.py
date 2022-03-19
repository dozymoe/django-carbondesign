"""Base classes for carbondesign Template Tags.
"""
#from copy import copy
import logging
import re
from uuid import uuid4
#-
from django import template
from django.template.base import TextNode # pylint:disable=unused-import
from django.utils.translation import gettext as _
from lxml import etree
#-
from .base_widgets import CustomTextInput

_logger = logging.getLogger(__name__)

SLOT_NAME_PATTERN = re.compile(r'{(tmpl|slot)_(\w+)}')


def var_eval(value, context):
    """Evaluate argument passed to our Template Tag.
    """
    if isinstance(value, template.Variable):
        return value.resolve(context)
    return value


def modify_svg(xml, props):
    """Modify xml attributes of an svg image.
    """
    # pylint:disable=c-extension-no-member
    root = etree.fromstring(xml)
    for attr, value in props.items():
        if attr == 'style':
            value = ';'.join('%s:%s' % (x, y) for x, y in value.items())
        root.attrib[attr] = value
    return etree.tostring(root).decode()


class IgnoreMissing(dict):
    """String formatting but the variables are optional.
    """
    def __missing__(self, key):
        """Replacement string for missing variables.
        """
        return '{' + key + '}'


class DummyNodeList:
    """Fake Django template node.
    """
    def __init__(self, text):
        self.text = text


    def get_nodes_by_type(self, type_):
        """Dummy method that returns empty.
        """
        return []


    def render(self, context):
        """Return the passed in string.
        """
        return self.text


class Slot(template.Node):
    """Implements slots.

    It's very simple, so don't inherit from Node class below.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    name = None

    def __init__(self, *args, **kwargs):
        # First argument sent by templatetag is children nodes.
        self.nodelist = args[0]
        # Second required argument is the slot's name.
        self.name = args[1]
        self.kwargs = kwargs


    def classList(self, context):
        """Get class argument as a list.
        """
        return var_eval(self.kwargs.get('class', ''), context).split()


    def label(self, context):
        """Get label argument.
        """
        return var_eval(self.kwargs.get('label'), context)


    def props(self, context):
        """Filter arguments passed to Slot excluding the PROPS.
        """
        props = []
        for key, val in self.kwargs.items():
            if key == 'class':
                continue
            props.append((key, var_eval(val, context)))
        # Ignore properties with falsy value except empty string.
        return [x for x in props if bool(x[1]) or x[1] == '']


    def render(self, context):
        """Render the Slot as html.
        """
        return self.nodelist.render(context)


class Node(template.Node):
    """Base class for all carbondesign tags.
    """
    WANT_CHILDREN = False
    "Template Tag needs closing end tag."
    SLOTS = ()
    "Named children."
    MODES = ()
    "Available variants."
    BASE_NODE_PROPS = ('mode', 'tag', 'class', 'label')
    "Base Template Tag arguments."
    NODE_PROPS = ()
    "Extended Template Tag arguments."
    REQUIRED_PROPS = ()
    "Will raise Exception if not set."
    DEFAULT_TAG = 'div'
    "Rendered HTML tag."
    CLASS_AND_PROPS = ()
    "Prepare xxx_class and xxx_props values."

    # Parent Tags can set the arguments of their children Tags, in effect
    # changing their appearance.
    CATCH_PROPS = ()

    context = None
    mode = None
    _id = None

    def __init__(self, *args, **kwargs):
        if self.WANT_CHILDREN:
            self.args = args[1:]

            self.nodelist = args[0]
            slots = self.nodelist.get_nodes_by_type(Slot)
            for slot in slots:
                self.nodelist.remove(slot)
            self.slots = {s.name: s for s in slots}
        else:
            self.args = args
            self.slots = {}

        self.kwargs = kwargs


    def render(self, context):
        """Render the Template Tag as html.
        """
        # Parent Tags can set the arguments of their children Tags.
        # You can also set them to children Tags in specific slot.
        myslot = context.get('slot')
        for drop in self.CATCH_PROPS:
            if drop in context:
                self.kwargs.update(context[drop])
            if myslot and f'{myslot}_{drop}' in context:
                self.kwargs.update(context[f'{myslot}_{drop}'])

        for prop in self.REQUIRED_PROPS:
            if prop not in self.kwargs:
                raise template.exceptions.TemplateSyntaxError(
                        _("Argument {prop} for template tag is required.")\
                        .format(prop=prop))

        values = {}

        self.before_prepare(values, context)
        self.prepare(values, context)
        self.after_prepare(values, context)

        method = getattr(self, 'render_%s' % self.mode, None)
        if not method:
            raise NotImplementedError("Method is missing: render_%s" %\
                    self.mode)

        return method(values, context) # pylint:disable=not-callable


    def default_id(self):
        """Get unique id.
        """
        return 'node-' + uuid4().hex


    def props(self, context):
        """Filter arguments passed to Template Tag excluding the PROPS.
        """
        props = [(key, val) for key, val in self.kwargs.items()\
                if key not in self.BASE_NODE_PROPS\
                and key not in self.NODE_PROPS \
                and key not in (f'{a}_class' for a in self.CLASS_AND_PROPS)\
                and key not in (f'{a}_props' for a in self.CLASS_AND_PROPS)]
        props = [(key, var_eval(val, context)) for key, val in props]
        # Ignore properties with falsy value except empty string.
        return [x for x in props if bool(x[1]) or x[1] == '']


    def tmpl(self, name, values, context, slots):
        """Render individual templates.
        """
        # We don't return values like we do in javascript, not needed.
        slot_name = f'tmpl_{name}'
        if slot_name in slots:
            return

        method = getattr(self, f'render_tmpl_{name}')
        slots[slot_name] = method(values, context)


    def slot(self, name, values, context, slots):
        """Render individual slots.
        """
        # We don't return values like we do in javascript, not needed.
        slot_name = f'slot_{name}'
        if slot_name in slots:
            return

        slot = self.slots.get(name)
        if slot:
            method = getattr(self, f'render_slot_{name}', None)
            if method:
                slot_context = template.Context(context.flatten())
                slot_context['slot'] = name
                slots[slot_name] = method(
                        {
                            # Use context to tell slot's children in which slot
                            # they are, for example when catching props from
                            # parent tags.
                            # It is set here to mimic javascript.
                            'child': slot.render(slot_context),
                            'class': values[name + '_class'],
                            'props': values[name + '_props'],
                            'id': values['id'],
                            'label': slot.label(context),
                        },
                        context)
            else:
                slots[slot_name] = slot.render(context)
        else:
            slots[slot_name] = ''


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.mode = self.kwargs.get('mode', None)
        if self.MODES:
            if not self.mode:
                self.mode = self.MODES[0]
            elif self.mode not in self.MODES:
                raise NotImplementedError("Mode %s is not allowed." %\
                        self.mode)
        else:
            self.mode = 'default'

        values['mode'] = self.mode
        values['tag'] = var_eval(self.kwargs.get('tag', self.DEFAULT_TAG),
                context)
        values['props'] = self.props(context)
        values['class'] = var_eval(self.kwargs.get('class', ''), context)\
                .split()
        values['label'] = var_eval(self.kwargs.get('label', ''), context)
        self._id = var_eval(self.kwargs.get('id', self.default_id()), context)
        values['id'] = self._id
        for name in self.CLASS_AND_PROPS:
            if name in self.SLOTS:
                continue
            self.before_prepare_class_props(name, values, context)

        self.before_prepare_slots(values, context)


    def before_prepare_class_props(self, name, values, context):
        """Initialize variables for storing html classes and attributes.
        """
        values[f'{name}_props'] = []
        values[f'{name}_class'] = var_eval(
                self.kwargs.get(f'{name}_class', ''), context)\
                .split()


    def before_prepare_slots(self, values, context):
        """Initialize the values meant for rendering slot templates.
        """
        for name in self.SLOTS:
            slot = self.slots.get(name)
            if slot:
                values[f'{name}_class'] = slot.classList(context)
                values[f'{name}_props'] = slot.props(context)
            else:
                values[f'{name}_class'] = []
                values[f'{name}_props'] = []


    def after_prepare(self, values, context):
        """Simplifying values meant for rendering templates.
        """
        values['props'] = self.join_attributes(self.prune_attributes(
                values['props']))
        values['class'] = ' '.join(values['class'])

        if self.WANT_CHILDREN:
            values['child'] = self.nodelist.render(context)
        else:
            values['child'] = ''

        for name in self.CLASS_AND_PROPS:
            if name in self.SLOTS:
                continue
            self.after_prepare_class_props(name, values, context)

        self.after_prepare_slots(values, context)


    def after_prepare_class_props(self, name, values, context):
        """Join html classes and html attributes into single strings.
        """
        values[f'{name}_props'] = self.join_attributes(
                self.prune_attributes(values[f'{name}_props']))
        values[f'{name}_class'] = ' '.join(values[f'{name}_class'])


    def after_prepare_slots(self, values, context):
        """Simplifying values meant for rendering slot templates.
        """
        for name in self.SLOTS:
            slot = self.slots.get(name)
            if not slot:
                continue
            self.after_prepare_class_props(name, values, context)


    def prune_attributes(self, attrs):
        """Cleanup duplicate html attributes.
        """
        added_props = set()

        def _clean_attributes():
            for prop in reversed(attrs):
                prop_name = prop[0]
                if prop_name in added_props:
                    continue
                added_props.add(prop_name)
                yield prop

        return reversed(list(_clean_attributes()))


    def join_attributes(self, attrs):
        """Format html attributes.
        """
        return ' '.join('%s="%s"' % x for x in attrs)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """


    def eval(self, value, context):
        """Evaluate argument passed to our Template Tag.
        """
        return var_eval(value, context)


    def format(self, tpl, values, context=None):
        """Apply the prepared values to the templates.
        """
        if context:
            # Assume the caller want to tell us there is sub-templates.
            slots = {}
            for typ, nam in SLOT_NAME_PATTERN.findall(tpl):
                method = getattr(self, typ)
                method(nam, values, context, slots)
            if slots:
                tpl = tpl.format_map(IgnoreMissing(slots))

        return tpl.format_map(IgnoreMissing(values))


    def set_child_props(self, context, name, slot=None, **kwargs):
        """Use context to set arguments for all children Template Tags.
        """
        if slot:
            name = f'{slot}_{name}'
        context.setdefault(name, {})
        context[name].update(kwargs)


class FormNode(Node):
    """Base class for form field tags.

    The first argument to the tag is the Django form field.
    """
    BASE_NODE_PROPS = ('widget', 'hidden', 'disabled', *Node.BASE_NODE_PROPS)
    "Base Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'help')
    "Prepare xxx_class and xxx_props values."
    RENDER_ELEMENT = True
    "Render the form field widget."

    bound_field = None
    bound_value = None

    def default_id(self):
        """Get Django form field html id.
        """
        return self.bound_field.id_for_label


    def label(self):
        """Get Django form field label.
        """
        return self.bound_field.label


    def element(self, values, context):
        """Render django form field.
        """
        field = self.bound_field
        widget_attrs = field.field.widget.attrs

        attrs = dict(values['props'])
        attrs['class'] = widget_attrs.get('class', '').split()
        if field.help_text or 'help' in self.slots:
            attrs['aria-controls'] = values['id'] + '-hint'
            attrs['aria-describedby'] = values['id'] + '-hint'

        self.prepare_element_props(attrs, widget_attrs, context)
        attrs['class'] = ' '.join(attrs['class'])

        if var_eval(self.kwargs.get('hidden'), context):
            return field.as_hidden(attrs=attrs)

        widget = self.eval(self.kwargs.get('widget'), context)
        if widget == 'input':
            widget = CustomTextInput(attrs=attrs)
            return field.as_widget(widget=widget, attrs=attrs)
        return field.as_widget(attrs=attrs)


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.bound_field = self.args[0].resolve(context)
        self.bound_value = self.bound_field.value()
        super().before_prepare(values, context)
        if not values['label']:
            values['label'] = self.label()


    def after_prepare(self, values, context):
        """Simplifying values meant for rendering templates.
        """
        if self.RENDER_ELEMENT:
            values['element'] = self.element(values, context)
        super().after_prepare(values, context)

        if self.bound_field.errors:
            values['form_errors'] = self.bound_field.errors.as_text()
        else:
            values['form_errors'] = ''


    def prepare_element_props(self, props, default, context):
        """Prepare html attributes for rendering the form element.
        """


    def choices(self):
        """Get Django form field choices.
        """
        for option_value, option_label in self.bound_field.field.choices:
            if option_value is None:
                option_value = ''

            if isinstance(option_label, (list, tuple)):
                group_name = option_value
                choices = option_label
            else:
                group_name = None
                choices = [(option_value, option_label)]

            for subvalue, sublabel in choices:
                yield (group_name, subvalue, sublabel)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''
        tmpl = """
<label for="{id}" class="bx--label {label_class}" {label_props}>
  {label}
</label>
"""
        return self.format(tmpl, values)


    def render_tmpl_help(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.bound_field.help_text:
            tmpl = """
<div class="bx--form__helper-text {class}" {props}>
  {child}
</div>
"""
            help_values = {
                'child': self.bound_field.help_text,
                'class': values['help_class'],
                'props': values['help_props'],
            }
            return tmpl.format(**help_values)
        return ''


class FormNodes(Node):
    """Base class for tags with multiple form fields.

    The arguments to the tag are all Django form fields.
    """
    BASE_NODE_PROPS = ('widget', 'hidden', 'disabled', *Node.BASE_NODE_PROPS)
    "Base Template Tag arguments."

    bound_fields = None

    def elements(self, values, context):
        """Render django form fields.
        """
        for field in self.bound_fields:
            widget_attrs = field.field.widget.attrs

            attrs = dict(values['props'])
            attrs['class'] = widget_attrs.get('class', '').split()
            if field.help_text or 'help' in self.slots:
                attrs['aria-controls'] = values['id'] + '-hint'
                attrs['aria-describedby'] = values['id'] + '-hint'

            self.prepare_element_props(field, attrs, widget_attrs, context)
            attrs['class'] = ' '.join(attrs['class'])

            if var_eval(self.kwargs.get('hidden'), context):
                yield field.as_hidden(attrs=attrs)
                continue

            widget = self.eval(self.kwargs.get('widget'), context)
            if widget == 'input':
                widget = CustomTextInput(attrs=attrs)
                yield field.as_widget(widget=widget, attrs=attrs)
                continue

            yield field.as_widget(attrs=attrs)


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.bound_fields = [x.resolve(context) for x in self.args]
        for ii, field in enumerate(self.bound_fields):
            values[f'id_{ii}'] = field.id_for_label
            values[f'label_{ii}'] = field.label
        super().before_prepare(values, context)


    def after_prepare(self, values, context):
        """Simplifying values meant for rendering templates.
        """
        for ii, element in enumerate(self.elements(values, context)):
            values[f'element_{ii}'] = element
        super().after_prepare(values, context)

        for ii, field in enumerate(self.bound_fields):
            if field.errors:
                values[f'form_errors_{ii}'] = field.errors.as_text()
            else:
                values[f'form_errors_{ii}'] = ''


    def prepare_element_props(self, field, props, default, context):
        """Prepare html attributes for rendering the form element.
        """


class DumbFormNode(Node):
    """For rendering html elements without the associated Django form fields.

    Experimental.
    """
    SLOTS = ('help', 'icon')
    "Named children."
    BASE_NODE_PROPS = ('hidden', 'disabled', *Node.BASE_NODE_PROPS)
    "Base Template Tag arguments."

    def element(self, values, context):
        """Render html of the form control.
        """
        attrs = dict(values['props'])
        attrs['class'] = []
        if 'help' in self.slots:
            attrs['aria-controls'] = values['id'] + '-hint'
            attrs['aria-describedby'] = values['id'] + '-hint'

        self.prepare_element_props(attrs, attrs, context)
        attrs['class'] = ' '.join(attrs['class'])

        if var_eval(self.kwargs.get('hidden'), context):
            attrs.pop('type')
            props = self.join_attributes(self.prune_attributes(attrs))
            return '<input type="hidden" {props}">'.format(props=props)
        return self.render_form_control(attrs, context)


    def render_form_control(self, values, context):
        """Default to rendering input, need to be overridden by subclass.
        """
        props = self.join_attributes(self.prune_attributes(values))
        return '<input {props}">'.format(props=props)


    def after_prepare(self, values, context):
        """Post-process the values for rendering templates.
        """
        values['element'] = self.element(values, context)
        super().after_prepare(values, context)


    def prepare_element_props(self, props, default, context):
        """Prepare html attributes for rendering the form element.
        """


    def render_slot_help(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<div class="bx--form__helper-text {class}" {props}>
  {child}
</div>
"""
        return tmpl.format(**values)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        tmpl = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
    class="bx--btn__icon {class}" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true" {props}>
  {child}
</svg>
"""
        return tmpl.format(**values)


components = {
    'Slot': Slot,
}
