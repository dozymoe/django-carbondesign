# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class ProgressIndicatorHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% ProgressIndicator %}
  {% Progress variant="complete" id="uid" %}
    First step

    {% Slot 'help' %}{% endSlot %}
    {% Slot 'optional' %}
      Optional
    {% endSlot %}
  {% endProgress %}

  {% Progress variant="current" id="uid" %}
    Second Step

    {% Slot 'help' %}Overflow Ex.1{% endSlot %}
  {% endProgress %}

  {% Progress variant="incomplete" id="uid" %}
    Third Step

    {% Slot 'help' %}Overflow Ex. 2 Multi Line{% endSlot %}
  {% endProgress %}

  {% Progress variant="invalid" id="uid" %}
    Fourth step

    {% Slot 'help' %}{% endSlot %}
  {% endProgress %}

  {% Progress variant="disabled" id="uid" %}
    Fifth step

    {% Slot 'help' %}{% endSlot %}
  {% endProgress %}
{% endProgressIndicator %}
"""
        expected = """
<ul data-progress data-progress-current class="bx--progress">
<li class="bx--progress-step bx--progress-step--complete">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
    height="16" viewBox="0 0 32 32" aria-hidden="true">
  <path d="M14 21.414L9 16.413 10.413 15 14 18.586 21.585 11 23 12.415 14 21.414z"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,26A12,12,0,1,1,28,16,12,12,0,0,1,16,28Z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    First step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text"></p>
</div>
<p class="bx--progress-optional">
      Optional
    </p>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--current">
<svg>
  <path d="M 7, 7 m -7, 0 a 7,7 0 1,0 14,0 a 7,7 0 1,0 -14,0" ></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Second Step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text">Overflow Ex.1</p>
</div>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--incomplete">
<svg>
  <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Third Step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text">Overflow Ex. 2 Multi Line</p>
</div>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--incomplete" data-invalid="">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--progress__warning" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.1,1,1,4.1,1,8s3.1,7,7,7s7-3.1,7-7S11.9,1,8,1z M8,14c-3.3,0-6-2.7-6-6s2.7-6,6-6s6,2.7,6,6S11.3,14,8,14z"></path>
  <path d="M7.5 4H8.5V9H7.5zM8 10.2c-.4 0-.8.3-.8.8s.3.8.8.8c.4 0 .8-.3.8-.8S8.4 10.2 8 10.2z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Fourth step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text"></p>
</div>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--disabled bx--progress-step--incomplete" aria-disabled="true">
<svg>
  <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Fifth step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text"></p>
</div>
  <span class="bx--progress-line"></span>
</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_vertical(self):
        template = """
{% load carbondesign %}
{% ProgressIndicator vertical=True %}
  {% Progress variant="complete" id="uid" %}
    First step

    {% Slot 'help' %}{% endSlot %}
    {% Slot 'optional' %}
      Optional
    {% endSlot %}
  {% endProgress %}

  {% Progress variant="current" id="uid" %}
    Second Step

    {% Slot 'help' %}Overflow Ex.1{% endSlot %}
  {% endProgress %}

  {% Progress variant="incomplete" id="uid" %}
    Third Step

    {% Slot 'help' %}Overflow Ex. 2 Multi Line{% endSlot %}
  {% endProgress %}

  {% Progress variant="invalid" id="uid" %}
    Fourth step

    {% Slot 'help' %}{% endSlot %}
  {% endProgress %}

  {% Progress variant="disabled" id="uid" %}
    Fifth step

    {% Slot 'help' %}{% endSlot %}
  {% endProgress %}
{% endProgressIndicator %}
"""
        expected = """
<ul data-progress data-progress-current class="bx--progress bx--progress--vertical">
<li class="bx--progress-step bx--progress-step--complete">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
    height="16" viewBox="0 0 32 32" aria-hidden="true">
  <path d="M14 21.414L9 16.413 10.413 15 14 18.586 21.585 11 23 12.415 14 21.414z"></path>
  <path d="M16,2A14,14,0,1,0,30,16,14,14,0,0,0,16,2Zm0,26A12,12,0,1,1,28,16,12,12,0,0,1,16,28Z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    First step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text"></p>
</div>
<p class="bx--progress-optional">
      Optional
    </p>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--current">
<svg>
  <path d="M 7, 7 m -7, 0 a 7,7 0 1,0 14,0 a 7,7 0 1,0 -14,0" ></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Second Step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text">Overflow Ex.1</p>
</div>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--incomplete">
<svg>
  <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Third Step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text">Overflow Ex. 2 Multi Line</p>
</div>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--incomplete" data-invalid="">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--progress__warning" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M8,1C4.1,1,1,4.1,1,8s3.1,7,7,7s7-3.1,7-7S11.9,1,8,1z M8,14c-3.3,0-6-2.7-6-6s2.7-6,6-6s6,2.7,6,6S11.3,14,8,14z"></path>
  <path d="M7.5 4H8.5V9H7.5zM8 10.2c-.4 0-.8.3-.8.8s.3.8.8.8c.4 0 .8-.3.8-.8S8.4 10.2 8 10.2z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Fourth step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text"></p>
</div>
  <span class="bx--progress-line"></span>
</li>
<li class="bx--progress-step bx--progress-step--disabled bx--progress-step--incomplete" aria-disabled="true">
<svg>
  <path d="M8 1C4.1 1 1 4.1 1 8s3.1 7 7 7 7-3.1 7-7-3.1-7-7-7zm0 13c-3.3 0-6-2.7-6-6s2.7-6 6-6 6 2.7 6 6-2.7 6-6 6z"></path>
</svg>
  <p tabindex="0" class="bx--progress-label" id="uid" aria-describedby="hint-uid">
    Fifth step
  </p>
<div id="hint-uid" role="tooltip" data-floating-menu-direction="bottom"
    class="bx--tooltip" data-avoid-focus-on-open>
  <span class="bx--tooltip__caret"></span>
  <p class="bx--tooltip__text"></p>
</div>
  <span class="bx--progress-line"></span>
</li>
</ul>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
