"""
Dropdown
========

See: https://www.carbondesignsystem.com/components/dropdown/usage/

This module is currently disabled, it's a weird component that receive input,
but there is no html input element. Wait and see its progress.

Dropdowns present a list of options from which a user can select one option,
or several. A selected option can represent a value in a form, or can be used
as an action to filter or sort existing content.

Overview
--------

There are three different variants of dropdowns that support various kinds of
functionality—dropdown, multiselect, and combo box.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node, clean_attr_value, modify_svg

class Dropdown(Node):
    """Dropdown component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('help', 'errors')
    "Named children."
    NODE_PROPS = ('id', 'value', 'disabled', 'up', 'light', 'inline')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'help', 'wrapper', 'dropdown')
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['value'] = self.eval(self.kwargs.get('value', ''), context)

        if self.eval(self.kwargs.get('disabled', False), context):
            values['class'].append('bx--dropdown--disabled')
            values['props'].append(('disabled', 'disabled'))
            values['label_class'].append('bx--label--disabled')
            values['label_props'].append(('aria-disabled', 'true'))
            values['help_class'].append('bx--form__helper-text--disabled')
            values['help_props'].append(('aria-disabled', 'true'))
            context['dropdown_disabled'] = True

        if self.eval(self.kwargs.get('up', False), context):
            values['class'].append('bx--dropdown--up')

        if self.eval(self.kwargs.get('light', False), context):
            values['class'].append('bx--dropdown--light')

        if self.eval(self.kwargs.get('inline', False), context):
            values['wrapper_class'].append('bx--dropdown__wrapper--inline')
            values['dropdown_props'].append(('data-dropdown-type', 'inline'))
            values['class'].append('bx--dropdown--inline')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if 'errors' in self.slots:
            template = """
<div class="bx--form-item">
  <div class="bx--dropdown__wrapper {wrapper_class}">
    <span id="label-{id}" class="bx--label {label_class}" {label_props}>
      {label}{label_suffix}
    </span>
    <div data-dropdown data-value
        class="bx--dropdown bx--dropdown--invalid {class}" data-invalid
        {dropdown_props}>
      <button class="bx--dropdown-text" aria-haspopup="true"
          aria-expanded="false" aria-controls="menu-{id}"
          aria-labelledby="label-{id} value-{id}" type="button" {props}>
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--dropdown__invalid-icon" width="16" height="16"
            viewBox="0 0 16 16" aria-hidden="true">
          <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z">
          </path><path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
        </svg>
        <span class="bx--dropdown-text__inner" id="value-{id}">
          {value}
        </span>
        <span class="bx--dropdown__arrow-container">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              class="bx--dropdown__arrow" width="16" height="16"
              viewBox="0 0 16 16" aria-hidden="true">
            <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
          </svg>
        </span>
      </button>
      <ul class="bx--dropdown-list" id="menu-{id}" role="menu" tabindex="-1"
          aria-hidden="true" aria-labelledby="label-{id}">
        {child}
      </ul>
    </div>
    {slot_help}
    <div class="bx--form-requirement">
      {slot_errors}
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--dropdown__wrapper {wrapper_class}">
    <span id="label-{id}" class="bx--label {label_class}" {label_props}>
      {label}{label_suffix}
    </span>
    <div data-dropdown data-value class="bx--dropdown {class}" {dropdown_props}>
      <button class="bx--dropdown-text" aria-haspopup="true"
          aria-expanded="false" aria-controls="menu-{id}"
          aria-labelledby="label-{id} value-{id}" type="button" {props}>
        <span class="bx--dropdown-text__inner" id="value-{id}">
          {value}
        </span>
        <span class="bx--dropdown__arrow-container">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              class="bx--dropdown__arrow" width="16" height="16"
              viewBox="0 0 16 16" aria-hidden="true">
            <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
          </svg>
        </span>
      </button>
      <ul class="bx--dropdown-list" id="menu-{id}" role="menu" tabindex="-1"
          aria-hidden="true" aria-labelledby="label-{id}">
        {child}
      </ul>
    </div>
    {slot_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_slot_help(self, values, context):
        """Render html of the slot.
        """
        template = """
<div class="bx--form__helper-text {class}" {props}>{child}</div>
"""
        return self.format(template, values, context)


class DropdownItem(Node):
    """Dropdown item component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."
    NODE_PROPS = ('active', 'value')
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['value'] = self.eval(self.kwargs.get('value', ''), context)

        if self.eval(self.kwargs.get('active'), context):
            values['props'].append(('aria-checked', 'true'))
        else:
            values['props'].append(('aria-checked', 'false'))
            values['props'].append(('tabindex', '-1'))

        # Note: remove `tabindex` from disabled dropdown lists
        if context.get('dropdown_disabled'):
            values['props'].append(('tabindex', '-1'))


    def render_default(self, values, context):
        """Output html of the component.
        """
        values['cleaned_child'] = clean_attr_value(values['child'])

        template = """
<li data-option data-value="{value}" class="bx--dropdown-item {class}"
    title="{cleaned_child}">
  <a class="bx--dropdown-link" role="menuitemradio" id="item-{id}" {props}>
    {child}
  </a>
  {slot_icon}
</li>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'class': 'bx--list-box__menu-item__selected-icon ' +\
                values['class'],
            'style': {
                'will-change': 'transform',
                'width': '%spx' % 16,
                'height': '%spx' % 16,
            },
            'aria-hidden': 'true',
        })


components = {
    'Dropdown': Dropdown,
    'DropdownItem': DropdownItem,
}
