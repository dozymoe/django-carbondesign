import logging
from uuid import uuid4
#-
from django import template
from django.template.base import TextNode # pylint:disable=unused-import

_logger = logging.getLogger(__name__)


def var_eval(value, context):
    if isinstance(value, template.Variable):
        return value.resolve(context)
    return value


class IgnoreMissing(dict):
    def __missing__(self, key):
        return '{' + key + '}'


class DummyNodeList:

    def __init__(self, text):
        self.text = text


    def render(self, context):
        return self.text


class Slot(template.Node):
    """Implements slots.

    It's very simple, don't inherit from Node class below.
    """
    WANT_CHILDREN = True # Needed for coordination with the templatetag

    name = None

    def __init__(self, *args, **kwargs):
        # First argument sent by templatetag is children nodes.
        self.nodelist = args[0]
        # Second required argument is the slot's name.
        self.name = args[1]
        self.kwargs = kwargs


    def classList(self, context):
        return var_eval(self.kwargs.get('class', ''), context).split()


    def label(self, context):
        return var_eval(self.kwargs.get('label'), context)


    def props(self, context):
        props = []
        for key, val in self.kwargs.items():
            if key == 'class':
                continue
            props.append((key, var_eval(val, context)))
        # Ignore properties with falsy value except empty string.
        return [x for x in props if bool(x[1]) or x[1] == '']


    def render(self, context):
        return self.nodelist.render(context)


