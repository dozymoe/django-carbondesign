"""
UI Shell
========

See: https://the-carbon-components.netlify.app/?nav=ui-shell

""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node, clean_attr_value, modify_svg

class UiShell(Node):
    """UI Shell component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('title', 'title_prefix', 'navigation', 'links', 'actions',
            'sidenav', 'switcher')
    "Named children."
    NODE_PROPS = ('id', 'href', 'label_prefix')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'header'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_skip_menu'] = _("Skip to main content")
        values['txt_open_menu'] = _("Open menu")
        values['txt_close_menu'] = _("Close menu")

        values['href'] = self.eval(self.kwargs.get('href', '#'), context)

        if 'label_prefix' in self.kwargs:
            values['long_label'] = '%s %s' % (
                    self.eval(self.kwargs.get('label_prefix'), context),
                    values['label'])
        else:
            values['long_label'] = values['label']


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--header {class}" role="banner" aria-label="{long_label}"
    data-header {props}>
  <a class="bx--skip-to-content" href="#main-content" tabindex="0">
    {txt_skip_menu}
  </a>
  {tmpl_hamburger}
  <a class="bx--header__name" href="{href}" title="">
    {tmpl_title}
  </a>
  {slot_links}
  {slot_actions}
</{astag}>

{slot_sidenav}
{slot_switcher}
{slot_navigation}
<div class="bx--content">{child}</div>
"""
        return self.format(template, values, context)


    def render_slot_navigation(self, values, context):
        """Render html of the slot.
        """
        template = """
<div class="bx--navigation {class}" id="navigation-menu-{id}"
    hidden data-navigation-menu {props}>
  {child}
</div>
"""
        return self.format(template, values)


    def render_slot_links(self, values, context):
        """Render html of the slot.
        """
        template = """
<nav class="bx--header__nav {class}" aria-label="{label}" data-header-nav>
  <ul class="bx--header__menu-bar" aria-label="{label}" {props}>
    {child}
  </ul>
</nav>
"""
        return self.format(template, values)


    def render_slot_actions(self, values, context):
        """Render html of the slot.
        """
        template = """
<div class="bx--header__global {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


    def render_slot_title_prefix(self, values, context):
        """Render html of the slot.
        """
        template = """
<span class="bx--header__name--prefix {class}" {props}>{child} &nbsp;</span>
"""
        return self.format(template, values)


    def render_tmpl_title(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if 'title' in self.slots:
            title = '{slot_title}'
        else:
            title = '{label}'
        if 'title_prefix' in self.slots:
            template = '{slot_title_prefix} ' + title
        else:
            template = title
        return self.format(template, values, context)


    def render_tmpl_hamburger(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if 'navigation' not in self.slots:
            return ''

        template = """
<button class="bx--header__menu-trigger bx--header__action"
    aria-label="{txt_open_menu}" title="{txt_open_menu}"
    data-navigation-menu-panel-label-expand="{txt_open_menu}"
    data-navigation-menu-panel-label-collapse="{txt_close_menu}"
    data-navigation-menu-target="#navigation-menu-{id}">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-hidden="true" class="bx--navigation-menu-panel-collapse-icon"
      width="20" height="20" viewBox="0 0 32 32">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      aria-hidden="true" class="bx--navigation-menu-panel-expand-icon"
      width="20" height="20" viewBox="0 0 20 20">
    <path d="M2 14.8H18V16H2zM2 11.2H18V12.399999999999999H2zM2 7.6H18V8.799999999999999H2zM2 4H18V5.2H2z"></path>
  </svg>
</button>
"""
        return self.format(template, values)


class Link(Node):
    """Navigation link.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('submenu',)
    "Named children."
    NODE_PROPS = ('expanded',)
    "Extended Template Tag arguments."

    is_submenu = False

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        self.is_submenu = context.get('navlink_submenu')
        if self.is_submenu:
            values['props'].append(('tabindex', '-1'))
        else:
            values['props'].append(('tabindex', '0'))

        if 'submenu' in self.slots:
            context['navlink_submenu'] = True

        if 'submenu' in self.slots:
            if self.eval(self.kwargs.get('expanded'), context):
                values['props'].append(('aria-expanded', 'true'))
            else:
                values['props'].append(('aria-expanded', 'false'))


    def render_default(self, values, context):
        """Output html of the component.
        """
        if 'submenu' in self.slots:
            values['cleaned_child'] = clean_attr_value(values['child'])
            template = """
<li class="bx--header__submenu" data-header-submenu>
  <a class="bx--header__menu-item bx--header__menu-title {class}"
      aria-haspopup="true" {props}>
    {child}
    <svg class="bx--header__menu-arrow" width="12" height="7"
        aria-hidden="true">
      <path d="M6.002 5.55L11.27 0l.726.685L6.003 7 0 .685.726 0z" />
    </svg>
  </a>
  {slot_submenu}
</li>
"""
            return self.format(template, values, context)

        if self.is_submenu:
            template = """
<li role="none">
  <a class="bx--header__menu-item {class}" {props}>
    <span class="bx--text-truncate--end">
      {child}
    </span>
  </a>
</li>
"""
        else:
            template = """
<li>
  <a class="bx--header__menu-item {class}" {props}>
    {child}
  </a>
</li>
"""
        return self.format(template, values)


    def render_slot_submenu(self, values, context):
        """Render html of the slot.
        """
        template = """
<ul class="bx--header__menu {class}" aria-label="{cleaned_child}" {props}>
  {child}
</ul>
"""
        return self.format(template, values)


class Action(Node):
    """Topbar action buttons.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."
    REQUIRED_PROPS = ('label',)
    "Will raise Exception if not set."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--header__action {class}" aria-label="{label}{label_suffix}" title="{label}{label_suffix}"
    {props}>
  {slot_icon}
</{astag}>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
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
        })


