"""Implements Carbon Design Component: UI Shell
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.html import strip_tags
from django.utils.translation import gettext as _
#-
from .base import Node

class UiShell(Node):
    """UI Shell component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('navigation', 'links', 'actions', 'sidenav', 'switcher')
    "Named children."
    NODE_PROPS = ('href', 'label_prefix', 'title', 'title_prefix')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'header'
    "Rendered HTML tag."
    TEMPLATES = ('title', 'hamburger')
    "Conditional templates."

    def prepare(self, values, context):
        values['title'] = self.eval(self.kwargs.get('title'), context)
        values['title_prefix'] = self.eval(self.kwargs.get('title_prefix'),
                context)
        values['href'] = self.eval(self.kwargs.get('href', '#'), context)

        if 'label_prefix' in self.kwargs:
            values['long_label'] = '%s %s' % (
                    self.eval(self.kwargs.get('label_prefix'), context),
                    self.label(context))
        values['long_label'] = self.label(context)

        values['txt_skip_menu'] = _("Skip to main content")
        values['txt_open_menu'] = _("Open menu")
        values['txt_close_menu'] = _("Close menu")


    def render_default(self, values, context):
        template = """
<{tag} class="bx--header {class}" role="banner" aria-label="{long_label}"
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
</{tag}>

{slot_sidenav}
{slot_switcher}
{slot_navigation}
<div class="bx--content">{child}</div>
"""
        return self.format(template, values, context)


    def render_slot_navigation(self, values, context):
        template = """
<div class="bx--navigation {class}" id="navigation-menu-{id}"
    hidden data-navigation-menu {props}>
  {child}
</div>
"""
        return self.format(template, values)


    def render_slot_links(self, values, context):
        template = """
<nav class="bx--header__nav {class}" aria-label="{label}" data-header-nav>
  <ul class="bx--header__menu-bar" aria-label="{label}" {props}>
    {child}
  </ul>
</nav>
"""
        return self.format(template, values)


    def render_slot_actions(self, values, context):
        template = """
<div class="bx--header__global {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


    def render_tmpl_title(self, values, context):
        if 'title' in self.kwargs:
            if 'title_prefix' in self.kwargs:
                template = """
<span class="bx--header__name--prefix">{title_prefix} &nbsp;</span>
{title}
"""
            else:
                template = "{title}"
        else:
            template = "{label}"
        return self.format(template, values)


    def render_tmpl_hamburger(self, values, context):
        template = """
<button class="bx--header__menu-trigger bx--header__action"
    aria-label="{txt_open_menu}" title="{txt_open_menu}"
    data-navigation-menu-panel-label-expand="{txt_open_menu}"
    data-navigation-menu-panel-label-collapse="{txt_close_menu}"
    data-navigation-menu-target="#navigation-menu-{id}">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true" class="bx--navigation-menu-panel-collapse-icon"
      width="20" height="20" viewBox="0 0 32 32">
    <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
      aria-hidden="true" class="bx--navigation-menu-panel-expand-icon"
      width="20" height="20" viewBox="0 0 20 20">
    <path d="M2 14.8H18V16H2zM2 11.2H18V12.399999999999999H2zM2 7.6H18V8.799999999999999H2zM2 4H18V5.2H2z"></path>
  </svg>
