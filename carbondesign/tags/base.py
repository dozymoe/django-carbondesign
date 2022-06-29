"""Base classes for carbondesign Template Tags.
"""
import html
import logging
import re
from typing import Sequence
from uuid import uuid4
#-
from django import template
from django.template.base import TextNode # pylint:disable=unused-import
from django.template.base import FilterExpression, Variable
from django.utils.html import strip_tags
from django.utils.translation import gettext as _
from lxml import etree
#-
from .base_widgets import CustomCheckboxInput, CustomTextarea, CustomTextInput

_logger = logging.getLogger(__name__)

SLOT_NAME_PATTERN = re.compile(r'{(tmpl|slot)_(\w+)}')
TMPL_MULTI_PATTERN = re.compile(r'(?P<name>\w+)_(?P<index>\d+)$')
VARIABLE_IN_ARG = re.compile(r'{{([\w.:|\'"]+)}}')


def var_eval(value, context):
    """Evaluate argument passed to our Template Tag.
    """
    if isinstance(value, (VariableInVariable, FilterExpression, Variable)):
        return value.resolve(context)

    if isinstance(value, str):
        for match in VARIABLE_IN_ARG.finditer(value):
            parsed = Variable(match.group(1)).resolve(context)
            value = value.replace(match.group(0), str(parsed))

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


def clean_attr_value(value):
    """Strip html of its tags and prepare it to be used as html attribute value.
    """
    value = strip_tags(value).strip().replace('\n', ' ')
    return html.escape(re.sub(r'\s\s+', ' ', value))


class VariableInVariable:
    """Evaluate expressions in tag parameters
    """
    def __init__(self, value, parser):
        self.value = value
        self.parser = parser

    def resolve(self, context):
        """Resolve stored param
        """
        value = self.value
        for match in VARIABLE_IN_ARG.finditer(value):
            expr = FilterExpression(match.group(1), self.parser)
            parsed = expr.resolve(context)
            value = value.replace(match.group(0), parsed)
        return Variable(value).resolve(context)


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
        return var_eval(self.kwargs.get('label', ''), context)


    def props(self, context):
        """Filter arguments passed to Slot excluding the PROPS.
        """
        props = []
        for key, val in self.kwargs.items():
            if key in ('class', 'label'):
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
    BASE_NODE_PROPS = ('mode', 'astag', 'class', 'label', 'label_suffix')
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
        # Create local context.
        context.push({})
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

        if self.WANT_CHILDREN:
            values['child'] = self.nodelist.render(context)
        else:
            values['child'] = ''

        self.after_prepare(values, context)

        method = getattr(self, 'render_%s' % self.mode, None)
        if not method:
            raise NotImplementedError("Method is missing: render_%s" %\
                    self.mode)

        result = method(values, context) # pylint:disable=not-callable
        # Destroy local context.
        context.pop()
        return result


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
                and key not in (f'{a}_class' for a in self.CLASS_AND_PROPS)]
        props = [(key, var_eval(val, context)) for key, val in props]
        # Ignore properties with falsy value except empty string.
        return [x for x in props if bool(x[1]) or x[1] == '']


    def tmpl(self, name, values, context, slots):
        """Render individual templates.

        We don't return values like we do in javascript, not needed.
        """
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
                # Process values set in self.before_prepare_slots()
                self.after_prepare_class_props(name, values, context)

                # Create slot local context.
                context.push({'slot': name})
                slots[slot_name] = method(
                        {
                            # Use context to tell slot's children in which slot
                            # they are, for example when catching props from
                            # parent tags.
                            # It is set here to mimic javascript.
                            'child': slot.render(context),
                            'class': values[name + '_class'],
                            'props': values[name + '_props'],
                            'id': values['id'],
                            'label': slot.label(context),
                        },
                        context)
                # Destroy slot local context.
                context.pop()
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
        if 'tag' in self.kwargs and 'astag' not in self.kwargs:
            _logger.warning("tag NODE_PROPS is deprecated by astag")
            mytag = var_eval(self.kwargs['tag'], context)
        else:
            mytag = var_eval(self.kwargs.get('astag', self.DEFAULT_TAG),
                    context)
        values['astag'] = mytag
        values['props'] = self.props(context)
        values['class'] = var_eval(self.kwargs.get('class', ''), context)\
                .split()
        self._id = var_eval(self.kwargs.get('id', self.default_id()), context)
        values['id'] = self._id

        values['label'] = var_eval(self.kwargs.get('label', ''), context)
        values['label_suffix'] = var_eval(self.kwargs.get('label_suffix', ''),
                    context)

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
        values['props_raw'] = self.prune_attributes(values['props'])
        values['props'] = self.join_attributes(self.prune_attributes(
                values['props']))
        values['class'] = ' '.join(values['class'])

        for name in self.CLASS_AND_PROPS:
            if name in self.SLOTS:
                continue
            self.after_prepare_class_props(name, values, context)


    def after_prepare_class_props(self, name, values, context):
        """Join html classes and html attributes into single strings.
        """
        values[f'{name}_props'] = self.join_attributes(
                self.prune_attributes(values[f'{name}_props']))
        values[f'{name}_class'] = ' '.join(values[f'{name}_class'])


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
        result = []
        for att, val in attrs:
            if val is None or val is False:
                continue
            if val is True:
                result.append(att)
            else:
                val = html.escape(str(val))
                result.append(f'{att}="{val}"')
        return ' '.join(result)


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

        try:
            return tpl.format_map(IgnoreMissing(values))
        except ValueError as e:
            raise e


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
    BASE_NODE_PROPS = ('widget', 'id', 'hidden', 'disabled',
            *Node.BASE_NODE_PROPS)
    "Base Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'help')
    "Prepare xxx_class and xxx_props values."

    bound_field = None
    bound_value = None
    _choices = None

    def default_id(self):
        """Get Django form field html id.
        """
        return self.bound_field.id_for_label


    def label(self):
        """Get Django form field label.
        """
        return self.bound_field.label


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.bound_field = var_eval(self.args[0], context)
        self.bound_value = self.bound_field.value()
        super().before_prepare(values, context)
        if not values['label']:
            values['label'] = self.label()


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """


    def choices(self):
        """Get Django form field choices.
        """
        if self._choices is not None:
            return self._choices
        self._choices = []
        try:
            # We assume self.bound_field is set, but
            # self.bound_field.field.choices may not be.
            choices = self.bound_field.field.choices
        except AttributeError:
            # Assume we are dealing with BooleanField
            default_truthy = self.bound_value or 'on'
            label = self.bound_field.label
            choices = (('', label), (default_truthy, label))

        for option_value, option_label in choices:
            if option_value is None:
                option_value = ''

            if isinstance(option_label, (list, tuple)):
                group_name = option_value
                subchoices = option_label
            else:
                group_name = None
                subchoices = [(option_value, option_label)]

            for subvalue, sublabel in subchoices:
                self._choices.append((group_name, subvalue, sublabel))
        return self._choices


    def render_tmpl_element(self, values, context):
        """Render django form field.
        """
        bound_field = self.bound_field

        attrs = dict(values['props_raw'])
        attrs['id'] = self._id
        attrs['class'] = bound_field.field.widget.attrs.get('class', '').split()
        if bound_field.help_text:
            attrs['aria-controls'] = 'hint-' + values['id']
            attrs['aria-describedby'] = 'hint-' + values['id']

        self.prepare_element_props(attrs, context)
        attrs['class'] = ' '.join(attrs['class'])

        if var_eval(self.kwargs.get('disabled'), context):
            attrs['disabled'] = True

        if var_eval(self.kwargs.get('hidden'), context):
            return bound_field.as_hidden(attrs=attrs)

        widget = self.eval(self.kwargs.get('widget'), context)
        if widget == 'input':
            widget = CustomTextInput(attrs=attrs)
        elif widget == 'textarea':
            widget = CustomTextarea(attrs=attrs)
        else:
            return bound_field.as_widget(attrs=attrs)
        return bound_field.as_widget(widget=widget, attrs=attrs)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not values['label']:
            return ''
        tmpl = """
