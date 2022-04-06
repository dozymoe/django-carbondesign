# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long
from .base import compare_template, SimpleTestCase

class OverflowMenuHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% OverflowMenu id="uid" %}
  {% OverflowMenuItem active=True %}
    An example option that is really long to show what should be done to handle
    long text
  {% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 2{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 3{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 4{% endOverflowMenuItem %}
  {% OverflowMenuItem disabled=True %}
    Disabled
  {% endOverflowMenuItem %}
  {% OverflowMenuItem variant="danger" %}
    Danger option
  {% endOverflowMenuItem %}
{% endOverflowMenu %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--right bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-uid"
      aria-controls="uid">
    <span class="bx--assistive-text">Overflow</span>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
  </button>
  <div class="bx--overflow-menu-options" tabindex="-1" role="menu"
      aria-labelledby="trigger-uid" id="uid" data-floating-menu-direction="bottom">
    <ul class="bx--overflow-menu-options__content">
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem" data-floating-menu-primary-focus="" title="An example option that is really long to show what should be done to handle long text">
    <span class="bx--overflow-menu-options__option-content">
    An example option that is really long to show what should be done to handle
    long text
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 2
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 3
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 4
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--disabled">
  <button class="bx--overflow-menu-options__btn" role="menuitem" disabled>
    <span class="bx--overflow-menu-options__option-content">
    Disabled
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--danger">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
    Danger option
    </span>
  </button>
</li>
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_flip(self):
        template = """
{% load carbondesign %}
{% OverflowMenu id="uid" flip=True position="left" %}
  {% OverflowMenuItem active=True %}
    An example option that is really long to show what should be done to handle
    long text
  {% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 2{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 3{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 4{% endOverflowMenuItem %}
  {% OverflowMenuItem disabled=True %}
    Disabled
  {% endOverflowMenuItem %}
  {% OverflowMenuItem variant="danger" %}
    Danger option
  {% endOverflowMenuItem %}
{% endOverflowMenu %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--left bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-uid"
      aria-controls="uid">
    <span class="bx--assistive-text">Overflow</span>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
  </button>
  <div class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1" role="menu"
      aria-labelledby="trigger-uid" id="uid" data-floating-menu-direction="bottom">
    <ul class="bx--overflow-menu-options__content">
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem" data-floating-menu-primary-focus="" title="An example option that is really long to show what should be done to handle long text">
    <span class="bx--overflow-menu-options__option-content">
    An example option that is really long to show what should be done to handle
    long text
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 2
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 3
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 4
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--disabled">
  <button class="bx--overflow-menu-options__btn" role="menuitem" disabled>
    <span class="bx--overflow-menu-options__option-content">
    Disabled
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--danger">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
    Danger option
    </span>
  </button>
</li>
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_flip_link(self):
        template = """
{% load carbondesign %}
{% OverflowMenu id="uid" flip=True position="left" %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" active=True %}
    An example option that is really long to show what should be done to handle
    long text
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" %}
    Option 2
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" %}
    Option 3
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" %}
    Option 4
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" disabled=True %}
    Disabled
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" variant="danger" %}
    Danger option
  {% endOverflowMenuItem %}
{% endOverflowMenu %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--left bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-uid"
      aria-controls="uid">
    <span class="bx--assistive-text">Overflow</span>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
  </button>
  <div class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1" role="menu"
      aria-labelledby="trigger-uid" id="uid" data-floating-menu-direction="bottom">
    <ul class="bx--overflow-menu-options__content">
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com" data-floating-menu-primary-focus="" title="An example option that is really long to show what should be done to handle long text">
    <span class="bx--overflow-menu-options__option-content">
    An example option that is really long to show what should be done to handle
    long text
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Option 2
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Option 3
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Option 4
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--disabled">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com" tabindex="-1" aria-disabled="true">
    <span class="bx--overflow-menu-options__option-content">
    Disabled
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--danger">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Danger option
    </span>
  </a>
</li>
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_up(self):
        template = """
{% load carbondesign %}
{% OverflowMenu id="uid" direction="top" %}
  {% OverflowMenuItem active=True %}
    An example option that is really long to show what should be done to handle
    long text
  {% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 2{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 3{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 4{% endOverflowMenuItem %}
  {% OverflowMenuItem disabled=True %}
    Disabled
  {% endOverflowMenuItem %}
  {% OverflowMenuItem variant="danger" %}
    Danger option
  {% endOverflowMenuItem %}
{% endOverflowMenu %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--right bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-uid"
      aria-controls="uid">
    <span class="bx--assistive-text">Overflow</span>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
  </button>
  <div class="bx--overflow-menu-options" tabindex="-1" role="menu"
      aria-labelledby="trigger-uid" id="uid" data-floating-menu-direction="top">
    <ul class="bx--overflow-menu-options__content">
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem" data-floating-menu-primary-focus="" title="An example option that is really long to show what should be done to handle long text">
    <span class="bx--overflow-menu-options__option-content">
    An example option that is really long to show what should be done to handle
    long text
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 2
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 3
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 4
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--disabled">
  <button class="bx--overflow-menu-options__btn" role="menuitem" disabled>
    <span class="bx--overflow-menu-options__option-content">
    Disabled
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--danger">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
    Danger option
    </span>
  </button>
</li>
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_flip_up(self):
        template = """
{% load carbondesign %}
{% OverflowMenu id="uid" flip=True position="left" direction="top" %}
  {% OverflowMenuItem active=True %}
    An example option that is really long to show what should be done to handle
    long text
  {% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 2{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 3{% endOverflowMenuItem %}
  {% OverflowMenuItem %}Option 4{% endOverflowMenuItem %}
  {% OverflowMenuItem disabled=True %}
    Disabled
  {% endOverflowMenuItem %}
  {% OverflowMenuItem variant="danger" %}
    Danger option
  {% endOverflowMenuItem %}
{% endOverflowMenu %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--left bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-uid"
      aria-controls="uid">
    <span class="bx--assistive-text">Overflow</span>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
  </button>
  <div class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1" role="menu"
      aria-labelledby="trigger-uid" id="uid" data-floating-menu-direction="top">
    <ul class="bx--overflow-menu-options__content">
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem" data-floating-menu-primary-focus="" title="An example option that is really long to show what should be done to handle long text">
    <span class="bx--overflow-menu-options__option-content">
    An example option that is really long to show what should be done to handle
    long text
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 2
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 3
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
      Option 4
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--disabled">
  <button class="bx--overflow-menu-options__btn" role="menuitem" disabled>
    <span class="bx--overflow-menu-options__option-content">
    Disabled
    </span>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--danger">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <span class="bx--overflow-menu-options__option-content">
    Danger option
    </span>
  </button>
</li>
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_flip_link_up(self):
        template = """
{% load carbondesign %}
{% OverflowMenu id="uid" flip=True position="left" direction="top" %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" active=True %}
    An example option that is really long to show what should be done to handle
    long text
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" %}
    Option 2
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" %}
    Option 3
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" %}
    Option 4
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" disabled=True %}
    Disabled
  {% endOverflowMenuItem %}
  {% OverflowMenuItem tag="a" href="https://www.ibm.com" variant="danger" %}
    Danger option
  {% endOverflowMenuItem %}
{% endOverflowMenu %}
"""
        expected = """
<div data-overflow-menu class="bx--overflow-menu">
  <button class="bx--overflow-menu__trigger bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--left bx--tooltip--align-start"
      aria-haspopup="true" aria-expanded="false" id="trigger-uid"
      aria-controls="uid">
    <span class="bx--assistive-text">Overflow</span>
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 32 32"
    aria-hidden="true">
  <circle cx="16" cy="8" r="2"></circle>
  <circle cx="16" cy="16" r="2"></circle>
  <circle cx="16" cy="24" r="2"></circle>
</svg>
  </button>
  <div class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1" role="menu"
      aria-labelledby="trigger-uid" id="uid" data-floating-menu-direction="top">
    <ul class="bx--overflow-menu-options__content">
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com" data-floating-menu-primary-focus="" title="An example option that is really long to show what should be done to handle long text">
    <span class="bx--overflow-menu-options__option-content">
    An example option that is really long to show what should be done to handle
    long text
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Option 2
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Option 3
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Option 4
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--disabled">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com" tabindex="-1" aria-disabled="true">
    <span class="bx--overflow-menu-options__option-content">
    Disabled
    </span>
  </a>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu-options__option--danger">
  <a class="bx--overflow-menu-options__btn" role="menuitem" href="https://www.ibm.com">
    <span class="bx--overflow-menu-options__option-content">
    Danger option
    </span>
  </a>
</li>
    </ul>
    <span tabindex="0"></span>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
