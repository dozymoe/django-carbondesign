"""
UI Shell Switcher
=================

See: https://the-carbon-components.netlify.app/?nav=ui-shell

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode, Node, clean_attr_value, modify_svg

class Action(Node):
    """Topbar action buttons.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('svg_open', 'svg_close')
    "Named children."
    NODE_PROPS = ('target',)
    "Extended Template Tag arguments."
    REQUIRED_PROPS = ('label', 'target')
    "Will raise Exception if not set."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_close_menu'] = _("Close menu")
        values['target'] = self.eval(self.kwargs['target'], context)


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--header__menu-trigger bx--header__action {class}"
    aria-label="{label}{label_suffix}" title="{label}{label_suffix}"
    data-navigation-menu-panel-label-expand="{label}{label_suffix}"
    data-navigation-menu-panel-label-collapse="{txt_close_menu}"
    data-panel-switcher-target="#{target}" {props}>
  {slot_svg_close}
  {slot_svg_open}
</{astag}>
"""
        return self.format(template, values, context)


    def render_slot_svg_open(self, values, context):
        """Render html of the slot.
        """
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '20px',
                'height': '20px',
            },
            'aria-hidden': 'true',
            'class': 'bx--navigation-menu-panel-collapse-icon',
        })


    def render_slot_svg_close(self, values, context):
        """Render html of the slot.
        """
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '20px',
                'height': '20px',
            },
            'aria-hidden': 'true',
            'class': 'bx--navigation-menu-panel-expand-icon',
        })


class Switcher(Node):
    """UI Shell switcher panel.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('id',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'aside'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--panel--overlay" id="{id}" data-panel-switcher>
  <div class="bx--panel-switcher">
    {child}
  </div>
</{astag}>
"""
        return self.format(template, values, context)


class SwitcherSearch(FormNode):
    """UI Shell switcher search box.
    """
    NODE_PROPS = ('placeholder',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_clear'] = _("Clear search input")


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('bx--search-input')

        placeholder = self.eval(self.kwargs.get('placeholder'), context)
        props['placeholder'] = placeholder or _("Search")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="bx--panel-switcher__search">
  <div class="bx--form-item">
    <div data-search class="bx--search bx--search--sm bx--search--shell"
        role="search">
      {tmpl_label}
      {tmpl_element}
      <svg class="bx--search-magnifier" width="16" height="16"
          viewBox="0 0 16 16">
        <path d="M6.5 12a5.5 5.5 0 1 0 0-11 5.5 5.5 0 0 0 0 11zm4.936-1.27l4.563 4.557-.707.708-4.563-4.558a6.5 6.5 0 1 1 .707-.707z" fill-rule="nonzero" />
      </svg>
      <button class="bx--search-close bx--search-close--hidden"
          title="{txt_clear}" aria-label="{txt_clear}">
        <svg width="16" height="16" viewBox="0 0 16 16" xmlns="http://www.w3.org/2000/svg">
          <path d="M8 6.586L5.879 4.464 4.464 5.88 6.586 8l-2.122 2.121 1.415 1.415L8 9.414l2.121 2.122 1.415-1.415L9.414 8l2.122-2.121-1.415-1.415L8 6.586zM8 16A8 8 0 1 1 8 0a8 8 0 0 1 0 16z" fill-rule="evenodd" />
        </svg>
      </button>
    </div>
  </div>
</div>
"""
        return self.format(template, values, context)


class SwitcherHeader(Node):
    """UI Shell switcher header.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'p'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--panel-switcher__subheader {class}" {props}>{child}</{astag}>
"""
        return self.format(template, values)


class SwitcherItem(Node):
    """UI Shell switcher item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = '<div class="bx--panel-switcher__item">{child}</div>'
        return self.format(template, values)


class SwitcherMenu(Node):
    """UI Shell switcher menu list.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    DEFAULT_TAG = 'ul'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--panel-switcher__panel-list {class}" {props}>{child}</{astag}>
"""
        return self.format(template, values)


class SwitcherMenuSection(Node):
    """UI Shell switcher submenu.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."
    NODE_PROPS = ('menu_label',)
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('overflow',)
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        menu_label = self.eval(self.kwargs.get('menu_label'), context)
        if menu_label:
            values['overflow_props'].append(('aria-label', menu_label))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--panel-list__item">
  <a class="bx--panel-link" tabindex="0" href="javascript:void(0)">
    {slot_icon}
    <span class="bx--panel-link__name">{label}{label_suffix}</span>
  </a>
  <div data-overflow-menu tabindex="0" class="bx--overflow-menu {overflow_class}" {overflow_props}>
    <svg width="3" height="15" viewBox="0 0 3 15">
      <path d="M0 1.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 1 1-3 0M0 7.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 1 1-3 0M0 13.5a1.5 1.5 0 1 1 3 0 1.5 1.5 0 1 1-3 0"></path>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      data-floating-menu-direction="bottom">
      {child}
    </ul>
  </div>
</li>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        template = '<div class="bx--panel-switcher__icon">{child}</div>'

        values['child'] = modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '20px',
                'height': '20px',
            },
            'aria-hidden': 'true',
        })
        return self.format(template, values)


class SwitcherMenuItem(Node):
    """UI Shell switcher menu item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('active',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('active'), context):
            values['props'].append(('data-floating-menu-primary-focus', True))


    def render_default(self, values, context):
        """Output html of the component.
        """
        values['cleaned_child'] = clean_attr_value(values['child'])

        template = """
<li class="bx--overflow-menu-options__option bx--overflow__item">
  <button class="bx--overflow-menu-options__btn {class}" title="{cleaned_child}"
      {props}>
    {child}
  </button>
</li>
"""
        return self.format(template, values)


components = {
    'UiActionSwitcher': Action,
    'UiSwitcher': Switcher,
    'UiSwitcherSearch': SwitcherSearch,
    'UiSwitcherHeader': SwitcherHeader,
    'UiSwitcherItem': SwitcherItem,
    'UiSwitcherMenu': SwitcherMenu,
    'UiSwitcherMenuSection': SwitcherMenuSection,
    'UiSwitcherMenuItem': SwitcherMenuItem,
}
