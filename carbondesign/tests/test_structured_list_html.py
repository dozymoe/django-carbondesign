# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    services = forms.ChoiceField(required=False,
            label="Number input label",
            choices=(
                ('apache spark', "apache spark"),
                ('Cloudant', "Cloudant"),
                ('block-storage', "block-storage"),
                ('open-whisk', "open-whisk"),
            ))


class StructuredListHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% Sl %}
  {% Slot 'header' %}
    {% SlTh %}Column1{% endSlTh %}
    {% SlTh %}Column2{% endSlTh %}
  {% endSlot %}

  {% SlTr %}
    {% SlTd nowrap=True %}Row 1{% endSlTd %}
    {% SlTd %}
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue.
    {% endSlTd %}
  {% endSlTr %}

  {% SlTr %}
    {% SlTd nowrap=True %}Row 2{% endSlTd %}
    {% SlTd %}
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue. Aenean posuere sem vel
      euismod dignissim. Nulla ut cursus dolor. Pellentesque vulputate nisl a
      porttitor interdum.
    {% endSlTd %}
  {% endSlTr %}
{% endSl %}
"""
        expected = """
<section class="bx--structured-list">
  <div class="bx--structured-list-thead">
    <div class="bx--structured-list-row bx--structured-list-row--header-row">
<div class="bx--structured-list-th">Column1</div>
<div class="bx--structured-list-th">Column2</div>
    </div>
  </div>
  <div class="bx--structured-list-tbody">
<div class="bx--structured-list-row">
<div class="bx--structured-list-td bx--structured-list-content--nowrap">
  Row 1
</div>
<div class="bx--structured-list-td">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue.
</div>
</div>
<div class="bx--structured-list-row">
<div class="bx--structured-list-td bx--structured-list-content--nowrap">
  Row 2
</div>
<div class="bx--structured-list-td">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue. Aenean posuere sem vel
      euismod dignissim. Nulla ut cursus dolor. Pellentesque vulputate nisl a
      porttitor interdum.
</div>
</div>
  </div>
</section>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_selection(self):
        form = DummyForm(data={'services': 'apache spark'})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% SlSelect form.services %}
  {% Slot 'header' %}
    {% SlTh %}Column1{% endSlTh %}
    {% SlTh %}Column2{% endSlTh %}
    {% SlTh %}{% endSlTh %}
  {% endSlot %}

  {% SlTr value="apache spark" %}
    {% SlTd nowrap=True %}Row 1{% endSlTd %}
    {% SlTd %}
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue.
    {% endSlTd %}
  {% endSlTr %}

  {% SlTr value="Cloudant" %}
    {% SlTd nowrap=True %}Row 2{% endSlTd %}
    {% SlTd %}
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue. Aenean posuere sem vel
      euismod dignissim. Nulla ut cursus dolor. Pellentesque vulputate nisl a
      porttitor interdum.
    {% endSlTd %}
  {% endSlTr %}

  {% SlTr value="block-storage" %}
    {% SlTd nowrap=True %}Row 3{% endSlTd %}
    {% SlTd %}
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue.
    {% endSlTd %}
  {% endSlTr %}

  {% SlTr value="open-whisk" %}
    {% SlTd nowrap=True %}Row 4{% endSlTd %}
    {% SlTd %}
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue. Aenean posuere sem vel
      euismod dignissim. Nulla ut cursus dolor. Pellentesque vulputate nisl a
      porttitor interdum.
    {% endSlTd %}
  {% endSlTr %}
{% endSlSelect %}
"""
        expected = """
<section class="bx--structured-list bx--structured-list--selection"
    data-structured-list>
  <div class="bx--structured-list-thead">
    <div class="bx--structured-list-row bx--structured-list-row--header-row">
<div class="bx--structured-list-th">Column1</div>
<div class="bx--structured-list-th">Column2</div>
<div class="bx--structured-list-th"></div>
    </div>
  </div>
  <div class="bx--structured-list-tbody">
<label class="bx--structured-list-row bx--structured-list-row--selected" tabindex="0" aria-label="apache spark">
<div class="bx--structured-list-td bx--structured-list-content--nowrap">
  Row 1
</div>
<div class="bx--structured-list-td">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue.
</div>
  <input tabindex="-1" class="bx--structured-list-input" value="apache spark"
      type="radio" name="services" checked="" title="apache spark">
  <div class="bx--structured-list-td">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--structured-list-svg" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
  </div>
</label>
<label class="bx--structured-list-row" tabindex="0" aria-label="Cloudant">
<div class="bx--structured-list-td bx--structured-list-content--nowrap">
  Row 2
</div>
<div class="bx--structured-list-td">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue. Aenean posuere sem vel
      euismod dignissim. Nulla ut cursus dolor. Pellentesque vulputate nisl a
      porttitor interdum.
</div>
  <input tabindex="-1" class="bx--structured-list-input" value="Cloudant"
      type="radio" name="services" title="Cloudant">
  <div class="bx--structured-list-td">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--structured-list-svg" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
  </div>
</label>
<label class="bx--structured-list-row" tabindex="0" aria-label="block-storage">
<div class="bx--structured-list-td bx--structured-list-content--nowrap">
  Row 3
</div>
<div class="bx--structured-list-td">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue.
</div>
  <input tabindex="-1" class="bx--structured-list-input" value="block-storage"
      type="radio" name="services" title="block-storage">
  <div class="bx--structured-list-td">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--structured-list-svg" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
  </div>
</label>
<label class="bx--structured-list-row" tabindex="0" aria-label="open-whisk">
<div class="bx--structured-list-td bx--structured-list-content--nowrap">
  Row 4
</div>
<div class="bx--structured-list-td">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc dui magna,
      finibus id tortor sed, aliquet bibendum augue. Aenean posuere sem vel
      euismod dignissim. Nulla ut cursus dolor. Pellentesque vulputate nisl a
      porttitor interdum.
</div>
  <input tabindex="-1" class="bx--structured-list-input" value="open-whisk"
      type="radio" name="services" title="open-whisk">
  <div class="bx--structured-list-td">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--structured-list-svg" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
  </div>
</label>
  </div>
</section>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)