class NavSection(Node):
    """Side navigation's section.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--navigation-section {class}" {props}>
  <ul class="bx--navigation-items">
    {child}
  </ul>
</{astag}>
"""
        return self.format(template, values)


class NavItem(Node):
    """Side navigation's items.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('submenu', 'icon')
    "Named children."
    NODE_PROPS = ('id', 'active', 'icon_size')
    "Extended Template Tag arguments."

    is_submenu = False

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        is_active = self.eval(self.kwargs.get('active'), context)

        self.is_submenu = context.get('navitem_submenu')
        if self.is_submenu:
            values['class'].append('bx--navigation__category-item')
            if is_active:
                values['class'].append('bx--navigation__category-item--active')
        else:
            values['class'].append('bx--navigation-item')
            if is_active:
                values['class'].append('bx--navigation-item--active')

        if 'submenu' in self.slots:
            context['navitem_submenu'] = True

        if 'icon' in self.slots:
            values['class'].append('bx--navigation-item--icon')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if 'submenu' in self.slots:
            template = """
<li class="{class}" {props}>
  <div class="bx--navigation__category">
    <button type="button" class="bx--navigation__category-toggle"
        aria-haspopup="true" aria-expanded="false"
        aria-controls="category-{id}-menu">
      {slot_icon}
      <div class="bx--navigation__category-title">
        {child}
        <svg aria-hidden="true" width="20" height="20"
            xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
          <path d="M16 22L6 12l1.414-1.414L16 19.172l8.586-8.586L26 12 16 22z" />
        </svg>
      </div>
    </button>
    {slot_submenu}
  </div>
</li>
"""
        else:
            template = """
<li class="{class}">
  <a class="bx--navigation-link" {props}>
    {slot_icon}
    {child}
  </a>
</li>
"""
        return self.format(template, values, context)


    def render_slot_submenu(self, values, context):
        """Render html of the slot.
        """
        template = """
<ul id="category-{id}-menu" class="bx--navigation__category-items {class}"
    {props}>
  {child}
</ul>
"""
        return self.format(template, values)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        size = self.eval(self.kwargs.get('icon_size', 20), context)
        values['child'] = modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '%spx' % size,
                'height': '%spx' % size,
            },
            'aria-hidden': 'true',
        })

        template = """
<div class="bx--navigation-icon {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


