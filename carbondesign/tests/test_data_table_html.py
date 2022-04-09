# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-many-lines
from django import forms
from django.core.paginator import Paginator
#-
from .base import compare_template, SimpleTestCase

class DummyForm(forms.Form):
    rows = forms.MultipleChoiceField(
            label="Selected rows",
            required=False)


class TableHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_compact(self):
        template = """
{% load carbondesign %}
{% Table variant="compact" %}
  {% Slot 'head' %}
    <tr>
      {% Th %}Name{% endTh %}
      {% Th %}Protocol{% endTh %}
      {% Th %}Port{% endTh %}
      {% Th %}Rule{% endTh %}
      {% Th %}Attached Groups{% endTh %}
      {% Th %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<table class="bx--data-table bx--data-table--compact">
  <thead class="">
    <tr>
<th class="">
  <span class="bx--table-header-label">Name</span>
</th>
<th class="">
  <span class="bx--table-header-label">Protocol</span>
</th>
<th class="">
  <span class="bx--table-header-label">Port</span>
</th>
<th class="">
  <span class="bx--table-header-label">Rule</span>
</th>
<th class="">
  <span class="bx--table-header-label">Attached Groups</span>
</th>
<th class="">
  <span class="bx--table-header-label">Status</span>
</th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
  </tbody>
</table>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_expandable_all(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="expand_all" %}{% endTh %}
      {% Th mode="checkbox" id="bx--checkbox-21" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Ports{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    {% TrExpandable %}
      {% TdCheck form.rows value="green" id="bx--checkbox-13" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}

      {% Slot 'subrow' %}
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
      {% endSlot %}
    {% endTrExpandable %}
    {% TrExpandable %}
      {% TdCheck form.rows value="green" id="bx--checkbox-10" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}

      {% Slot 'subrow' %}
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
      {% endSlot %}
    {% endTrExpandable %}
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
</p>
</div>
<section class="bx--table-toolbar">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-persistent">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem" >
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-expand" data-event="expandAll">
  <button class="bx--table-expand__button">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-expand__svg" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
  </button>
</th>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-21" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-21" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Ports">
    <span class="bx--table-header-label">Ports</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
    </tr>
  </thead>
  <tbody>
<tr class="bx--parent-row" data-parent-row>
  <td class="bx--table-expand" data-event="expand">
    <button class="bx--table-expand__button">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--table-expand__svg" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
      </svg>
    </button>
  </td>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-13"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-13" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
</tr>
<tr class="bx--expandable-row bx--expandable-row--hidden" data-child-row>
  <td colspan="8">
    <div class="bx--child-row-inner-container">
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
    </div>
  </td>
</tr>
<tr class="bx--parent-row" data-parent-row>
  <td class="bx--table-expand" data-event="expand">
    <button class="bx--table-expand__button">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--table-expand__svg" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
      </svg>
    </button>
  </td>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-10"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-10" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
</tr>
<tr class="bx--expandable-row bx--expandable-row--hidden" data-child-row>
  <td colspan="8">
    <div class="bx--child-row-inner-container">
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
    </div>
  </td>
</tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_expandable(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="expandable" %}{% endTh %}
      {% Th mode="checkbox" id="bx--checkbox-21" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Ports{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    {% TrExpandable %}
      {% TdCheck form.rows value="green" id="bx--checkbox-13" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}

      {% Slot 'subrow' %}
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
      {% endSlot %}
    {% endTrExpandable %}
    {% TrExpandable %}
      {% TdCheck form.rows value="green" id="bx--checkbox-10" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}

      {% Slot 'subrow' %}
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
      {% endSlot %}
    {% endTrExpandable %}
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
</p>
</div>
<section class="bx--table-toolbar">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-persistent">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false" >
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem" >
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem" >
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>
  
  <table class="bx--data-table bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-expand" data-event="expandAll">
  <span class="bx--table-header-label"></span>
</th>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-21" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-21" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Ports">
    <span class="bx--table-header-label">Ports</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
    </tr>
  </thead>
  <tbody>
<tr class="bx--parent-row" data-parent-row>
  <td class="bx--table-expand" data-event="expand">
    <button class="bx--table-expand__button">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--table-expand__svg" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
      </svg>
    </button>
  </td>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-13"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-13" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
</tr>
<tr class="bx--expandable-row bx--expandable-row--hidden" data-child-row>
  <td colspan="8">
    <div class="bx--child-row-inner-container">
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
    </div>
  </td>
</tr>
<tr class="bx--parent-row" data-parent-row>
  <td class="bx--table-expand" data-event="expand">
    <button class="bx--table-expand__button">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--table-expand__svg" width="16" height="16"
          viewBox="0 0 16 16" aria-hidden="true">
        <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
      </svg>
    </button>
  </td>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-10"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-10" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
</tr>
<tr class="bx--expandable-row bx--expandable-row--hidden" data-child-row>
  <td colspan="8">
    <div class="bx--child-row-inner-container">
        <p>A variety of content types can live here. Be sure to follow Carbon
            design guidelines for spacing and alignment.</p>
    </div>
  </td>
</tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_row_header(self):
        template = """
{% load carbondesign %}
{% Table %}
  {% Slot 'head' %}
    <tr>
      {% Th %}Name{% endTh %}
      {% Th %}Protocol{% endTh %}
      {% Th %}Port{% endTh %}
      {% Th %}Rule{% endTh %}
      {% Th %}Attached Groups{% endTh %}
      {% Th %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% Th mode="row" %}Load Balancer 1{% endTh %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Th mode="row" %}Load Balancer 5{% endTh %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Th mode="row" %}Load Balancer 5{% endTh %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Th mode="row" %}Load Balancer 5{% endTh %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Th mode="row" %}Load Balancer 5{% endTh %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<table class="bx--data-table">
  <thead class="">
    <tr>
<th class="">
  <span class="bx--table-header-label">Name</span>
</th>
<th class="">
  <span class="bx--table-header-label">Protocol</span>
</th>
<th class="">
  <span class="bx--table-header-label">Port</span>
</th>
<th class="">
  <span class="bx--table-header-label">Rule</span>
</th>
<th class="">
  <span class="bx--table-header-label">Attached Groups</span>
</th>
<th class="">
  <span class="bx--table-header-label">Status</span>
</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" class="">Load Balancer 1</th>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
      <th scope="row" class="">Load Balancer 5</th>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
      <th scope="row" class="">Load Balancer 5</th>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
      <th scope="row" class="">Load Balancer 5</th>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
      <th scope="row" class="">Load Balancer 5</th>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
  </tbody>
</table>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_select(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}Optional Helper Text{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch expandable=True small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="checkbox" id="bx--checkbox-20" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Port{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
      {% Th mode="menu" %}{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-16" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-14" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-15" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-11" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-12" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
  Optional Helper Text
</p>
</div>
<section class="bx--table-toolbar">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-expandable">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier" tabindex="0">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-20" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Port">
    <span class="bx--table-header-label">Port</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
      <th class="bx--table-column-menu"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-16"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-14"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-15"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-11"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-12"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_short_select(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table variant="short" sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}Optional Helper Text{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch expandable=True small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="checkbox" id="bx--checkbox-20" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Port{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
      {% Th mode="menu" %}{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-16" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-14" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-15" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-11" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-12" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
  Optional Helper Text
</p>
</div>
<section class="bx--table-toolbar">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-expandable">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier" tabindex="0">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false" >
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem" >
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--short bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-20" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Port">
    <span class="bx--table-header-label">Port</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
      <th class="bx--table-column-menu"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-16"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-14"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-15"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-11"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-12"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_short(self):
        template = """
{% load carbondesign %}
{% Table variant="short" %}
  {% Slot 'head' %}
    <tr>
      {% Th %}Name{% endTh %}
      {% Th %}Protocol{% endTh %}
      {% Th %}Port{% endTh %}
      {% Th %}Rule{% endTh %}
      {% Th %}Attached Groups{% endTh %}
      {% Th %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<table class="bx--data-table bx--data-table--short">
  <thead class="">
    <tr>
<th class="">
  <span class="bx--table-header-label">Name</span>
</th>
<th class="">
  <span class="bx--table-header-label">Protocol</span>
</th>
<th class="">
  <span class="bx--table-header-label">Port</span>
</th>
<th class="">
  <span class="bx--table-header-label">Rule</span>
</th>
<th class="">
  <span class="bx--table-header-label">Attached Groups</span>
</th>
<th class="">
  <span class="bx--table-header-label">Status</span>
</th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
  </tbody>
</table>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_show_overflow(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table visible_overflow=True sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}Optional Helper Text{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch expandable=True small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="checkbox" id="bx--checkbox-20" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Port{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
      {% Th mode="menu" %}{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-16" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-14" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-15" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-11" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-12" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
  Optional Helper Text
</p>
</div>
<section class="bx--table-toolbar">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-expandable">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier" tabindex="0">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--sort bx--data-table--visible-overflow-menu">
    <thead class="">
    <tr>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-20" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Port">
    <span class="bx--table-header-label">Port</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
      <th class="bx--table-column-menu"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-16"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-14"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-15"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-11"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-12"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_small_select(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table variant="compact" sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}Optional Helper Text{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch expandable=True small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="checkbox" id="bx--checkbox-20" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Port{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
      {% Th mode="menu" %}{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-16" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-14" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-15" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-11" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-12" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
  Optional Helper Text
</p>
</div>
<section class="bx--table-toolbar bx--table-toolbar--small">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary bx--btn--sm" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary bx--btn--sm" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary bx--btn--sm" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary bx--btn--sm" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-expandable">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier" tabindex="0">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false" >
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--compact bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-20" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Port">
    <span class="bx--table-header-label">Port</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
      <th class="bx--table-column-menu"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-16"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-14"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-15"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-11"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-12"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_sticky(self):
        template = """
{% load carbondesign %}
{% Table mode="sticky" %}
  {% Slot 'head' %}
    <tr>
      {% Th %}Name{% endTh %}
      {% Th %}Protocol{% endTh %}
      {% Th %}Port{% endTh %}
      {% Th %}Rule{% endTh %}
      {% Th %}Attached Groups{% endTh %}
      {% Th %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<section class="bx--data-table_inner-container">
  <table class="bx--data-table bx--data-table--sticky-header">
    <thead class="">
    <tr>
<th class="">
  <span class="bx--table-header-label">Name</span>
</th>
<th class="">
  <span class="bx--table-header-label">Protocol</span>
</th>
<th class="">
  <span class="bx--table-header-label">Port</span>
</th>
<th class="">
  <span class="bx--table-header-label">Rule</span>
</th>
<th class="">
  <span class="bx--table-header-label">Attached Groups</span>
</th>
<th class="">
  <span class="bx--table-header-label">Status</span>
</th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
  </tbody>
  </table>
</section>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_tall_select(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table variant="tall" sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}Optional Helper Text{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch expandable=True small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="checkbox" id="bx--checkbox-20" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Port{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
      {% Th mode="menu" %}{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-16" label="Label name" %}
      {% Td %}
        Load Balancer 1
        {% Slot 'secondary' %}
          Secondary Text
        {% endSlot %}
      {% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-14" label="Label name" %}
      {% Td %}
        Load Balancer 5
        {% Slot 'secondary' %}
          Secondary Text
        {% endSlot %}
      {% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-15" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-11" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-12" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
  Optional Helper Text
</p>
</div>
<section class="bx--table-toolbar ">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-expandable">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier" tabindex="0">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false">
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--tall bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-20" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Port">
    <span class="bx--table-header-label">Port</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
      <th class="bx--table-column-menu"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-16"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
        Load Balancer 1
<div class="bx--data-table--cell-secondary-text">
          Secondary Text
</div>
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-14"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
        Load Balancer 5
<div class="bx--data-table--cell-secondary-text">
          Secondary Text
</div>
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-15"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-11"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-12"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_tall(self):
        template = """
{% load carbondesign %}
{% Table variant="tall" %}
  {% Slot 'head' %}
    <tr>
      {% Th %}Name{% endTh %}
      {% Th %}Protocol{% endTh %}
      {% Th %}Port{% endTh %}
      {% Th %}Rule{% endTh %}
      {% Th %}Attached Groups{% endTh %}
      {% Th %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% Td %}
        Load Balancer 1
        {% Slot 'secondary' %}
          Secondary Text
        {% endSlot %}
      {% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}
        Load Balancer 5
        {% Slot 'secondary' %}
          Secondary Text
        {% endSlot %}
      {% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<table class="bx--data-table bx--data-table--tall">
  <thead class="">
    <tr>
<th class="">
  <span class="bx--table-header-label">Name</span>
</th>
<th class="">
  <span class="bx--table-header-label">Protocol</span>
</th>
<th class="">
  <span class="bx--table-header-label">Port</span>
</th>
<th class="">
  <span class="bx--table-header-label">Rule</span>
</th>
<th class="">
  <span class="bx--table-header-label">Attached Groups</span>
</th>
<th class="">
  <span class="bx--table-header-label">Status</span>
</th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="">
        Load Balancer 1
<div class="bx--data-table--cell-secondary-text">
          Secondary Text
</div>
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
        Load Balancer 5
<div class="bx--data-table--cell-secondary-text">
          Secondary Text
</div>
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
  </tbody>
</table>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_with_pager(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        pager = Paginator(range(50), 10)
        context = {'form': form, 'page_first': pager.page(1)}

        template = """
{% load carbondesign %}
{% Table sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="checkbox" id="bx--checkbox-20" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Port{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
      {% Th mode="menu" %}{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-16" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-14" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-15" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-11" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-12" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
  </tbody>

  {% Slot 'pagination' %}
    {% Pagination pager=page_first id="uid" %}
  {% endSlot %}
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
</p>
</div>
<section class="bx--table-toolbar ">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-persistent">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false" >
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-20" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Port">
    <span class="bx--table-header-label">Port</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
      <th class="bx--table-column-menu"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-16"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-14"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>

    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-15"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-11"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-12"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
  </tbody>
  </table>

<div class="bx--pagination" data-pagination data-page-name="page"
    data-pagesize-name="pagesize">
  <div class="bx--pagination__left">
    <label id="select-uid-pagination-count-label" class="bx--pagination__text"
        for="select-uid-pagination-count">
      Items per page:
    </label>
    <div class="bx--select bx--select--inline bx--select__item-count">
      <select class="bx--select-input" id="select-uid-pagination-count"
          aria-label="select number of items per page" tabindex="0"
          data-items-per-page>
<option class="bx--select-option" selected>10</option>
<option class="bx--select-option">20</option>
<option class="bx--select-option">30</option>
<option class="bx--select-option">40</option>
<option class="bx--select-option">50</option>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <span class="bx--pagination__text">
<span data-displayed-item-range>1 – 10</span>
 of <span data-total-items>50</span> items
    </span>
  </div>
  <div class="bx--pagination__right">
    <div class="bx--select bx--select--inline bx--select__page-number">
      <select class="bx--select-input" id="select-uid-pagination-page"
          aria-label="select page number to view" tabindex="0"
          data-page-number-input>
<option class="bx--select-option" selected>1</option>
<option class="bx--select-option">2</option>
<option class="bx--select-option">3</option>
<option class="bx--select-option">4</option>
<option class="bx--select-option">5</option>
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--select__arrow" width="16" height="16" viewBox="0 0 16 16"
          aria-hidden="true">
        <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
      </svg>
    </div>
    <label id="select-uid-pagination-page-label" class="bx--pagination__text"
        for="select-uid-pagination-page">
      of 5 pages
    </label>
    <button class="bx--pagination__button bx--pagination__button--backward"
        tabindex="0" data-page-backward aria-label="previous page">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M20 24L10 16 20 8z"></path>
      </svg>
    </button>
    <button class="bx--pagination__button bx--pagination__button--forward"
        tabindex="0" data-page-forward aria-label="next page">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M12 8L22 16 12 24z"></path>
      </svg>
    </button>
  </div>
</div>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_zebra_select(self):
        form = DummyForm(data={'rows': [1, 2, 3]})
        context = {'form': form}

        template = """
{% load carbondesign %}
{% Table variant="zebra" sortable=True batch_field=form.rows %}
  {% Slot 'title' %}Table title{% endSlot %}
  {% Slot 'description' %}Optional Helper Text{% endSlot %}

  {% Slot 'batch_actions' %}
    {% Button type="button" %}
      Delete

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 32 32">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Save

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
      {% endSlot %}
    {% endButton %}

    {% Button type="button" %}
      Download

      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
            viewBox="0 0 16 16">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'search' %}
    {% TbSearch expandable=True small=True id="search-input-1" %}
  {% endSlot %}

  {% Slot 'toolbar_overflow' %}
    {% TableOvButton active=True %}
      Option 1
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 2
	{% endTableOvButton %}
    {% TableOvButton %}
      Option 3
	{% endTableOvButton %}
  {% endSlot %}

  {% Slot 'toolbar_actions' %}
    {% Button small=True %}
      Primary Button
      {% Slot 'icon' %}
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"
            viewBox="0 0 32 32">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"></path>
        </svg>
      {% endSlot %}
    {% endButton %}
  {% endSlot %}

  {% Slot 'head' %}
    <tr>
      {% Th mode="checkbox" id="bx--checkbox-20" label="Label name" %}{% endTh %}
      {% Th mode="sortable" %}Name{% endTh %}
      {% Th mode="sortable" %}Protocol{% endTh %}
      {% Th mode="sortable" %}Port{% endTh %}
      {% Th mode="sortable" %}Rule{% endTh %}
      {% Th mode="sortable" %}Attached Groups{% endTh %}
      {% Th mode="sortable" %}Status{% endTh %}
      {% Th mode="menu" %}{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-16" label="Label name" %}
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-14" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-15" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-11" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
    <tr>
      {% TdCheck form.rows value="green" id="bx--checkbox-12" label="Label name" %}
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
      {% Td mode="menu" label="Overflow menu description" %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Edit
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Download
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Save
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 16 16">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
        {% TdOvButton tag="button" onclick="console.log('keyboard action')" %}
          Delete
          {% Slot 'icon' %}
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16"
                viewBox="0 0 32 32">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"></path>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"></path>
            </svg>
          {% endSlot %}
        {% endTdOvButton %}
      {% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<div class="bx--data-table-container" data-table>
<div class="bx--data-table-header">
<h4 class="bx--data-table-header__title">
  Table title
</h4>
<p class="bx--data-table-header__description">
  Optional Helper Text
</p>
</div>
<section class="bx--table-toolbar ">
<div class="bx--batch-actions" aria-label="Table Action Bar">
  <div class="bx--action-list">
<button class="bx--btn bx--btn--primary" type="button">
      Delete
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
          <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Save
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z">
          </path>
        </svg>
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Download
  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
        </svg>
</button>
<button class="bx--btn bx--batch-summary__cancel bx--btn--primary" data-event="action-bar-cancel">
  Cancel
</button>
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>3</span> items selected
    </p>
  </div>
</div>
  <div class="bx--toolbar-content">
<div class="bx--toolbar-search-container-expandable">
  <div data-search class="bx--search bx--search--sm" role="search">
    <div class="bx--search-magnifier" tabindex="0">
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
    </div>
    <label id="label-search-input-1" class="bx--label" for="search-input-1">
      Search
    </label>
    <input class="bx--search-input" type="text" id="search-input-1" role="search"
        placeholder="Search" aria-labelledby="label-search-input-1">
    <button class="bx--search-close bx--search-close--hidden"
        title="Clear search input" aria-label="Clear search input">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>

<div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu
    role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
    aria-expanded="false" >
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem"
      data-floating-menu-primary-focus="">
    <div class="bx--overflow-menu-options__option-content">
      Option 1
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 2
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--overflow-menu--data-table"
    role="presentation">
  <button class="bx--overflow-menu-options__btn" role="menuitem">
    <div class="bx--overflow-menu-options__option-content">
      Option 3
    </div>
  </button>
</li>
  </ul>
</div>

<button class="bx--btn bx--btn--primary bx--btn--sm">
      Primary Button
  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="bx--btn__icon">
          <path d="M17 15L17 8 15 8 15 15 8 15 8 17 15 17 15 24 17 24 17 17 24 17 24 15z"/>
        </svg>
</button>
  </div>
</section>

  <table class="bx--data-table bx--data-table--zebra bx--data-table--sort">
    <thead class="">
    <tr>
<th class="bx--table-column-checkbox">
  <input type="checkbox" id="bx--checkbox-20" data-event="select-all" class="bx--checkbox">
  <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Name">
    <span class="bx--table-header-label">Name</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Protocol">
    <span class="bx--table-header-label">Protocol</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Port">
    <span class="bx--table-header-label">Port</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Rule">
    <span class="bx--table-header-label">Rule</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Attached Groups">
    <span class="bx--table-header-label">Attached Groups</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
<th class="">
  <button class="bx--table-sort" data-event="sort" title="Status">
    <span class="bx--table-header-label">Status</span>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-sort__icon-unsorted" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <path d="M27.6 20.6L24 24.2 24 4 22 4 22 24.2 18.4 20.6 17 22 23 28 29 22zM9 4L3 10 4.4 11.4 8 7.8 8 28 10 28 10 7.8 13.6 11.4 15 10z"></path>
    </svg>
  </button>
</th>
      <th class="bx--table-column-menu"></th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-16"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-14"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-15"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-11"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
    <tr>
<td class="bx--table-column-checkbox">
  <input name="rows" value="green" type="checkbox" id="bx--checkbox-12"
      class="bx--checkbox" data-event="select">
  <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
</td>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
<td class="bx--table-column-menu">
  <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description"
      class="bx--overflow-menu" title="Open menu">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Edit" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M2 26H30V28H2zM25.4 9c.8-.8.8-2 0-2.8 0 0 0 0 0 0l-3.6-3.6c-.8-.8-2-.8-2.8 0 0 0 0 0 0 0l-15 15V24h6.4L25.4 9zM20.4 4L24 7.6l-3 3L17.4 7 20.4 4zM6 22v-3.6l10-10 3.6 3.6-10 10H6z"/>
            </svg>
          Edit
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Download" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"/>
            </svg>
          Download
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Save" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5      C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1     h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"/>
            </svg>
          Save
    </div>
  </button>
</li>
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <button class="bx--overflow-menu-options__btn"
      title="Delete" onclick="console.log(&#x27;keyboard action&#x27;)">
    <div class="bx--overflow-menu-options__option-content">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 32 32" focusable="false" preserveAspectRatio="xMidYMid meet" fill="currentColor" style="width:16px;height:16px" aria-hidden="true" class="">
              <path d="M12 12H14V24H12zM18 12H20V24H18z"/>
              <path d="M4 6V8H6V28a2 2 0 002 2H24a2 2 0 002-2V8h2V6zM8 28V8H24V28zM12 2H20V4H12z"/>
            </svg>
          Delete
    </div>
  </button>
</li>
    </ul>
  </div>
</td>
    </tr>
  </tbody>
  </table>
</div>
"""
        rendered = compare_template(template, expected, context)
        self.assertEqual(*rendered)

    def test_zebra(self):
        template = """
{% load carbondesign %}
{% Table variant="zebra" %}
  {% Slot 'head' %}
    <tr>
      {% Th %}Name{% endTh %}
      {% Th %}Protocol{% endTh %}
      {% Th %}Port{% endTh %}
      {% Th %}Rule{% endTh %}
      {% Th %}Attached Groups{% endTh %}
      {% Th %}Status{% endTh %}
    </tr>
  {% endSlot %}
  <tbody>
    <tr>
      {% Td %}Load Balancer 1{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups Testing a really long text here{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
    <tr>
      {% Td %}Load Balancer 5{% endTd %}
      {% Td %}HTTP{% endTd %}
      {% Td %}80{% endTd %}
      {% Td %}Round Robin{% endTd %}
      {% Td %}Maureen’s VM Groups{% endTd %}
      {% Td %}Active{% endTd %}
    </tr>
  </tbody>
{% endTable %}
"""
        expected = """
<table class="bx--data-table bx--data-table--zebra">
  <thead class="">
    <tr>
<th class="">
  <span class="bx--table-header-label">Name</span>
</th>
<th class="">
  <span class="bx--table-header-label">Protocol</span>
</th>
<th class="">
  <span class="bx--table-header-label">Port</span>
</th>
<th class="">
  <span class="bx--table-header-label">Rule</span>
</th>
<th class="">
  <span class="bx--table-header-label">Attached Groups</span>
</th>
<th class="">
  <span class="bx--table-header-label">Status</span>
</th>
    </tr>
  </thead>
  <tbody>
    <tr>
<td class="">
  Load Balancer 1
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups Testing a really long text here
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
    <tr>
<td class="">
  Load Balancer 5
</td>
<td class="">
  HTTP
</td>
<td class="">
  80
</td>
<td class="">
  Round Robin
</td>
<td class="">
  Maureen’s VM Groups
</td>
<td class="">
  Active
</td>
    </tr>
  </tbody>
</table>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
