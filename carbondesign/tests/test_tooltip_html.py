# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long
from .base import compare_template, SimpleTestCase

class TooltipHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% InteractiveTooltip id="example-ubxquesph4" label="Tooltip label" %}
  This is some tooltip text. This box shows the maximum amount of text that
  should appear inside. If more room is needed please use a modal instead.

  {% Slot 'footer' %}
    {% Link href="#" %}Learn More{% endLink %}
    {% Button type="button" small=True %}Create{% endButton %}
  {% endSlot %}

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 16 16">
      <path d="M8.5 11L8.5 6.5 6.5 6.5 6.5 7.5 7.5 7.5 7.5 11 6 11 6 12 10 12 10 11zM8 3.5c-.4 0-.8.3-.8.8S7.6 5 8 5c.4 0 .8-.3.8-.8S8.4 3.5 8 3.5z"/>
      <path d="M8,15c-3.9,0-7-3.1-7-7s3.1-7,7-7s7,3.1,7,7S11.9,15,8,15z M8,2C4.7,2,2,4.7,2,8s2.7,6,6,6s6-2.7,6-6S11.3,2,8,2z"/>
    </svg>
  {% endSlot %}
{% endInteractiveTooltip %}
"""
        expected = """
<div id="label-example-ubxquesph4" class="bx--tooltip__label">
  Tooltip label
  <button aria-expanded="false" aria-labelledby="label-example-ubxquesph4"
      data-tooltip-trigger data-tooltip-target="#example-ubxquesph4"
      class="bx--tooltip__trigger" aria-controls="example-ubxquesph4">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M8.5 11L8.5 6.5 6.5 6.5 6.5 7.5 7.5 7.5 7.5 11 6 11 6 12 10 12 10 11zM8 3.5c-.4 0-.8.3-.8.8S7.6 5 8 5c.4 0 .8-.3.8-.8S8.4 3.5 8 3.5z"/>
      <path d="M8,15c-3.9,0-7-3.1-7-7s3.1-7,7-7s7,3.1,7,7S11.9,15,8,15z M8,2C4.7,2,2,4.7,2,8s2.7,6,6,6s6-2.7,6-6S11.3,2,8,2z"/>
    </svg>
  </button>
</div>
<div id="example-ubxquesph4" aria-hidden="true" data-floating-menu-direction="bottom"
    class="bx--tooltip">
  <span class="bx--tooltip__caret"></span>
  <div class="bx--tooltip__content" tabindex="-1" role="dialog"
      aria-describedby="body-example-ubxquesph4" aria-labelledby="label-example-ubxquesph4">
    <p id="body-example-ubxquesph4">
  This is some tooltip text. This box shows the maximum amount of text that
  should appear inside. If more room is needed please use a modal instead.
</p>
<div class="bx--tooltip__footer">
    <a class="bx--link" href="#">Learn More</a>
<button class="bx--btn bx--btn--primary bx--btn--sm" type="button">
  Create
