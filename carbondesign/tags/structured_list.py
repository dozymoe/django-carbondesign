"""Implements Carbon Design Component: Structured List
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node, FormNode

class StructuredList(Node):
    """Structured List component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('header',)
    "Named children."

    def render_default(self, values, context):
        template = """
<section class="bx--structured-list">
  <div class="bx--structured-list-thead">
    <div class="bx--structured-list-row bx--structured-list-row--header-row">
      {slot_header}
    </div>
  </div>
  <div class="bx--structured-list-tbody">
    {child}
  </div>
</section>
"""
        return self.format(template, values, context)


class StructuredListSelection(FormNode):
    """Structured List Selection component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('header',)
    "Named children."

    def prepare(self, values, context):
        context['bound_field'] = self.bound_field


    def render_default(self, values, context):
        template = """
<section class="bx--structured-list bx--structured-list--selection"
    data-structured-list>
  <div class="bx--structured-list-thead">
    <div class="bx--structured-list-row bx--structured-list-row--header-row">
      {slot_header}
    </div>
  </div>
  <div class="bx--structured-list-tbody">
    {child}
  </div>
</section>
"""
        return self.format(template, values, context)


class StructuredListTh(Node):
    """Structured List column header component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        template = """
<div class="bx--structured-list-th {class}" {props}>{child}</div>
"""
        return self.format(template, values)


class StructuredListTd(Node):
    """Structured List column header component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('nowrap',)

    def prepare(self, values, context):
        if self.eval(self.kwargs.get('nowrap'), context):
            values['class'].append('bx--structured-list-content--nowrap')


    def render_default(self, values, context):
        template = """
<div class="bx--structured-list-td {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


class StructuredListRow(Node):
    """Structured List row component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('value',)

    bound_field = None

    def prepare(self, values, context):
        self.bound_field = context.get('bound_field')
        if self.bound_field:
            values['name'] = self.bound_field.name
            values['value'] = value = self.eval(self.kwargs.get('value'),
                    context)

            selected = self.bound_field.value()
            if value in selected:
                values['label_class'].append(
                        'bx--structured-list-row--selected')
                values['props'].append(('checked', ''))


    def render_default(self, values, context):
        if self.bound_field:
            template = """
<label aria-label="{label}" class="bx--structured-list-row {label_class}"
    tabindex="0" {label_props}>
  {child}
  <input tabindex="-1" class="bx--structured-list-input {class}" value="{value}"
      type="radio" name="{name}" title="{label}" {props}/>
  <div class="bx--structured-list-td">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--structured-list-svg" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
  </div>
</label>
"""
        else:
            template = """
<div class="bx--structured-list-row">
  {child}
</div>
        """
        return self.format(template, values)


components = {
    'StructuredList': StructuredList,
    'StructuredListSelect': StructuredListSelection,
    'StructuredListTh': StructuredListTh,
    'StructuredListTr': StructuredListRow,
    'StructuredListTd': StructuredListTd,
}
