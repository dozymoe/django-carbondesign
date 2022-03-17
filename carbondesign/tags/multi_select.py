"""
Multi Select
============

See: https://the-carbon-components.netlify.app/?nav=multi-select

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class MultiSelect(FormNode):
    """Multi Select component.
    """
    MODES = ('default', 'inline', 'filterable')
    "Available variants."
    NODE_PROPS = ('light',)
    "Extended Template Tag arguments."
    TEMPLATES = ('items', 'icon_menu', 'icon_clear', *FormNode.TEMPLATES)
    "Conditional templates."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_open'] = _("Open menu")
        values['txt_close'] = _("Close menu")
        values['txt_multi'] = _("Multi select options")
        values['txt_clear'] = _("Clear all selected items")
        values['txt_clear_num'] = _("Clear selection")
        values['txt_filter'] = _("Filter...")

        values['values_count'] = len(self.bound_field.value())

        if self.eval(self.kwargs.get('light'), context):
            values['wrapper_class'].append('bx--list-box-light')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    <label class="bx--label {label_class}" {label_props}>
      {label}
    </label>
    <div class="bx--multi-select bx--list-box {wrapper_class}">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="{txt_open}" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">{txt_multi}</span>
        {tmpl_icon_menu}
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          {label}
        </legend>
        {tmpl_items}
      </fieldset>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_filterable(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper">
    <label class="bx--label {label_class}" {label_props}>
      {label}
    </label>
    <div class="bx--multi-select bx--list-box bx--combo-box bx--multi-select-filterable {wrapper_class}">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="{txt_open}" aria-expanded="false" aria-haspopup="true">
        <input class="bx--text-input" placeholder="{txt_filter}">
        {tmpl_icon_menu}
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          {label}
        </legend>
        {tmpl_items}
      </fieldset>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_inline(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--form-item">
  <div class="bx--list-box__wrapper bx--list-box__wrapper--inline">
    <label class="bx--label {label_class}" {label_props}>
      {label}
    </label>
    <div class="bx--multi-select bx--list-box bx--list-box--inline {wrapper_class}">
      <div role="button" class="bx--list-box__field" tabindex="0"
          aria-label="{txt_open}" aria-expanded="false" aria-haspopup="true">
        <span class="bx--list-box__label">{txt_multi}</span>
        {tmpl_icon_menu}
      </div>
      <fieldset class="bx--list-box__menu" role="listbox">
        <legend class="bx--assistive-text">
          {label}
        </legend>
        {tmpl_items}
      </fieldset>
    </div>
    {tmpl_help}
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_icon_clear(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<div role="button"
    class="bx--list-box__selection bx--list-box__selection--multi bx--tag--filter"
    tabindex="0" title="{txt_clear}">
    {values_count}
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        aria-label="{txt_clear_num}" width="16" height="16"
        viewBox="0 0 32 32" role="img">
      <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
    </svg>
</div>
"""
        return self.format(template, values)


    def render_tmpl_icon_menu(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<div class="bx--list-box__menu-icon">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-label="{txt_open}" width="16" height="16" viewBox="0 0 16 16"
      role="img">
    <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
  </svg>
</div>
"""
        return self.format(template, values)


    def render_tmpl_items(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<div class="bx--list-box__menu-item">
  <div class="bx--list-box__menu-item__option">
    <div class="bx--form-item bx--checkbox-wrapper">
      <label title="{child}" class="bx--checkbox-label">
        <input type="checkbox" name="{name}" readonly class="bx--checkbox"
            id="{id}" value="{value}" {props}>
        <span class="bx--checkbox-appearance"></span>
        <span class="bx--checkbox-label-text">
          {child}
        </span>
      </label>
    </div>
  </div>
</div>
"""
        selected = self.bound_field.value()

        items = []
        for ii, (_, val, txt) in enumerate(self.choices(context)):
            options = {
                'id': '%s-%s' % (values['id'], ii),
                'value': val,
                'child': txt,
                'name': self.bound_field.name,
            }
            props = []
            if val in selected:
                props.append('checked')
            options['props'] = ' '.join(props)
            items.append(self.format(template, options))

        return '\n'.join(items)


components = {
    'MultiSelect': MultiSelect,
}