</button>
</div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_richtext(self):
        template = """
{% load carbondesign %}
{% InteractiveTooltip id="example-hb4qi35jz3c" label="Tooltip label" %}
  {% Slot 'heading' %}
    Heading within a Tooltip
  {% endSlot %}
    
  This is some tooltip text. This box shows the maximum amount of text that
  should appear inside. If more room is needed please use a modal instead.

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 16 16">
      <path d="M8.5 11L8.5 6.5 6.5 6.5 6.5 7.5 7.5 7.5 7.5 11 6 11 6 12 10 12 10 11zM8 3.5c-.4 0-.8.3-.8.8S7.6 5 8 5c.4 0 .8-.3.8-.8S8.4 3.5 8 3.5z"/>
      <path d="M8,15c-3.9,0-7-3.1-7-7s3.1-7,7-7s7,3.1,7,7S11.9,15,8,15z M8,2C4.7,2,2,4.7,2,8s2.7,6,6,6s6-2.7,6-6S11.3,2,8,2z"/>
    </svg>
  {% endSlot %}
{% endInteractiveTooltip %}
"""
        expected = """
<div id="label-example-hb4qi35jz3c" class="bx--tooltip__label">
  Tooltip label
  <button aria-expanded="false" aria-labelledby="label-example-hb4qi35jz3c"
      data-tooltip-trigger data-tooltip-target="#example-hb4qi35jz3c"
      class="bx--tooltip__trigger" aria-controls="example-hb4qi35jz3c">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M8.5 11L8.5 6.5 6.5 6.5 6.5 7.5 7.5 7.5 7.5 11 6 11 6 12 10 12 10 11zM8 3.5c-.4 0-.8.3-.8.8S7.6 5 8 5c.4 0 .8-.3.8-.8S8.4 3.5 8 3.5z"/>
      <path d="M8,15c-3.9,0-7-3.1-7-7s3.1-7,7-7s7,3.1,7,7S11.9,15,8,15z M8,2C4.7,2,2,4.7,2,8s2.7,6,6,6s6-2.7,6-6S11.3,2,8,2z"/>
    </svg>
  </button>
</div>
<div id="example-hb4qi35jz3c" aria-hidden="true" data-floating-menu-direction="bottom"
    class="bx--tooltip">
  <span class="bx--tooltip__caret"></span>
  <div class="bx--tooltip__content" tabindex="-1" role="dialog"
      aria-describedby="body-example-hb4qi35jz3c" aria-labelledby="heading-example-hb4qi35jz3c">
<h4 id="heading-example-hb4qi35jz3c" class="bx--tooltip__heading">
    Heading within a Tooltip
  </h4>
    <p id="body-example-hb4qi35jz3c">
  This is some tooltip text. This box shows the maximum amount of text that
  should appear inside. If more room is needed please use a modal instead.
</p>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_nolabel(self):
        template = """
{% load carbondesign %}
{% InteractiveTooltip mode="nolabel" id="example-dqozgv7kk49" label="Tooltip label" %}
  This is some tooltip text. This box shows the maximum amount of text that
  should appear inside. If more room is needed please use a modal instead.

  {% Slot 'footer' %}
    {% Link href="#" %}Learn More{% endLink %}
    {% Button type="button" small=True %}Create{% endButton %}
  {% endSlot %}

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 16 16">
      <path d="M8.5 11L8.5 6.5 6.5 6.5 6.5 7.5 7.5 7.5 7.5 11 6 11 6 12 10 12 10 11zM8 3.5c-.4 0-.8.3-.8.8S7.6 5 8 5c.4 0 .8-.3.8-.8S8.4 3.5 8 3.5z"/>
      <path d="M8,15c-3.9,0-7-3.1-7-7s3.1-7,7-7s7,3.1,7,7S11.9,15,8,15z M8,2C4.7,2,2,4.7,2,8s2.7,6,6,6s6-2.7,6-6S11.3,2,8,2z"/>
    </svg>
  {% endSlot %}
{% endInteractiveTooltip %}
"""
        expected = """
<div id="label-example-dqozgv7kk49" class="bx--tooltip__label">
  Tooltip label
  <div tabindex="0" aria-expanded="false" aria-labelledby="label-example-dqozgv7kk49"
      data-tooltip-trigger data-tooltip-target="#example-dqozgv7kk49"
      role="button" class="bx--tooltip__trigger" aria-controls="example-dqozgv7kk49">
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M8.5 11L8.5 6.5 6.5 6.5 6.5 7.5 7.5 7.5 7.5 11 6 11 6 12 10 12 10 11zM8 3.5c-.4 0-.8.3-.8.8S7.6 5 8 5c.4 0 .8-.3.8-.8S8.4 3.5 8 3.5z"/>
      <path d="M8,15c-3.9,0-7-3.1-7-7s3.1-7,7-7s7,3.1,7,7S11.9,15,8,15z M8,2C4.7,2,2,4.7,2,8s2.7,6,6,6s6-2.7,6-6S11.3,2,8,2z"/>
    </svg>
  </div>
</div>
<div id="example-dqozgv7kk49" aria-hidden="true" data-floating-menu-direction="bottom"
    class="bx--tooltip">
  <span class="bx--tooltip__caret"></span>
  <div class="bx--tooltip__content" tabindex="-1" role="dialog"
      aria-describedby="body-example-dqozgv7kk49" aria-label="Tooltip label">
    <p id="body-example-dqozgv7kk49">
  This is some tooltip text. This box shows the maximum amount of text that
  should appear inside. If more room is needed please use a modal instead.