</button>
"""
        if 'navigation' in self.slots:
            return self.format(template, values)
        return ""


class Link(Node):
    """Navigation link.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('submenu',)
    "Named children."

    is_submenu = False

    def prepare(self, values, context):
        self.is_submenu = context.get('navlink_submenu')
        if self.is_submenu:
            values['props'].append(('tabindex', '-1'))
        else:
            values['props'].append(('tabindex', '0'))

        if 'submenu' in self.slots:
            context['navlink_submenu'] = True


    def render_default(self, values, context):
        if 'submenu' in self.slots:
            values['cleaned_child'] = strip_tags(values['child'])

            template = """
<li class="bx--header__submenu" data-header-submenu>
  <a class="bx--header__menu-item bx--header__menu-title {class}"
      aria-haspopup="true" aria-expanded="true" {props}>
    {child}
    <svg class="bx--header__menu-arrow" width="12" height="7"
        aria-hidden="true">
      <path d="M6.002 5.55L11.27 0l.726.685L6.003 7 0 .685.726 0z" />
    </svg>
  </a>
  <ul class="bx--header__menu" aria-label="{cleaned_child}"
      {slot_submenu_props}>
    {slot_submenu}
  </ul>
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


class Action(Node):
    """Topbar action buttons.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('svg_open', 'svg_close')
    "Named children."
    NODE_PROPS = ('target',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def prepare(self, values, context):
        values['txt_close_menu'] = _("Close menu")
        values['target'] = self.eval(self.kwargs['target'], context)


    def render_default(self, values, context):
        template = """
<div class="bx--header__global {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


    def render_slot_svg_open(self, values, context):
        template = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true" class="bx--navigation-menu-panel-expand-icon {class}"
    width="20" height="20" viewBox="0 0 32 32" {props}>
  {child}
</svg>
"""
        return self.format(template, values)


    def render_slot_svg_close(self, values, context):
        template = """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
    aria-hidden="true" class="bx--navigation-menu-panel-collapse-icon {class}"
    width="20" height="20" viewBox="0 0 32 32" {props}>
  {child}
</svg>
"""
        return self.format(template, values)


class NavSection(Node):
    """Side navigation's section.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
        template = """
<{tag} class="bx--navigation-section {class}" {props}>
  <ul class="bx--navigation-items">
    {child}
  </ul>
</{tag}>
"""
        return self.format(template, values)


class NavItem(Node):
    """Side navigation's items.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('submenu', 'icon')
    "Named children."
    NODE_PROPS = ('active',)
    "Extended Template Tag arguments."

    is_submenu = False

    def prepare(self, values, context):
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


    def render_default(self, values, context):
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
        template = """
<ul id="category-{id}-menu" class="bx--navigation__category-items {class}"
    {props}>
  {child}
</ul>
"""
        return self.format(template, values)


    def render_slot_icon(self, values, context):
        values['class'].append('bx--navigation-item--icon')

        template = """
<div class="bx--navigation-icon {class}">
  <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 32 32" aria-hidden="true" {props}>
    {child}
  </svg>
</div>
"""
        return self.format(template, values)


class SideNav(Node):
    """UI Shell side navigation.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('header', 'footer', 'title_icon', 'title', 'switcher')
    "Named children."
    NODE_PROPS = ('fixed',)
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'aside'
    "Rendered HTML tag."

    def prepare(self, values, context):
        values['txt_label'] = _("Side navigation")
        if self.eval(self.kwargs.get('fixed'), context):
            values['class'].append('bx--side-nav--fixed')


    def render_default(self, values, context):
        template = """
<{tag} class="bx--side-nav {class}" data-side-nav {props}>
  <nav class="bx--side-nav__navigation" role="navigation"
      aria-label="{txt_label}">
    {slot_header}
    <ul class="bx--side-nav__items">
      {child}
    </ul>
    {slot_footer}
  </nav>
</{tag}>
"""
        return self.format(template, values, context)


    def render_slot_header(self, values, context):
        if set('title_icon', 'title', 'switcher')\
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


    def render_slot_footer(self, values, context):
        values['txt_close'] = _("Close the side navigation menu")
        values['txt_close_help'] = _("Toggle the expansion state of the navigation") # pylint:disable=line-too-long

        template = """
<footer class="bx--side-nav__footer {class}" {props}>
  <button type="button" class="bx--side-nav__toggle" title="{txt_close}">
    <div class="bx--side-nav__icon">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          class="bx--side-nav__icon--collapse bx--side-nav-collapse-icon"
          width="20" height="20" viewBox="0 0 32 32">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          aria-hidden="true"
          class="bx--side-nav__icon--expand bx--side-nav-expand-icon" width="20"
          height="20" viewBox="0 0 32 32">
        <path d="M22 16L12 26 10.6 24.6 19.2 16 10.6 7.4 12 6z"></path>
      </svg>
    </div>
    <span class="bx--assistive-text">{txt_close_help}</span>
  </button>
</footer>
"""
        return self.format(template, values)


    def render_slot_title_icon(self, values, context):
        template = """
<div class="bx--side-nav__icon {class}">
  <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 32 32" aria-hidden="true" {props}>
    {child}
  </svg>
</div>
"""
        return self.format(template, values)


    def render_slot_title(self, values, context):
        values['cleaned_title'] = strip_tags(self.values['slot_title'])

        template = """
<h2 class="bx--side-nav__title {class}" title="{cleaned_title}" {props}>
  {child}
</h2>
"""
        return self.format(template, values)


    def render_slot_switcher(self, values, context):
        values['txt_switcher'] = _("Switcher")

        template = """
<div class="bx--side-nav__switcher {class}">
  <label for="side-nav-switcher-{id}" class="bx--assistive-text">
    {txt_switcher}
  </label>
  <select id="side-nav-switcher-{id}" class="bx--side-nav__select" {props}>
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


class SideNavOption(Node):
    """UI Shell side navigation's switcher option.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context):
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
    NODE_PROPS = ('active',)
    "Extended Template Tag arguments."

    is_submenu = False

    def prepare(self, values, context):
        is_active = self.eval(self.kwargs.get('active'), context)

        self.is_submenu = self.context.get('navitem_submenu')
        if self.is_submenu:
            values['class'].append('bx--side-nav__menu-item')
            if is_active:
                values['class'].append('bx--side-nav__menu-item--active')
        else:
            values['class'].append('bx--side-nav__item')
            if is_active:
                values['class'].append('bx--side-nav__item--active')

        if is_active:
            values['link_class'] = 'bx--side-nav__link--current'
            values['props'].append(('aria-current', 'page'))

        if 'submenu' in self.slots:
            context['navitem_submenu'] = True


    def render_default(self, values, context):
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
        template = """
<div class="bx--side-nav__icon bx--side-nav__icon--small {class}">
  <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 32 32" aria-hidden="true" {props}>
    {child}
  </svg>
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
