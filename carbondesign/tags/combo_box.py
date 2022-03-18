"""
Combo Box
=========

See: https://the-carbon-components.netlify.app/?nav=combo-box

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node, FormNode

class ComboBox(FormNode):
    """Combo Box component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('label', 'help', 'combo', 'list')
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_open'] = _("Open menu")
        values['txt_clear'] = _("Clear all")

        if self.eval(self.kwargs.get('disabled'), context):
            values['label_class'].append('bx--label--disabled')
            values['help_class'].append('bx--form__helper-text--disabled')
            values['combo_class'].append('bx--list-box--disabled')
            values['list_props'].append(('disabled', 'disabled'))
            values['props'].append(('disabled', 'disabled'))

        if self.eval(self.kwargs.get('light'), context):
            values['combo_class'].append('bx--list-box--light')


    def prepare_element_props(self, props, default, context):
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
    <div class="bx--combo-box bx--list-box {combo_class}" data-invalid>
      <div role="combobox" class="bx--list-box__field" aria-label="{txt_open}"
          aria-expanded="false" aria-haspopup="listbox" {list_props}>
        {element}
        {tmpl_icon_invalid}
        {tmpl_icon_clear}
        {tmpl_icon_menu}
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-{id}"
          aria-label="{label}">
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
    <div class="bx--combo-box bx--list-box {combo_class}">
      <div role="combobox" class="bx--list-box__field" aria-label="{txt_open}"
          aria-expanded="false" aria-haspopup="listbox" {list_props}>
        {element}
        {tmpl_icon_clear}
        {tmpl_icon_menu}
      </div>
      <ul class="bx--list-box__menu" role="listbox" id="menu-{id}"
          aria-label="{label}">
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
  {label}
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


    def render_tmpl_icon_clear(self, values, context):
        """Dynamically render a part of the component's template.
        """
        return """
<div class="bx--list-box__selection" role="button">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor" title="{txt_clear}"
      aria-label="{txt_clear}" width="16" height="16" viewBox="0 0 32 32"
      role="img">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
</div>
"""


class ComboBoxItem(Node):
    """Combo Box item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('active',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('active'), context):
            values['class'].append('bx--list-box__menu-item--highlighted')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--list-box__menu-item {class}" {props}>
  <div class="bx--list-box__menu-item__option" tabindex="0">
    {child}
  </div>
</li>
"""
        return self.format(template, values)


components = {
    'ComboBox': ComboBox,
    'ComboBoxItem': ComboBoxItem,
}
