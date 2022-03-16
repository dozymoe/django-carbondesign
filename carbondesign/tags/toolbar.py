"""Implements Carbon Design Component: Toolbar
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode, Node, modify_svg

class Toolbar(Node):
    """Toolbar component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--toolbar {class}" data-toolbar {props}>
  {child}
</div>
"""
        return self.format(template, values)


class ToolbarSearch(Node):
    """Toolbar search component.
    """
    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_search'] = _("Search")
        values['txt_toolbar_search'] = _("Toolbar Search")
        values['txt_clear_search'] = _("Clear search input")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--search bx--search--sm bx--toolbar-search" role="search"
    data-search data-toolbar-search>
  <label for="search__input-{id}" class="bx--label">
    {txt_search}
  </label>
  <input type="text" class="bx--search-input" id="search__input-{id}"
      placeholder="{txt_search}">
  <button class="bx--toolbar-search__btn" aria-label="{txt_toolbar_search}">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--search-magnifier" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5   C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
    </svg>
  </button>
  <button class="bx--search-close bx--search-close--hidden"
      title="{txt_clear_search}" aria-label="{txt_clear_search}">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 32 32" aria-hidden="true">
      <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
    </svg>
  </button>
</div>
"""
        return self.format(template, values)


class ToolbarItem(Node):
    """Toolbar item component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_list'] = _("List of options")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-overflow-menu class="bx--overflow-menu" tabindex="0"
    aria-label="{txt_list}">
  {slot_icon}
  <ul class="bx--overflow-menu-options">
    {child}
  </ul>
</div>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'class': 'bx--overflow-menu__icon bx--toolbar-filter-icon',
            'style': {
                'width': 16,
                'height': 16,
            },
            'aria-hidden': 'true',
        })


class ToolbarItemMultiSelect(FormNode):
    """Toolbar multi select item component.
    """
    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--toolbar-menu__option">
  <input id="{id}" class="bx--checkbox" type="checkbox" value="{value}"
      name="{name}" {props}>
  <label for="{id}" class="bx--checkbox-label">
    {child}
  </label>
</li>
"""
        values = self.bound_field.value()

        items = []
        for ii, (_, val, txt) in enumerate(self.choices(context)):
            options = {
                'id': '%s-%s' % (values['id'], ii),
                'index': ii,
                'value': val,
                'child': txt,
                'name': self.bound_field.name,
            }
            props = []
            if ii == 0:
                props.append('data-floating-menu-primary-focus')
            if val in values:
                props.append('checked')
            options['props'] = ' '.join(props)
            items.append(self.format(template, options))

        return '\n'.join(items)


class ToolbarItemRadioButton(FormNode):
    """Toolbar radio item component.
    """
    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<fieldset data-row-height class="bx--radio-button-group">
  <legend class="bx--visually-hidden">{label}</legend>
  {tmpl_items}
</fieldset>
"""
        return self.format(template, values, context)


    def render_tmpl_items(self, values, context):
        """Dynamically render a part of the component's template.
        """
        template = """
<li class="bx--toolbar-menu__option">
  <input id="{id}" class="bx--radio-button" type="radio" value="{value}"
      name="{name}" {props}>
  <label for="{id}" class="bx--radio-button__label">
    <span class="bx--radio-button__appearance"></span>
    {child}
  </label>
</li>
"""
        value = self.bound_field.value()

        items = []
        for ii, (_, val, txt) in enumerate(self.choices(context)):
            options = {
                'id': '%s-%s' % (values['id'], ii),
                'index': ii,
                'value': val,
                'child': txt,
                'name': self.bound_field.name,
            }
            props = []
            if ii == 0:
                props.append('data-floating-menu-primary-focus')
            if val == value:
                props.append('checked')
            options['props'] = ' '.join(props)
            items.append(self.format(template, options))

        return '\n'.join(items)


class ToolbarItemHeading(Node):
    """Toolbar item heading component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--toolbar-menu__title {class}" {props}>{child}</li>
"""
        return self.format(template, values)


class ToolbarItemDivider(Node):
    """Toolbar item divider component.
    """
    def render_default(self, values, context):
        """Output html of the component.
        """
        return '<hr class="bx--toolbar-menu__divider"/>'


components = {
    'Toolbar': Toolbar,
    'ToolbarSearch': ToolbarSearch,
    'ToolbarItem': ToolbarItem,
    'ToolbarMultiSelect': ToolbarItemMultiSelect,
    'ToolbarRadioButton': ToolbarItemRadioButton,
    'ToolbarHeading': ToolbarItemHeading,
    'ToolbarDivider': ToolbarItemDivider,
}