class Node(template.Node):

    WANT_CHILDREN = False
    "Template Tag needs closing end tag."
    SLOTS = ()
    "Named children."
    MODES = ()
    "Available variants."
    BASE_NODE_PROPS = ('mode', 'tag', 'class', 'label', 'label_class')
    "Base Template Tag arguments."
    NODE_PROPS = ()
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'div'
    "Rendered HTML tag."

    # Parent Tags can set html attributes on their childs.
    CATCH_CLASSNAMES = ()
    CATCH_PROPERTIES = ()

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
        values = {}
        slots = {}

        self.before_prepare(values, context)
        self.prepare(values, context)
        self.after_prepare(values, context)

        self.render_slots(slots, values, context)

        method = getattr(self, 'render_%s' % self.mode, None)
        if not method:
            raise NotImplementedError("Method is missing: render_%s" %\
                    self.mode)

        return method(values, context, slots) # pylint:disable=not-callable


    def id(self, context):
        if not self._id:
            self._id = var_eval(self.kwargs.get('id', 'node-' + uuid4().hex),
                    context)
        return self._id


    def label(self, context):
        return var_eval(self.kwargs.get('label'), context)


    def props(self, context):
        props = [(key, var_eval(val, context))\
                for (key, val) in self.kwargs.items()\
                if key not in self.BASE_NODE_PROPS\
                and key not in self.NODE_PROPS]
        # Ignore properties with falsy value except empty string.
        return [x for x in props if bool(x[1]) or x[1] == '']


    def render_slots(self, slots, values, context):
        for name in self.SLOTS:
            slot_name = f'slot_{name}'
            slot = self.slots.get(name)
            if slot:
                method = getattr(self, f'render_slot_{name}')
                if method:
                    slots[slot_name] = method(
                            {
                                'child': slot.render(context),
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
        self.mode = self.kwargs.get('mode', None)
        if self.MODES:
            if not self.mode:
                self.mode = self.MODES[0]
            elif self.mode not in self.MODES:
                raise NotImplementedError("Mode %s is not allowed." %\
                        self.mode)
        else:
            self.mode = 'default'

        values['id'] = self.id(context)
        values['tag'] = var_eval(self.kwargs.get('tag', self.DEFAULT_TAG),
                context)
        values['label'] = self.label(context)
        values['props'] = self.props(context)
        values['class'] = var_eval(self.kwargs.get('class', ''), context)\
                .split()
        values['label_props'] = []
        values['label_class'] = var_eval(self.kwargs.get('label_class', ''),
                context)\
                .split()

        self.before_prepare_slots(values, context)

        # Parent Tags can set html attributes on their childs.
        for ext in self.CATCH_CLASSNAMES:
            if ext in context:
                values['class'].extend(context[ext])
        for ext in self.CATCH_PROPERTIES:
            if ext in context:
                values['props'].extend(context[ext])


    def before_prepare_slots(self, values, context):
        for name in self.SLOTS:
            slot = self.slots.get(name)
            if slot:
                values[name + '_class'] = slot.classList(context)
                values[name + '_props'] = slot.props(context)
            else:
                values[name + '_class'] = []
                values[name + '_props'] = []


    def after_prepare(self, values, context):
        values['props'] = self.join_attributes(self.prune_attributes(
                values['props']))

        if self.WANT_CHILDREN:
            values['child'] = self.nodelist.render(context)
        else:
            values['child'] = ''

        values['class'] = ' '.join(values['class'])
        values['label_props'] = self.join_attributes(self.prune_attributes(
                values['label_props']))
        values['label_class'] = ' '.join(values['label_class'])

        self.after_prepare_slots(values, context)


    def after_prepare_slots(self, values, context):
        for name in self.SLOTS:
            slot = self.slots.get(name)
            if not slot:
                continue
            values[name + '_class'] = ' '.join(values[name + '_class'])
            values[name + '_props'] = self.join_attributes(
                    self.prune_attributes(values[name +'_props']))


    def prune_attributes(self, attrs):
        """Cleanup duplicate attributes.
        """
        added_props = set()

        def _clean_attributes():
            for prop in reversed(attrs):
                prop_name = prop[0]
                if prop_name in added_props:
                    continue
                added_props.add(prop_name)
                yield prop

        return list(_clean_attributes())


    def join_attributes(self, attrs):
        return ' '.join('%s="%s"' % x for x in attrs)


    def prepare(self, values, context):
        pass


    def eval(self, value, context):
        return var_eval(value, context)


    def format(self, tpl, values, slots=None):
        if slots:
            tpl = tpl.format_map(IgnoreMissing(slots))
        return tpl.format_map(IgnoreMissing(values))


class FormNode(Node):

    SLOTS = ('help', 'icon')
    "Named children."
    BASE_NODE_PROPS = ('hidden', 'disabled', *Node.BASE_NODE_PROPS)
    "Base Template Tag arguments."

    bound_field = None

    def id(self, context):
        return self.bound_field.id_for_label


    def label(self, context):
        if 'label' in self.kwargs:
            return var_eval(self.kwargs['label'], context)
        return self.bound_field.label


    def element(self, values, context):
        field = self.bound_field
        widget_attrs = field.field.widget.attrs

        attrs = dict(values['props'])
        attrs['class'] = widget_attrs.get('class', '').split()
        if field.help_text:
            attrs['aria-controls'] = values['id'] + '-hint'
            attrs['aria-describedby'] = values['id'] + '-hint'

        self.prepare_element_attributes(attrs, widget_attrs, context)
        attrs['class'] = ' '.join(attrs['class'])

        if var_eval(self.kwargs.get('hidden'), context):
            return self.bound_field.as_hidden(attrs=attrs)
        return field.as_widget(attrs=attrs)


    def element_attributes(self):
        return self.bound_field.field.widget.attrs


    def before_prepare(self, values, context):
        self.bound_field = self.args[0].resolve(context)
        if 'help' not in self.slots and self.bound_field.help_text:
            self.slots['help'] = Slot(DummyNodeList(self.bound_field.help_text),
                    'help')
        super().before_prepare(values, context)


    def after_prepare(self, values, context):
        super().after_prepare(values, context)
        values['element'] = self.element(values, context)

        if self.bound_field.errors:
            values['form_errors'] = self.bound_field.errors.as_text()
        else:
            values['form_errors'] = ''


    def prepare_element_attributes(self, attrs, default, context):
        pass


    def render_slot_help(self, values, context):
        tmpl = """
<div class="bx--form__helper-text {class}" {props}>
  {child}
</div>
"""
        return tmpl.format(**values)


    def render_slot_icon(self, values, context):
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