<label for="{id}" class="bx--label {label_class}" {label_props}>
  {label}{label_suffix}
</label>
"""
        return self.format(tmpl, values)


    def render_tmpl_help(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.bound_field.help_text:
            tmpl = """
<div id="hint-{id}" class="bx--form__helper-text {class}" {props}>
  {child}
</div>
"""
            help_values = {
                'child': self.bound_field.help_text,
                'class': values['help_class'],
                'props': values['help_props'],
                'id': values['id'],
            }
            return tmpl.format(**help_values)
        return ''


    def render_tmpl_errors(self, values, context):
        """Dynamically render a part of the component's template.
        """
        tmpl_t = '<div class="bx--form-requirement__title">{title}.</div>'
        tmpl_s = '<p class="bx--form-requirement__supplement">{supplement}</p>'

        items = []
        for error in self.bound_field.errors:
            title, supplement = error.split('.', 1)
            supplement = supplement.strip()
            items.append(tmpl_t.format(title=title))
            if supplement:
                items.append(tmpl_s.format(supplement=supplement.strip()))
        return '\n'.join(items)


class FormNodes(Node):
    """Base class for tags with multiple form fields.

    The arguments to the tag are all Django form fields.
    """
    BASE_NODE_PROPS = ('widget', 'hidden', 'disabled', *Node.BASE_NODE_PROPS)
    "Base Template Tag arguments."

    bound_fields = None

    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.bound_fields = [var_eval(x, context) for x in self.args]
        for ii, field in enumerate(self.bound_fields):
            values[f'id_{ii}'] = field.id_for_label
            values[f'label_{ii}'] = field.label
        super().before_prepare(values, context)


    def prepare_element_props(self, props, context, bound_field):
        """Prepare html attributes for rendering the form element.
        """


    def tmpl(self, name, values, context, slots):
        """Render individual templates.

        We don't return values like we do in javascript, not needed.
        """
        if isinstance(name, str):
            method_name = name
        else:
            # Trying to facilitate tmpl_label_1 that is used in FormNodes,
            # where 1 refers to self.bound_fields[1].
            # In that case the value of name will be ['label_1', 'label']
            name, method_name = name
        slot_name = f'tmpl_{name}'
        if slot_name in slots:
            return

        method = getattr(self, f'render_tmpl_{method_name}')
        slots[slot_name] = method(values, context)


    def format(self, tpl, values, context=None):
        """Apply the prepared values to the templates.
        """
        # pylint:disable=too-many-nested-blocks
        if context:
            # Assume the caller want to tell us there are sub-templates.
            slots = {}
            for typ, nam in SLOT_NAME_PATTERN.findall(tpl):
                tplvalues = values
                if typ == 'tmpl':
                    # Trying to facilitate tmpl_label_1 that is used in
                    # FormNodes, where 1 refers to self.bound_fields[1].
                    match = TMPL_MULTI_PATTERN.match(nam)
                    if match:
                        index = int(match.group('index'))
                        name = match.group('name')
                        for ii, field in enumerate(self.bound_fields):
                            if ii != index:
                                continue
                            nam = [nam, name]
                            tplvalues = values.copy()
                            tplvalues['_bound_field'] = field
                            break
                method = getattr(self, typ)
                method(nam, tplvalues, context, slots)
            if slots:
                tpl = tpl.format_map(IgnoreMissing(slots))

        return tpl.format_map(IgnoreMissing(values))


    def render_tmpl_element(self, values, context):
        """Render django form fields.
        """
        bound_field = values['_bound_field']

        attrs = dict(values['props_raw'])
        attrs['class'] = bound_field.field.widget.attrs.get('class', '').split()
        if bound_field.help_text or 'help' in self.slots:
            attrs['aria-controls'] = 'hint-' + values['id']
            attrs['aria-describedby'] = 'hint-' + values['id']

        self.prepare_element_props(attrs, context, bound_field)
        attrs['class'] = ' '.join(attrs['class'])

        if var_eval(self.kwargs.get('hidden'), context):
            return bound_field.as_hidden(attrs=attrs)

        widget = self.eval(self.kwargs.get('widget'), context)
        if widget == 'input':
            widget = CustomTextInput(attrs=attrs)
            return bound_field.as_widget(widget=widget, attrs=attrs)
        return bound_field.as_widget(attrs=attrs)


    def render_tmpl_errors(self, values, context):
        """Dynamically render a part of the component's template.
        """
        tmpl_t = '<div class="bx--form-requirement__title">{title}.</div>'
        tmpl_s = '<p class="bx--form-requirement__supplement">{supplement}</p>'

        items = []
        bound_field = values['_bound_field']
        for error in bound_field.errors:
            title, supplement = error.split('.', 1)
            supplement = supplement.strip()
            items.append(tmpl_t.format(title=title))
            if supplement:
                items.append(tmpl_s.format(supplement=supplement.strip()))
        return '\n'.join(items)


class ChoiceFormNode(FormNode):
    """Base class for a single choice from form field with multiple choices.

    The first argument to the tag is the Django form field.
    """
    BASE_NODE_PROPS = ('value', *FormNode.BASE_NODE_PROPS)
    "Base Template Tag arguments."

    value = None
    widget_class = CustomCheckboxInput

    def default_id(self):
        """Get Django form field html id.
        """
        # Somehow this ended up here.
        # If the user didn't set the value argument, we assume they wanted us to
        # take it from the bound field.
        # There is strong assumption that this method is called before the label
        # method below.
        if self.value is None:
            if isinstance(self.bound_value, str):
                self.value = self.bound_value
            elif isinstance(self.bound_value, Sequence):
                self.value = self.bound_value[0]
            else:
                self.value = ''

        id_ = self.bound_field.id_for_label
        for ii, (_, val, _) in enumerate(self.choices()):
            if val == self.value:
                return f'{id_}-{ii}'
        return id_


    def label(self):
        """Get Django form field label.
        """
        for _, val, txt in self.choices():
            if val == self.value:
                return txt
        return ''


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.value = self.eval(self.kwargs.get('value', ''), context)
        super().before_prepare(values, context)

        self.bound_field.field.widget = self.widget_class(
                self.bound_field.field.widget.attrs,
                check_test=self.check_test)

        values['props'].append(('id', self._id))
        values['props'].append(('value', self.value))


    def check_test(self, value):
        """ Test checked attribute

        check_test is a callable that takes a value and returns True if the
        checkbox should be checked for that value.
        """
        if not value:
            return False
        if isinstance(self.bound_value, str):
            return value == self.bound_value
        if isinstance(self.bound_value, Sequence):
            return value in self.bound_value
        return False


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
        attrs = dict(values['props_raw'])
        attrs['class'] = []
        if 'help' in self.slots:
            attrs['aria-controls'] = 'hint-' + values['id']
            attrs['aria-describedby'] = 'hint-' + values['id']

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
<div id="hint-{id}" class="bx--form__helper-text {class}" {props}>
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