class SideNav(Node):
    """UI Shell side navigation.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('title_icon', 'title', 'switcher')
    "Named children."
    NODE_PROPS = ('id', 'fixed',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'aside'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_label'] = _("Side navigation")
        values['txt_close'] = _("Close the side navigation menu")
        values['txt_close_help'] = _("Toggle the expansion state of the navigation") # pylint:disable=line-too-long

        if self.eval(self.kwargs.get('fixed'), context):
            values['class'].append('bx--side-nav--fixed')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--side-nav {class}" data-side-nav {props}>
  <nav class="bx--side-nav__navigation" role="navigation"
      aria-label="{txt_label}">
    {tmpl_header}
    <ul class="bx--side-nav__items">
      {child}
    </ul>
    <footer class="bx--side-nav__footer {class}" {props}>
      <button type="button" class="bx--side-nav__toggle" title="{txt_close}">
        <div class="bx--side-nav__icon">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              class="bx--side-nav__icon--collapse bx--side-nav-collapse-icon"
              width="20" height="20" viewBox="0 0 32 32" aria-hidden="true">
            <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
          </svg>
          <svg focusable="false" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              class="bx--side-nav__icon--expand bx--side-nav-expand-icon"
              width="20" height="20" viewBox="0 0 32 32" aria-hidden="true">
            <path d="M22 16L12 26 10.6 24.6 19.2 16 10.6 7.4 12 6z"></path>
          </svg>
        </div>
        <span class="bx--assistive-text">{txt_close_help}</span>
      </button>
    </footer>
  </nav>
</{astag}>
"""
        return self.format(template, values, context)


    def render_slot_title_icon(self, values, context):
        """Render html of the slot.
        """
        values['child'] = modify_svg(values['child'], {
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '%spx' % 20,
                'height': '%spx' % 20,
            },
            'aria-hidden': 'true',
        })
        template = """
<div class="bx--side-nav__icon {class}">
  {child}
</div>
"""
        return self.format(template, values)


    def render_slot_title(self, values, context):
        """Render html of the slot.
        """
        values['cleaned_title'] = clean_attr_value(values['child'])

        template = """
<h2 class="bx--side-nav__title {class}" title="{cleaned_title}" {props}>
  {child}
</h2>
"""
        return self.format(template, values)


    def render_slot_switcher(self, values, context):
        """Render html of the slot.
        """
        values['txt_switcher'] = _("Switcher")

        template = """
<div class="bx--side-nav__switcher {class}">
  <label for="side-nav-switcher-{id}" class="bx--assistive-text">
    {txt_switcher}
  </label>
  <select id="side-nav-switcher-{id}" class="bx--side-nav__select" {props}>
    <option class="bx--side-nav__option" value="">{txt_switcher}</option>
    {child}
  </select>
  <div class="bx--side-nav__switcher-chevron">
    <svg aria-hidden="true" width="20" height="20"
        xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
      <path d="M16 22L6 12l1.414-1.414L16 19.172l8.586-8.586L26 12 16 22z" />
    </svg>
  </div>
</div>
"""
        return self.format(template, values)


    def render_tmpl_header(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if set(('title_icon', 'title', 'switcher'))\
                .intersection(self.slots.keys()):

            template = """
<header class="bx--side-nav__header {class}" {props}>
  {slot_title_icon}
  <div class="bx--side-nav__details">
    {slot_title}
    {slot_switcher}
  </div>
</header>
"""
            return self.format(template, values, context)
        return ""


class SideNavOption(Node):
    """UI Shell side navigation's switcher option.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<option class="bx--side-nav__option {class}" {props}>
  {child}
</option>
"""
        return self.format(template, values)


class SideNavItem(Node):
    """UI Shell side navigation's items.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('submenu', 'icon')
    "Named children."
    NODE_PROPS = ('active', 'current', 'icon_size')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('link',)
    "Prepare xxx_class and xxx_props values."

    is_submenu = False

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        is_active = self.eval(self.kwargs.get('active'), context)

        self.is_submenu = context.get('navitem_submenu')
        if self.is_submenu:
            values['class'].append('bx--side-nav__menu-item')
            if is_active:
                values['class'].append('bx--side-nav__menu-item--active')
        else:
            values['class'].append('bx--side-nav__item')
            if is_active:
                values['class'].append('bx--side-nav__item--active')

        if self.eval(self.kwargs.get('current'), context):
            values['link_class'].append('bx--side-nav__link--current')
            values['props'].append(('aria-current', 'page'))

        if 'submenu' in self.slots:
            context['navitem_submenu'] = True
        else:
            values['icon_class'].append('bx--side-nav__icon--small')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if 'submenu' in self.slots:
            template = """
<li class="{class}">
  <button type="button" class="bx--side-nav__submenu" aria-haspopup="true"
      aria-expanded="true" aria-controls="sidenav-{id}-menu">
    {slot_icon}
    <span class="bx--side-nav__submenu-title">
      {child}
    </span>
    <div class="bx--side-nav__icon bx--side-nav__icon--small bx--side-nav__submenu-chevron">
      <svg aria-hidden="true" width="20" height="20"
          xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32">
        <path d="M16 22L6 12l1.414-1.414L16 19.172l8.586-8.586L26 12 16 22z" />
      </svg>
    </div>
  </button>
  <ul id="sidenav-{id}-menu" class="bx--side-nav__menu" {props}>
    {slot_submenu}
  </ul>
</li>
"""
        elif self.is_submenu:
            template = """
<li role="none" class="{class}">
  <a class="bx--side-nav__link {link_class}" {props}>
    {slot_icon}
    <span class="bx--side-nav__link-text">{child}</span>
  </a>
</li>
"""
        else:
            template = """
<li class="{class}">
  <a class="bx--side-nav__link {link_class}" {props}>
    {slot_icon}
    <span class="bx--side-nav__link-text">{child}</span>
  </a>
</li>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        size = self.eval(self.kwargs.get('icon_size', 20), context)
        values['child'] = modify_svg(values['child'], {
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '%spx' % size,
                'height': '%spx' % size,
            },
            'aria-hidden': 'true',
        })
        template = """
<div class="bx--side-nav__icon {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


components = {
    'UiShell': UiShell,
    'UiLink': Link,
    'UiAction': Action,
    'UiNavSection': NavSection,
    'UiNavItem': NavItem,
    'UiSideNav': SideNav,
    'UiSideNavOption': SideNavOption,
    'UiSideNavItem': SideNavItem,
}
