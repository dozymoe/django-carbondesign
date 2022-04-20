"""
List Box
========

See: https://the-carbon-components.netlify.app/?nav=list-box

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node, FormNode

class ListBox(FormNode):
    """List Box component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'inline')
    "Available variants."
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'help', 'list')
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_open'] = _("Open menu")

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['help_class'].append('bx--form__helper-text--disabled')
            values['list_class'].append('bx--list-box--disabled')

        if self.eval(self.kwargs.get('light'), context):
            values['list_class'].append('bx--list-box--light')


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('bx--text-input')
        props['aria-autocomplete'] = 'list'
        props['aria-expanded'] = 'false'
        props['autocomplete'] = 'off'
        props['aria-owns'] = 'menu-' + self._id


    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    {tmpl_label}
    <div class="bx--list-box {list_class}" data-invalid>
      {tmpl_icon_invalid}
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="{txt_open}" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">{value}</span>
        {tmpl_icon_menu}
      </div>
      <ul class="bx--list-box__menu" role="combobox" id="menu-{id}">
        {child}
      </ul>
    </div>
    {tmpl_help}
    <div class="bx--form-requirement">
      {form_errors}
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    {tmpl_label}
    <div class="bx--list-box {list_class}">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="{txt_open}" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">{value}</span>
        {tmpl_icon_menu}
      </div>
      <ul class="bx--list-box__menu" role="combobox" id="menu-{id}">
        {child}
      </ul>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_inline(self, values, context):
        """Output html of the component.
        """
        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper bx--list-box__wrapper--inline">
    {tmpl_label}
    <div class="bx--list-box bx--list-box--inline {list_class}" data-invalid>
      {tmpl_icon_invalid}
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="{txt_open}" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">{value}</span>
        {tmpl_icon_menu}
      </div>
      <ul class="bx--list-box__menu" role="combobox" id="menu-{id}">
        {child}
      </ul>
    </div>
    {tmpl_help}
    <div class="bx--form-requirement">
      {form_errors}
    </div>
  </div>
</div>
"""
        else:
            template = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper bx--list-box__wrapper--inline">
    {tmpl_label}
    <div class="bx--list-box bx--list-box--inline {list_class}">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="{txt_open}" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">{value}</span>
        {tmpl_icon_menu}
      </div>
      <ul class="bx--list-box__menu" role="combobox" id="menu-{id}">
        {child}
      </ul>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_label(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<label for="{id}" class="bx--label {label_class}" {label_props}>
  {label}{label_suffix}
</label>
"""
        return self.format(template, values)


    def render_tmpl_icon_invalid(self, values, context):
        """Dynamically render a part of the component's template.
        """
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--list-box__invalid-icon" width="16" height="16"
    viewBox="0 0 16 16" aria-hidden="true">
  <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2   c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
  <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
</svg>
"""


    def render_tmpl_icon_menu(self, values, context):
        """Dynamically render a part of the component's template.
        """
        return """
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="{txt_open}" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
"""


class ListBoxItem(Node):
    """List Box item component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('active',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('active'), context):
            values['class'].append('bx--list-box__menu-item--active')
            values['class'].append('bx--list-box__menu-item--highlighted')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--list-box__menu-item {class}" {props}>
  <div class="bx--list-box__menu-item__option" tabindex="0">
    {child}
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        aria-hidden="true" class="bx--list-box__menu-item__selected-icon"
        width="16" height="16" viewBox="0 0 32 32">
      <path d="M13 24L4 15 5.414 13.586 13 21.171 26.586 7.586 28 9 13 24z"></path>
    </svg>
  </div>
</li>
"""
        return self.format(template, values)


components = {
    'ListBox': ListBox,
    'ListBoxItem': ListBoxItem,
}
