"""Implements Carbon Design Component: Data Table
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class DataTable(Node):
    """Data Table component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('head', 'foot')
    "Named children."
    MODES = ('default', 'sticky')
    "Available variants."
    NODE_PROPS = ('style', 'pager', 'pager_sizes')
    "Extended Template Tag arguments."
    AVAILABLE_STYLES = ('compact', 'short', 'tall', 'zebra')
    "Documentation only."
    PAGER_SIZES = (10, 20, 30, 40, 50)

    def prepare(self, values, context):
        style = self.eval(self.kwargs.get('style'), context)
        if style:
            values['class'].append('bx--data-table--%s' % style)


    def render_default(self, values, context, slots):
        values['tmpl_pagination'] = self.render_tmpl_pagination(values, context)

        template = """
<table class="bx--data-table {class}" {props}>
  {slot_head}
  {child}
  {slot_foot}
</table>
{tmpl_pagination}
"""
        return self.format(template, values, slots)


    def render_sticky(self, values, context, slots):
        values['tmpl_pagination'] = self.render_tmpl_pagination(values, context)

        template = """
<section class="bx--data-table_inner-container">
  <table class="bx--data-table bx--data-table--sticky-header {class}" {props}>
    {slot_head}}
    {child}
    {slot_foot}
  </table>
</section>
{tmpl_pagination}
"""
        return self.format(template, values, slots)


    def render_slot_head(self, values, context):
        template = '<thead class="{class}" {props}>{child}</thead>'
        return self.format(template, values)


    def render_slot_foot(self, values, context):
        template = '<tfoot class="{class}" {props}>{child}</tfoot>'
        return self.format(template, values)


    def render_pagination_sizes(self, pager, context):
        template = """
<option class="bx--select-option" value="{value}" {props}>
  {label}
</option>
"""
        options = []

        pager_sizes = self.eval(self.kwargs.get('pager_sizes',
                self.PAGER_SIZES), context)
        if isinstance(pager_sizes, str):
            pager_sizes = [int(x) for x in pager_sizes.split(',')]

        for ii, value in pager_sizes:
            if ii:
                options.append(template.format(
                        {
                            'value': value,
                            'label': value,
                        }))
            else:
                options.append(template.format(
                        {
                            'value': value,
                            'label': value,
                            'props': 'selected',
                        }))
        return ''.join(options)


    def render_pagination_numbers(self, pager, context):
        template = """
<option class="bx--select-option" value="{value}" {props}>
  {label}
</option>
"""
        options = []

        for value in (x + 1 for x in range(pager.num_pages)):
            if value != pager.number:
                options.append(template.format(
                        {
                            'value': value,
                            'label': value,
                        }))
            else:
                options.append(template.format(
                        {
                            'value': value,
                            'label': value,
                            'props': 'selected',
                        }))
        return ''.join(options)


    def render_pagination_of_items(self, pager, context):
        template = """
<span data-displayed-item-range>{range_start}-{range_end}</span>
"""
        page_range = template.format(
                {
                    'range_start': pager.page_range[0],
                    'range_end': pager.page_range[1],
                })
        template = '<span data-total-items>{total}</span>'
        page_total = template.format(
                {
                    'total': pager.count,
                })

        range_of_items = _("%s of %s items")
        return range_of_items % (page_range, page_total)


    def render_pagination_num_pages(self, pager, context):
        num_pages = _("of %s pages")
        return num_pages % pager.num_pages


    def render_tmpl_pagination(self, values, context):
        pager = self.eval(self.kwargs.get('pager'), context)
        if not pager:
            return ''
        if not pager.has_previous and not pager.has_next:
            return ''

        values['txt_per_page'] = _("Items per page")
        values['txt_select_per_page'] = _("select number of items per page") # pylint:disable=line-too-long
        values['txt_select_page_num'] = _("select page number to view")
        values['txt_back_btn'] = _("Backward button")
        values['txt_forw_btn'] = _("Forward button")

        values['tmpl_pagination_sizes'] = self.render_pagination_sizes(pager,
                context)
        values['tmpl_pagination_numbers'] = self.render_pagination_numbers(
                pager, context)
        values['tmpl_pagination_range'] = self.render_pagination_of_items(pager,
                context)
        values['tmpl_pagination_num_pages'] = self.render_pagination_num_pages(
                pager, context)

        template = """
<div class="bx--pagination" data-pagination>
  <div class="bx--pagination__left">
    <label id="select-{id}-pagination-count-label" class="bx--pagination__text"
        for="select-{id}-pagination-count">
      {txt_per_page}:
    </label>
    <div class="bx--select bx--select--inline bx--select__item-count">
      <select class="bx--select-input" id="select-{id}-pagination-count"
          aria-label="{txt_select_per_page}" tabindex="0"
          data-items-per-page>
        {tmpl_pagination_sizes}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          class="bx--select__arrow" width="10" height="6" viewBox="0 0 10 6"
          aria-hidden="true">
        <path d="M5 6L0 1 0.7 0.3 5 4.6 9.3 0.3 10 1z"></path>
      </svg>
    </div>
    <span class="bx--pagination__text">
      {tmpl_pagination_range}
    </span>
  </div>
  <div class="bx--pagination__right">
    <div class="bx--select bx--select--inline bx--select__page-number">
      <select class="bx--select-input" id="select-{id}-pagination-page"
          aria-label="{txt_select_page_num}" tabindex="0"
          data-page-number-input>
        {tmpl_pagination_numbers}
      </select>
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          class="bx--select__arrow" width="10" height="6" viewBox="0 0 10 6"
          aria-hidden="true">
        <path d="M5 6L0 1 0.7 0.3 5 4.6 9.3 0.3 10 1z"></path>
      </svg>
    </div>
    <label id="select-{id}-pagination-page-label" class="bx--pagination__text"
        for="select-{id}-pagination-page">
      {tmpl_pagination_num_pages}
    </label>
    <button class="bx--pagination__button bx--pagination__button--backward"
        tabindex="0" data-page-backward aria-label="{txt_back_btn}">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M19 23L11 16 19 9 19 23z"></path>
      </svg>
    </button>
    <button class="bx--pagination__button bx--pagination__button--forward"
        tabindex="0" data-page-forward aria-label="{txt_forw_btn}">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          style="will-change: transform;" xmlns="http://www.w3.org/2000/svg"
          class="bx--pagination__nav-arrow" width="20" height="20"
          viewBox="0 0 32 32" aria-hidden="true">
        <path d="M13 9L21 16 13 23 13 9z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        return self.format(template, values)

'''
<!--
  Copyright IBM Corp. 2016, 2018

  This source code is licensed under the Apache-2.0 license found in the
  LICENSE file in the root directory of this source tree.
-->
<!-- v10 Data Table -->
  <div class="bx--data-table-container " data-table>
    <div class="bx--data-table-header">
      <h4 class="bx--data-table-header__title">Table title</h4>
      <p class="bx--data-table-header__description"></p>
    </div>
    <!-- Toolbar Content -->
    <section class="bx--table-toolbar ">
      <!-- Batch actions -->
      <div class="bx--batch-actions" aria-label="Table Action Bar">
          <div class="bx--action-list">
            <button class="bx--btn bx--btn--primary" type="button">
              Delete
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg>
            </button>
            <button class="bx--btn bx--btn--primary" type="button">
              Save
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg>
            </button>
            <button class="bx--btn bx--btn--primary" type="button">
              Download
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg>
            </button>
            <button data-event="action-bar-cancel" class="bx--btn bx--btn--primary bx--batch-summary__cancel">Cancel</button>
          </div>
        <div class="bx--batch-summary">
          <p class="bx--batch-summary__para">
          <span data-items-selected>3</span> items selected
        </p>
        </div>
      </div>

     <div class="bx--toolbar-content">
          <!--  Default hidden search -->

            <!-- Persistent Search -->
            <div class="bx--toolbar-search-container-persistent">
              <div data-search class="bx--search bx--search--sm" role="search">
                <div class="bx--search-magnifier">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path></svg>
                </div>
                <label id="search-input-label-1" class="bx--label" for="search__input-2">Search</label>
                <input class="bx--search-input" type="text" id="search__input-2" role="search" placeholder="Search" aria-labelledby="search-input-label-1">
                <button class="bx--search-close bx--search-close--hidden" title="Clear search input" aria-label="Clear search input">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12 4.7L11.3 4 8 7.3 4.7 4 4 4.7 7.3 8 4 11.3 4.7 12 8 8.7 11.3 12 12 11.3 8.7 8z"></path></svg>
                </button>
              </div>
            </div>

            <!-- Toolbar Overflow Menu -->
            <div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
              aria-expanded="false" >
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path><path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path></svg>
              <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1" role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
                <li class="bx--overflow-menu-options__option  bx--overflow-menu--data-table " role="presentation">
                  <button class="bx--overflow-menu-options__btn" role="menuitem"  data-floating-menu-primary-focus >
                    <div class="bx--overflow-menu-options__option-content">
                    Option 1
                    </div>
                  </button>
                </li>
                <li class="bx--overflow-menu-options__option  bx--overflow-menu--data-table " role="presentation">
                  <button class="bx--overflow-menu-options__btn" role="menuitem" >
                    <div class="bx--overflow-menu-options__option-content">
                    Option 2
                    </div>
                  </button>
                </li>
                <li class="bx--overflow-menu-options__option  bx--overflow-menu--data-table " role="presentation">
                  <button class="bx--overflow-menu-options__btn" role="menuitem" >
                    <div class="bx--overflow-menu-options__option-content">
                    Option 3
                    </div>
                  </button>
                </li>
              </ul>
            </div>

          <!--  Toolbar primary button -->
          <button class="bx--btn bx--btn--sm bx--btn--primary">
             Primary Button 
            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="20" height="20" viewBox="0 0 32 32" aria-hidden="true"><path d="M17 15L17 7 15 7 15 15 7 15 7 17 15 17 15 25 17 25 17 17 25 17 25 15 17 15z"></path></svg>
          </button>
      </div>
    </section>
  <!-- End Toolbar Content -->

  <!-- Table -->
  <table class="bx--data-table  bx--data-table--sort  " >
    <thead>
      <tr>
          <th  class="bx--table-column-checkbox">
            <!-- checkbox th -->
              <input data-event="select-all" id="bx--checkbox-20" class="bx--checkbox" type="checkbox" value="green" name="checkbox-20">
              <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
          </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Name">
                  <span class="bx--table-header-label">Name</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Protocol">
                  <span class="bx--table-header-label">Protocol</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Port">
                  <span class="bx--table-header-label">Port</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Rule">
                  <span class="bx--table-header-label">Rule</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Attached Groups">
                  <span class="bx--table-header-label">Attached Groups</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Status">
                  <span class="bx--table-header-label">Status</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th  class="bx--table-column-menu">
            <!-- checkbox th -->
          </th>
      </tr>
    </thead>
  <tbody>
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-16" class="bx--checkbox" type="checkbox" value="green" name="checkbox-16" >
                <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 1
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups Testing a really long text here
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-14" class="bx--checkbox" type="checkbox" value="green" name="checkbox-14" >
                <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-15" class="bx--checkbox" type="checkbox" value="green" name="checkbox-15" >
                <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-11" class="bx--checkbox" type="checkbox" value="green" name="checkbox-11" >
                <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-12" class="bx--checkbox" type="checkbox" value="green" name="checkbox-12" >
                <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
    </tbody>
  </table>

  <!-- Pagination -->
  <div class="bx--pagination" data-pagination>
    <div class="bx--pagination__left">
      <label
         id="select-id-pagination-count-label"
         class="bx--pagination__text"
         for="select-id-pagination-count"
       >
         Items per page:
       </label>
       <div class="bx--select bx--select--inline bx--select__item-count">
         <select
           class="bx--select-input"
           id="select-id-pagination-count"
           aria-label="select number of items per page"
           tabindex="0"
           data-items-per-page
         >
           <option class="bx--select-option" value="10" selected>10</option>
           <option class="bx--select-option" value="20">20</option>
           <option class="bx--select-option" value="30">30</option>
           <option class="bx--select-option" value="40">40</option>
           <option class="bx--select-option" value="50">50</option>
         </select>
         <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--select__arrow" width="10" height="6" viewBox="0 0 10 6" aria-hidden="true"><path d="M5 6L0 1 0.7 0.3 5 4.6 9.3 0.3 10 1z"></path></svg>
      </div>
      <span class="bx--pagination__text">
         <span data-displayed-item-range>1-10</span> of
         <span data-total-items>50</span> items
      </span>
    </div>
    <div class="bx--pagination__right">
       <div class="bx--select bx--select--inline bx--select__page-number">
         <select
           class="bx--select-input"
           id="select-id-pagination-page"
           aria-label="select page number to view"
           tabindex="0"
           data-page-number-input
         >
           <option class="bx--select-option" value="1" selected>1</option>
           <option class="bx--select-option" value="2">2</option>
           <option class="bx--select-option" value="3">3</option>
           <option class="bx--select-option" value="4">4</option>
           <option class="bx--select-option" value="5">5</option>
         </select>
         <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--select__arrow" width="10" height="6" viewBox="0 0 10 6" aria-hidden="true"><path d="M5 6L0 1 0.7 0.3 5 4.6 9.3 0.3 10 1z"></path></svg>
       </div>
       <label
        id="select-id-pagination-page-label"
        class="bx--pagination__text"
        for="select-id-pagination-page"
      >
        of 5 pages
      </label>
      <button class="bx--pagination__button bx--pagination__button--backward" tabindex="0" data-page-backward aria-label="Backward button">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--pagination__nav-arrow" width="20" height="20" viewBox="0 0 32 32" aria-hidden="true"><path d="M19 23L11 16 19 9 19 23z"></path></svg>
      </button>
      <button class="bx--pagination__button bx--pagination__button--forward" tabindex="0" data-page-forward aria-label="Forward button">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--pagination__nav-arrow" width="20" height="20" viewBox="0 0 32 32" aria-hidden="true"><path d="M13 9L21 16 13 23 13 9z"></path></svg>
      </button>
    </div>
  </div>
</div>
'''

'''
<!--
  Copyright IBM Corp. 2016, 2018

  This source code is licensed under the Apache-2.0 license found in the
  LICENSE file in the root directory of this source tree.
-->
<!-- v10 Data Table -->
  <div class="bx--data-table-container " data-table>
    <div class="bx--data-table-header">
      <h4 class="bx--data-table-header__title">Table title</h4>
      <p class="bx--data-table-header__description">Optional Helper Text</p>
    </div>
    <!-- Toolbar Content -->
    <section class="bx--table-toolbar ">
      <!-- Batch actions -->
      <div class="bx--batch-actions" aria-label="Table Action Bar">
          <div class="bx--action-list">
            <button class="bx--btn bx--btn--primary" type="button">
              Delete
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg>
            </button>
            <button class="bx--btn bx--btn--primary" type="button">
              Save
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg>
            </button>
            <button class="bx--btn bx--btn--primary" type="button">
              Download
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg>
            </button>
            <button data-event="action-bar-cancel" class="bx--btn bx--btn--primary bx--batch-summary__cancel">Cancel</button>
          </div>
        <div class="bx--batch-summary">
          <p class="bx--batch-summary__para">
          <span data-items-selected>3</span> items selected
        </p>
        </div>
      </div>

     <div class="bx--toolbar-content">
          <!--  Default hidden search -->
           <div class="bx--toolbar-search-container-expandable">
             <div data-search class="bx--search bx--search--sm" role="search">
               <div class="bx--search-magnifier" tabindex="0">
                 <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path></svg>
               </div>
               <label id="search-input-label-1" class="bx--label" for="search__input-2">Search</label>
                <input class="bx--search-input" type="text" id="search__input-2" role="search" placeholder="Search" aria-labelledby="search-input-label-1">
                <button class="bx--search-close bx--search-close--hidden" title="Clear search input" aria-label="Clear search input">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12 4.7L11.3 4 8 7.3 4.7 4 4 4.7 7.3 8 4 11.3 4.7 12 8 8.7 11.3 12 12 11.3 8.7 8z"></path></svg>
                </button>
              </div>
            </div>

            <!-- Persistent Search -->

            <!-- Toolbar Overflow Menu -->
            <div class="bx--overflow-menu bx--toolbar-action" data-overflow-menu role="button" tabindex="0" aria-label="Overflow" aria-haspopup="true"
              aria-expanded="false" >
              <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path><path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path></svg>
              <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1" role="menu" aria-label="Overflow" data-floating-menu-direction="bottom">
                <li class="bx--overflow-menu-options__option  bx--overflow-menu--data-table " role="presentation">
                  <button class="bx--overflow-menu-options__btn" role="menuitem"  data-floating-menu-primary-focus >
                    <div class="bx--overflow-menu-options__option-content">
                    Option 1
                    </div>
                  </button>
                </li>
                <li class="bx--overflow-menu-options__option  bx--overflow-menu--data-table " role="presentation">
                  <button class="bx--overflow-menu-options__btn" role="menuitem" >
                    <div class="bx--overflow-menu-options__option-content">
                    Option 2
                    </div>
                  </button>
                </li>
                <li class="bx--overflow-menu-options__option  bx--overflow-menu--data-table " role="presentation">
                  <button class="bx--overflow-menu-options__btn" role="menuitem" >
                    <div class="bx--overflow-menu-options__option-content">
                    Option 3
                    </div>
                  </button>
                </li>
              </ul>
            </div>

          <!--  Toolbar primary button -->
          <button class="bx--btn bx--btn--sm bx--btn--primary">
             Primary Button
            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--btn__icon" width="20" height="20" viewBox="0 0 32 32" aria-hidden="true"><path d="M17 15L17 7 15 7 15 15 7 15 7 17 15 17 15 25 17 25 17 17 25 17 25 15 17 15z"></path></svg>
          </button>
      </div>
    </section>
  <!-- End Toolbar Content -->

  <!-- Table -->
  <table class="bx--data-table  bx--data-table--sort  " >
    <thead>
      <tr>
          <th  class="bx--table-column-checkbox">
            <!-- checkbox th -->
              <input data-event="select-all" id="bx--checkbox-20" class="bx--checkbox" type="checkbox" value="green" name="checkbox-20">
              <label for="bx--checkbox-20" class="bx--checkbox-label" aria-label="Label name"></label>
          </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Name">
                  <span class="bx--table-header-label">Name</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Protocol">
                  <span class="bx--table-header-label">Protocol</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Port">
                  <span class="bx--table-header-label">Port</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Rule">
                  <span class="bx--table-header-label">Rule</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Attached Groups">
                  <span class="bx--table-header-label">Attached Groups</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th >
            <!-- checkbox th -->
            <!-- sortable th  -->
                <button class="bx--table-sort" data-event="sort" title="Status">
                  <span class="bx--table-header-label">Status</span>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M12.3 9.3L8.5 13.1 8.5 1 7.5 1 7.5 13.1 3.7 9.3 3 10 8 15 13 10z"></path></svg>
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--table-sort__icon-unsorted" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.8 10.3L12 12.1 12 2 11 2 11 12.1 9.2 10.3 8.5 11 11.5 14 14.5 11zM4.5 2L1.5 5 2.2 5.7 4 3.9 4 14 5 14 5 3.9 6.8 5.7 7.5 5z"></path></svg>
                </button>
              <!-- no sort th -->
                        </th>
          <th  class="bx--table-column-menu">
            <!-- checkbox th -->
          </th>
      </tr>
    </thead>
  <tbody>
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-16" class="bx--checkbox" type="checkbox" value="green" name="checkbox-16" >
                <label for="bx--checkbox-16" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 1
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups Testing a really long text here
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-14" class="bx--checkbox" type="checkbox" value="green" name="checkbox-14" >
                <label for="bx--checkbox-14" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-15" class="bx--checkbox" type="checkbox" value="green" name="checkbox-15" >
                <label for="bx--checkbox-15" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-11" class="bx--checkbox" type="checkbox" value="green" name="checkbox-11" >
                <label for="bx--checkbox-11" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
      <tr >
          <!-- expand icon td -->
              <td class="bx--table-column-checkbox">
                <input data-event="select" id="bx--checkbox-12" class="bx--checkbox" type="checkbox" value="green" name="checkbox-12" >
                <label for="bx--checkbox-12" class="bx--checkbox-label" aria-label="Label name"></label>
              </td>
            <!-- inline action td's -->
          <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Load Balancer 5
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  HTTP
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  80
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Round Robin
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Maureen’s VM Groups
              </td>
                      <!-- expand icon td -->
              <td >
                <!-- truncated new markup -->
                  Active
              </td>
                      <!-- expand icon td -->
              <td class="bx--table-column-menu">
                <div data-overflow-menu role="menu" tabindex="0" aria-label="Overflow menu description" class="bx--overflow-menu">
                  <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" class="bx--overflow-menu__icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="3" r="1"></circle><circle cx="8" cy="8" r="1"></circle><circle cx="8" cy="13" r="1"></circle></svg>
                  <ul class="bx--overflow-menu-options bx--overflow-menu--flip">

                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                           <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M1 13H15V14H1zM12.7 4.5c.4-.4.4-1 0-1.4 0 0 0 0 0 0l-1.8-1.8c-.4-.4-1-.4-1.4 0 0 0 0 0 0 0L2 8.8V12h3.2L12.7 4.5zM10.2 2L12 3.8l-1.5 1.5L8.7 3.5 10.2 2zM3 11V9.2l5-5L9.8 6l-5 5H3z"></path></svg> Edit
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13 7L12.3 6.3 8.5 10.1 8.5 1 7.5 1 7.5 10.1 3.7 6.3 3 7 8 12zM13 12v2H3v-2H2v2l0 0c0 .6.4 1 1 1h10c.6 0 1-.4 1-1l0 0v-2H13z"></path></svg> Download
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M13.9,4.6l-2.5-2.5C11.3,2.1,11.1,2,11,2H3C2.4,2,2,2.4,2,3v10c0,0.6,0.4,1,1,1h10c0.6,0,1-0.4,1-1V5	C14,4.9,13.9,4.7,13.9,4.6z M6,3h4v2H6V3z M10,13H6V9h4V13z M11,13V9c0-0.6-0.4-1-1-1H6C5.4,8,5,8.4,5,9v4H3V3h2v2c0,0.6,0.4,1,1,1	h4c0.6,0,1-0.4,1-1V3.2l2,2V13H11z"></path></svg> Save
                          </div>
                        </button>
                      </li>
                      <li class="bx--overflow-menu-options__option bx--table-row--menu-option">
                        <button class="bx--overflow-menu-options__btn" onclick="console.log('keyboard action')">
                          <div class="bx--overflow-menu-options__option-content">
                            <svg focusable="false" preserveAspectRatio="xMidYMid meet" style="will-change: transform;" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true"><path d="M6 6H7V12H6zM9 6H10V12H9z"></path><path d="M2 3v1h1v10c0 .6.4 1 1 1h8c.6 0 1-.4 1-1V4h1V3H2zM4 14V4h8v10H4zM6 1H10V2H6z"></path></svg> Delete
                          </div>
                        </button>
                      </li>

                  </ul>
                </div>
              </td>
            <!-- inline edit tds -->
      </tr>
      <!-- Expandable child row -->
    </tbody>
  </table>

  <!-- Pagination -->
</div>
'''


class Th(Node):

    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def render_default(self, values, context, slots):
        template = """
<th class="{class}" {props}>
  <span class="bx--table-header-label">{child}</span>
</th>
"""
        return self.format(template, values, slots)


class Td(Node):

    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('secondary',)
    "Named children."


    def render_default(self, values, context, slots):
        template = """
<td class="{class}" {props}>
  {child}
  {slot_secondary}
</td>
"""
        return self.format(template, values, slots)


    def render_slot_secondary(self, values, context):
        template = """
<div class="bx--data-table--cell-secondary-text {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


components = {
    'DataTable': DataTable,
    'Th': Th,
    'Td': Td,
}
