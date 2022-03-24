# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class UiShellTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiShell %}
{% endUiShell %}
"""
        expected = """
<header class="bx--header" role="banner" aria-label=""
    data-header>
  <a class="bx--skip-to-content" href="#main-content" tabindex="0">
    Skip to main content
  </a>
  <a class="bx--header__name" href="#" title="">
  </a>
</header>
<div class="bx--content">
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class UiLinkTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiLink %}
{% endUiLink %}
"""
        expected = """
<li>
  <a class="bx--header__menu-item" tabindex="0">
  </a>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class UiActionTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiAction target="uid" %}
{% endUiAction %}
"""
        expected = """
<button class="bx--header__menu-trigger bx--header__action"
    aria-label="" title=""
    data-navigation-menu-panel-label-expand=""
    data-navigation-menu-panel-label-collapse="Close menu"
    data-switcher-target="#uid">
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class UiNavSectionTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiNavSection %}
{% endUiNavSection %}
"""
        expected = """
<div class="bx--navigation-section">
  <ul class="bx--navigation-items">
  </ul>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class UiNavItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiNavItem %}
{% endUiNavItem %}
"""
        expected = """
<li class="bx--navigation-item">
  <a class="bx--navigation-link">
  </a>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class UiSideNavTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiSideNav %}
{% endUiSideNav %}
"""
        expected = """
<aside class="bx--side-nav" data-side-nav>
  <nav class="bx--side-nav__navigation" role="navigation"
      aria-label="Side navigation">
    <ul class="bx--side-nav__items">
    </ul>
  </nav>
</aside>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class UiSideNavOptionTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiSideNavOption %}
{% endUiSideNavOption %}
"""
        expected = """
<option class="bx--side-nav__option">
</option>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class UiSideNavItemTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% UiSideNavItem %}
{% endUiSideNavItem %}
"""
        expected = """
<li class="bx--side-nav__item">
  <a class="bx--side-nav__link {link_class}">
    <span class="bx--side-nav__link-text">
</span>
  </a>
</li>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