</p>
<div class="bx--tooltip__footer">
    <a class="bx--link" href="#">Learn More</a>
<button class="bx--btn bx--btn--primary bx--btn--sm" type="button">
  Create
</button>
</div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_definition(self):
        template = """
{% load carbondesign %}
{% DefinitionTooltip id="example-start" label="Definition Tooltip (start aligned)" position="bottom" align="start" %}
  Brief description of the dotted, underlined word above.
{% endDefinitionTooltip %}
<br>
{% DefinitionTooltip id="example-center" label="Definition Tooltip (center aligned)" position="bottom" align="center" %}
  Brief description of the dotted, underlined word above.
{% endDefinitionTooltip %}
<br>
{% DefinitionTooltip id="example-end" label="Definition Tooltip (end aligned)" position="bottom" align="end" %}
  Brief description of the dotted, underlined word above.
{% endDefinitionTooltip %}
"""
        expected = """
<div class="bx--tooltip--definition bx--tooltip--a11y" data-tooltip-definition>
  <button aria-describedby="example-start"
      class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip__trigger--definition bx--tooltip--align-start bx--tooltip--bottom">
    Definition Tooltip (start aligned)
  </button>
  <div class="bx--assistive-text" id="example-start" role="tooltip">
  Brief description of the dotted, underlined word above.
  </div>
</div>
<br>
<div class="bx--tooltip--definition bx--tooltip--a11y" data-tooltip-definition>
  <button aria-describedby="example-center"
      class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip__trigger--definition bx--tooltip--align-center bx--tooltip--bottom">
    Definition Tooltip (center aligned)
  </button>
  <div class="bx--assistive-text" id="example-center" role="tooltip">
  Brief description of the dotted, underlined word above.
  </div>
</div>
<br>
<div class="bx--tooltip--definition bx--tooltip--a11y" data-tooltip-definition>
  <button aria-describedby="example-end"
      class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip__trigger--definition bx--tooltip--align-end bx--tooltip--bottom">
    Definition Tooltip (end aligned)
  </button>
  <div class="bx--assistive-text" id="example-end" role="tooltip">
  Brief description of the dotted, underlined word above.
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


    def test_icon(self):
        template = """
{% load carbondesign %}
<p>start</p>
<br>
{% IconTooltip mode="icon" position="left" align="start" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="top" align="start" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="bottom" align="start" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="right" align="start" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
<br>
<br>
<p>center</p>
<br>
{% IconTooltip mode="icon" position="left" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="top" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="bottom" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="right" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
<br>
<br>
<p>end</p>
<br>
{% IconTooltip mode="icon" position="left" align="end" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="top" align="end" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="bottom" align="end" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
{% IconTooltip mode="icon" position="right" align="end" %}
  Filter

  {% Slot 'icon' %}
    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
        viewBox="0 0 32 32">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
  {% endSlot %}
{% endIconTooltip %}
"""
        expected = """
<p>start</p>
<br>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-start bx--tooltip--left"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-start bx--tooltip--top"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-start bx--tooltip--bottom"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-start bx--tooltip--right"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<br>
<br>
<p>center</p>
<br>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--left"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--top"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--right"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<br>
<br>
<p>end</p>
<br>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-end bx--tooltip--left"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-end bx--tooltip--top"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-end bx--tooltip--bottom"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
<button class="bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--align-end bx--tooltip--right"
    data-tooltip-icon>
  <span class="bx--assistive-text">
  Filter
</span>
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16;height:16" aria-hidden="true">
      <path d="M18,28H14a2,2,0,0,1-2-2V18.41L4.59,11A2,2,0,0,1,4,9.59V6A2,2,0,0,1,6,4H26a2,2,0,0,1,2,2V9.59A2,2,0,0,1,27.41,11L20,18.41V26A2,2,0,0,1,18,28ZM6,6V9.59l8,8V26h4V17.59l8-8V6Z"/>
    </svg>
</button>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
