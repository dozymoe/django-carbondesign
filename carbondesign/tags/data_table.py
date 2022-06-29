"""
Data Table
==========

See: https://www.carbondesignsystem.com/components/data-table/usage/

Data tables are used to organize and display data efficiently. The data table
component allows for customization with additional functionality, as needed by
your product’s users.

Overview
--------

The data table’s features are ideal for organizing and displaying data in a UI.
The column headers can sort data in ascending or descending order, rows can be
expanded to progressively disclose information, and single or batch actions can
be taken on rows.

The data table toolbar gives a location for primary buttons, search, filtering,
table display settings, and other utilities.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

import logging
from uuid import uuid4
#-
from django.utils.translation import gettext as _
#-
from .base import DummyNodeList, FormNode, Node, clean_attr_value, modify_svg
from .button import Button

_logger = logging.getLogger(__name__)


class DataTable(Node):
    """Data Table component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('title', 'description', 'batch_actions', 'search',
            'toolbar_actions', 'toolbar_overflow', 'head', 'foot', 'pagination')
    "Named children."
    MODES = ('default', 'sticky')
    "Available variants."
    NODE_PROPS = ('variant', 'sortable', 'small_toolbar', 'batch_field',
            'visible_overflow')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('toolbar', *Node.CLASS_AND_PROPS)
    "Prepare xxx_class and xxx_props values."
    POSSIBLE_VARIANT = ('compact', 'short', 'tall', 'zebra')
    "Documentation only."
    PAGER_SIZES = (10, 20, 30, 40, 50)

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_batch_actions'] = _("Table Action Bar")
        values['txt_items_selected'] = _("items selected")
        values['txt_overflow'] = _("Overflow")

        variant = self.eval(self.kwargs.get('variant'), context)
        if variant:
            values['class'].append(f'bx--data-table--{variant}')
        if variant == 'compact':
            context['compact'] = True

        if self.eval(self.kwargs.get('sortable'), context):
            values['class'].append('bx--data-table--sort')

        if variant == 'compact' or\
                self.eval(self.kwargs.get('small_toolbar'), context):
            values['toolbar_class'].append('bx--table-toolbar--small')

            self.set_child_props(context, 'button_props', 'batch_actions',
                    small=True)
            self.set_child_props(context, 'search_props', small=True)
            self.set_child_props(context, 'button_props', 'toolbar',
                    small=True)

        if self.eval(self.kwargs.get('visible_overflow'), context):
            values['class'].append('bx--data-table--visible-overflow-menu')


    def render_default(self, values, context):
        """Output html of the component.
        """
        if self.has_tmpl_header() or self.has_tmpl_toolbar():
            template = """
<div class="bx--data-table-container" data-table>
  {tmpl_header}
  {tmpl_toolbar}
  <table class="bx--data-table {class}" {props}>
    {slot_head}
    {child}
    {slot_foot}
  </table>
  {slot_pagination}
</div>
"""
        else:
            template = """
<table class="bx--data-table {class}" {props}>
  {slot_head}
  {child}
  {slot_foot}
</table>
{slot_pagination}
"""
        return self.format(template, values, context)


    def render_sticky(self, values, context):
        """Output html of the component.
        """
        if self.has_tmpl_header() or self.has_tmpl_toolbar():
            template = """
<div class="bx--data-table-container" data-table>
  {tmpl_header}
  {tmpl_toolbar}
  <section class="bx--data-table_inner-container">
    <table class="bx--data-table bx--data-table--sticky-header {class}" {props}>
      {slot_head}
      {child}
      {slot_foot}
    </table>
  </section>
  {slot_pagination}
</div>
"""
        else:
            template = """
<section class="bx--data-table_inner-container">
  <table class="bx--data-table bx--data-table--sticky-header {class}" {props}>
    {slot_head}
    {child}
    {slot_foot}
  </table>
</section>
{slot_pagination}
"""
        return self.format(template, values, context)


    def render_slot_head(self, values, context):
        """Render html of the slot.
        """
        template = '<thead class="{class}" {props}>{child}</thead>'
        return self.format(template, values)


    def render_slot_foot(self, values, context):
        """Render html of the slot.
        """
        template = '<tfoot class="{class}" {props}>{child}</tfoot>'
        return self.format(template, values)


    def render_slot_title(self, values, context):
        """Render html of the slot.
        """
        template = """
<h4 class="bx--data-table-header__title {class}" {props}>
  {child}
</h4>
"""
        return self.format(template, values)


    def render_slot_description(self, values, context):
        """Render html of the slot.
        """
        template = """
<p class="bx--data-table-header__description {class}" {props}>
  {child}
</p>
"""
        return self.format(template, values)


    def render_slot_batch_actions(self, values, context):
        """Render html of the slot.
        """
        cancel_btn = Button(
                DummyNodeList(_("Cancel")),
                **{
                    'variant': 'primary',
                    'data-event': 'action-bar-cancel',
                    'class': 'bx--batch-summary__cancel',
                    'small': context.get('compact'),
                })

        form_field = self.eval(self.kwargs.get('batch_field'), context)
        if form_field and form_field.value():
            values['count'] = len(form_field.value())
        else:
            values['count'] = 0

        template = """
<div class="bx--batch-actions {class}" aria-label="{txt_batch_actions}" {props}>
  <div class="bx--action-list">
    {child}
    {cancel_btn}
  </div>
  <div class="bx--batch-summary">
    <p class="bx--batch-summary__para">
      <span data-items-selected>{count}</span> {txt_items_selected}
    </p>
  </div>
</div>
"""
        return self.format(template,
                dict(values, cancel_btn=cancel_btn.render(context)))


    def render_slot_toolbar_overflow(self, values, context):
        """Render html of the slot.
        """
        template = """
<div class="bx--overflow-menu bx--toolbar-action {class}" data-overflow-menu
    role="button" tabindex="0" aria-label="{txt_overflow}" aria-haspopup="true"
    aria-expanded="false" {props}>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--toolbar-action__icon" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M13.5,8.4c0-0.1,0-0.3,0-0.4c0-0.1,0-0.3,0-0.4l1-0.8c0.4-0.3,0.4-0.9,0.2-1.3l-1.2-2C13.3,3.2,13,3,12.6,3	c-0.1,0-0.2,0-0.3,0.1l-1.2,0.4c-0.2-0.1-0.4-0.3-0.7-0.4l-0.3-1.3C10.1,1.3,9.7,1,9.2,1H6.8c-0.5,0-0.9,0.3-1,0.8L5.6,3.1	C5.3,3.2,5.1,3.3,4.9,3.4L3.7,3C3.6,3,3.5,3,3.4,3C3,3,2.7,3.2,2.5,3.5l-1.2,2C1.1,5.9,1.2,6.4,1.6,6.8l0.9,0.9c0,0.1,0,0.3,0,0.4	c0,0.1,0,0.3,0,0.4L1.6,9.2c-0.4,0.3-0.5,0.9-0.2,1.3l1.2,2C2.7,12.8,3,13,3.4,13c0.1,0,0.2,0,0.3-0.1l1.2-0.4	c0.2,0.1,0.4,0.3,0.7,0.4l0.3,1.3c0.1,0.5,0.5,0.8,1,0.8h2.4c0.5,0,0.9-0.3,1-0.8l0.3-1.3c0.2-0.1,0.4-0.2,0.7-0.4l1.2,0.4	c0.1,0,0.2,0.1,0.3,0.1c0.4,0,0.7-0.2,0.9-0.5l1.1-2c0.2-0.4,0.2-0.9-0.2-1.3L13.5,8.4z M12.6,12l-1.7-0.6c-0.4,0.3-0.9,0.6-1.4,0.8	L9.2,14H6.8l-0.4-1.8c-0.5-0.2-0.9-0.5-1.4-0.8L3.4,12l-1.2-2l1.4-1.2c-0.1-0.5-0.1-1.1,0-1.6L2.2,6l1.2-2l1.7,0.6	C5.5,4.2,6,4,6.5,3.8L6.8,2h2.4l0.4,1.8c0.5,0.2,0.9,0.5,1.4,0.8L12.6,4l1.2,2l-1.4,1.2c0.1,0.5,0.1,1.1,0,1.6l1.4,1.2L12.6,12z"></path>
    <path d="M8,11c-1.7,0-3-1.3-3-3s1.3-3,3-3s3,1.3,3,3C11,9.6,9.7,11,8,11C8,11,8,11,8,11z M8,6C6.9,6,6,6.8,6,7.9C6,7.9,6,8,6,8	c0,1.1,0.8,2,1.9,2c0,0,0.1,0,0.1,0c1.1,0,2-0.8,2-1.9c0,0,0-0.1,0-0.1C10,6.9,9.2,6,8,6C8.1,6,8,6,8,6z"></path>
  </svg>
  <ul class="bx--overflow-menu-options bx--overflow-menu--flip" tabindex="-1"
      role="menu" aria-label="{txt_overflow}" data-floating-menu-direction="bottom">
    {child}
  </ul>
</div>
"""
        return self.format(template, values)


    def has_tmpl_header(self):
        """Should render header template?
        """
        return 'title' in self.slots or 'description' in self.slots

    def render_tmpl_header(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not self.has_tmpl_header():
            return ''

        template = """
<div class="bx--data-table-header">
  {slot_title}
  {slot_description}
</div>
"""
        return self.format(template, values, context)


    def has_tmpl_toolbar(self):
        """Should render toolbar template?
        """
        return 'batch_actions' in self.slots or\
                'toolbar_overflow' in self.slots or\
                'toolbar_actions' in self.slots

    def render_tmpl_toolbar(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if not self.has_tmpl_toolbar():
            return ''

        template = """
<section class="bx--table-toolbar {toolbar_class}" {toolbar_props}>
  {slot_batch_actions}
  <div class="bx--toolbar-content">
    {slot_search}
    {slot_toolbar_overflow}
    {slot_toolbar_actions}
  </div>
</section>
"""
        return self.format(template, values, context)


class TrExpandable(Node):
    """Table row for expandable table.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('subrow',)
    "Named children."

    def render_default(self, values, context):
        """Output html of the component.
        """
        values['total_column'] = values['child'].count('<td') + 1

        template = """
<tr class="bx--parent-row {class}" data-parent-row {props}>
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
  {child}
</tr>
<tr class="bx--expandable-row bx--expandable-row--hidden" data-child-row>
  <td colspan="{total_column}">
    <div class="bx--child-row-inner-container">
      {slot_subrow}
    </div>
  </td>
</tr>
"""
        return self.format(template, values, context)


class Th(Node):
    """Table row heading.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'checkbox', 'sortable', 'menu', 'expandable',
            'expand_all', 'row')
    "Available variants."
    NODE_PROPS = ('id',)
    "Extended Template Tag arguments."

    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<th class="{class}" {props}>
  <span class="bx--table-header-label">{child}</span>
</th>
"""
        return self.format(template, values)


    def render_checkbox(self, values, context):
        """Output html of the component.
        """
        template = """
<th class="bx--table-column-checkbox {class}">
  <input type="checkbox" id="{id}" data-event="select-all" class="bx--checkbox" {props}>
  <label for="{id}" class="bx--checkbox-label" aria-label="{label}{label_suffix}"></label>
</th>
"""
        return self.format(template, values)


    def render_sortable(self, values, context):
        """Output html of the component.
        """
        values['cleaned_child'] = clean_attr_value(values['child'])

        template = """
<th class="{class}" {props}>
  <button class="bx--table-sort" data-event="sort" title="{cleaned_child}">
    <span class="bx--table-header-label">{child}</span>
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
"""
        return self.format(template, values)


    def render_menu(self, values, context):
        """Output html of the component.
        """
        return '<th class="bx--table-column-menu"></th>'


    def render_expandable(self, values, context):
        """Output html of the component.
        """
        template = """
<th class="bx--table-expand {class}" data-event="expandAll" {props}>
  <span class="bx--table-header-label"></span>
</th>
"""
        return self.format(template, values)


    def render_expand_all(self, values, context):
        """Output html of the component.
        """
        template = """
<th class="bx--table-expand {class}" data-event="expandAll" {props}>
  <button class="bx--table-expand__button">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--table-expand__svg" width="16" height="16" viewBox="0 0 16 16"
        aria-hidden="true">
      <path d="M11 8L6 13 5.3 12.3 9.6 8 5.3 3.7 6 3z"></path>
    </svg>
  </button>
</th>
"""
        return self.format(template, values)


    def render_row(self, values, context):
        """Output html of the component.
        """
        template = '<th scope="row" class="{class}" {props}>{child}</th>'
        return self.format(template, values)


class Td(Node):
    """Table row column.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    MODES = ('default', 'menu', 'menu_visible')
    "Available variants."
    SLOTS = ('secondary',)
    "Named children."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_menu'] = _("Open menu")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<td class="{class}" {props}>
  {child}
  {slot_secondary}
</td>
"""
        return self.format(template, values, context)


    def render_menu(self, values, context):
        """Output html of the component.
        """
        template = """
<td class="bx--table-column-menu {class}" {props}>
  <div data-overflow-menu role="menu" tabindex="0" aria-label="{label}{label_suffix}"
      class="bx--overflow-menu" title="{txt_menu}">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 32 32" aria-hidden="true">
      <circle cx="16" cy="8" r="2"></circle>
      <circle cx="16" cy="16" r="2"></circle>
      <circle cx="16" cy="24" r="2"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
      {child}
    </ul>
  </div>
</td>
"""
        return self.format(template, values)


    def render_menu_visible(self, values, context):
        """Output html of the component.
        """
        template = """
<td class="bx--table-column-menu {class}" {props}>
  <div data-overflow-menu role="menu" tabindex="0"
      aria-label="{label}{label_suffix}" class="bx--overflow-menu" title="{txt_menu}">
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        fill="currentColor" xmlns="http://www.w3.org/2000/svg"
        class="bx--overflow-menu__icon" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <circle cx="8" cy="3" r="1"></circle>
      <circle cx="8" cy="8" r="1"></circle>
      <circle cx="8" cy="13" r="1"></circle>
    </svg>
    <ul class="bx--overflow-menu-options bx--overflow-menu--flip">
      {child}
    </ul>
  </div>
</td>
"""
        return self.format(template, values)


    def render_slot_secondary(self, values, context):
        """Render html of the slot.
        """
        template = """
<div class="bx--data-table--cell-secondary-text {class}" {props}>
  {child}
</div>
"""
        return self.format(template, values)


class TdCheckBox(FormNode):
    """Table row checkbox.
    """
    NODE_PROPS = ('value',)
    "Extended Template Tag arguments."
    REQUIRED_PROPS = ('value',)
    "Will raise Exception if not set."

    value = None

    def default_id(self):
        """Get Django form field html id.
        """
        return '%s-%s' % (self.bound_field.id_for_label, uuid4().hex)


    def label(self):
        """Get Django form field label.
        """
        for _, val, txt in self.choices():
            if val == self.value:
                return txt
        return ''


    def before_prepare(self, values, context):
        """Initialize the values meant for rendering templates.
        """
        self.value = self.eval(self.kwargs['value'], context)
        super().before_prepare(values, context)


    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['value'] = self.value
        values['name'] = self.bound_field.name

        if self.bound_value and self.value in self.bound_value:
            values['props'].append(('checked', True))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<td class="bx--table-column-checkbox">
  <input name="{name}" value="{value}" type="checkbox" id="{id}"
      class="bx--checkbox {class}" data-event="select" {props}>
  <label for="{id}" class="bx--checkbox-label" aria-label="{label}{label_suffix}"></label>
</td>
"""
        return self.format(template, values)


class TableToolbarSearch(Node):
    """Table toolbar search filter.
    """
    NODE_PROPS = ('id', 'expandable', 'small')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('wrapper', 'magnifier')
    "Prepare xxx_class and xxx_props values."

    CATCH_PROPS = ('search_props',)

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_search'] = _("Search")
        values['txt_clear'] = _("Clear search input")
        if not values['label']:
            values['label'] = values['txt_search']

        if self.eval(self.kwargs.get('expandable'), context):
            values['wrapper_class'].append(
                    'bx--toolbar-search-container-expandable')
            values['magnifier_props'].append(('tabindex', '0'))
        else:
            values['wrapper_class'].append(
                    'bx--toolbar-search-container-persistent')

        if self.eval(self.kwargs.get('small'), context):
            values['class'].append('bx--search--sm')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div class="{wrapper_class}" {wrapper_props}>
  <div data-search class="bx--search {class}" role="search" {props}>
    <div class="bx--search-magnifier {magnifier_class}" {magnifier_props}>
      {tmpl_magnifier_icon}
    </div>
    <label id="label-{id}" class="bx--label" for="{id}">
      {label}{label_suffix}
    </label>
    <input class="bx--search-input" type="text" id="{id}" role="search"
        placeholder="{txt_search}" aria-labelledby="label-{id}">
    <button class="bx--search-close bx--search-close--hidden"
        title="{txt_clear}" aria-label="{txt_clear}">
      <svg focusable="false" preserveAspectRatio="xMidYMid meet"
          xmlns="http://www.w3.org/2000/svg" fill="currentColor"
          width="16" height="16" viewBox="0 0 32 32" aria-hidden="true">
        <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
      </svg>
    </button>
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_magnifier_icon(self, values, context):
        """Dynamically render a part of the component's template.
        """
        return """
<svg focusable="false" preserveAspectRatio="xMidYMid meet"
    xmlns="http://www.w3.org/2000/svg" fill="currentColor"
    class="bx--toolbar-action__icon" width="16" height="16" viewBox="0 0 16 16"
    aria-hidden="true">
  <path d="M15,14.3L10.7,10c1.9-2.3,1.6-5.8-0.7-7.7S4.2,0.7,2.3,3S0.7,8.8,3,10.7c2,1.7,5,1.7,7,0l4.3,4.3L15,14.3z M2,6.5	C2,4,4,2,6.5,2S11,4,11,6.5S9,11,6.5,11S2,9,2,6.5z"></path>
</svg>
"""


class TableToolbarOverflowButton(Node):
    """Table toolbar action button.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('active',)
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('list',)
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('active'), context):
            values['props'].append(('data-floating-menu-primary-focus', True))

        if not context.get('compact'):
            values['list_class'].append('bx--overflow-menu--data-table')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--overflow-menu-options__option {list_class}"
    role="presentation" {list_props}>
  <button class="bx--overflow-menu-options__btn {class}" role="menuitem"
      {props}>
    <div class="bx--overflow-menu-options__option-content">
      {child}
    </div>
  </button>
</li>
"""
        return self.format(template, values)


class TdOverflowButton(Node):
    """Table row action button.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('icon',)
    "Named children."
    NODE_PROPS = ('icon_size',)
    "Extended Template Tag arguments."

    def render_default(self, values, context):
        """Output html of the component.
        """
        values['cleaned_child'] = clean_attr_value(values['child'])

        template = """
<li class="bx--overflow-menu-options__option bx--table-row--menu-option">
  <{astag} class="bx--overflow-menu-options__btn {class}"
      title="{cleaned_child}" {props}>
    <div class="bx--overflow-menu-options__option-content">
      {slot_icon}
      {child}
    </div>
  </{astag}>
</li>
"""
        return self.format(template, values, context)


    def render_slot_icon(self, values, context):
        """Render html of the slot.
        """
        size = self.eval(self.kwargs.get('icon_size', 16), context)
        return modify_svg(values['child'], {
            'focusable': 'false',
            'preserveAspectRatio': 'xMidYMid meet',
            'fill': 'currentColor',
            'style': {
                'width': '%spx' % size,
                'height': '%spx' % size,
            },
            'aria-hidden': 'true',
            'class': values['class'],
        })


components = {
    'Table': DataTable,
    'Th': Th,
    'Td': Td,
    'TdCheck': TdCheckBox,
    'TableOvButton': TableToolbarOverflowButton,
    'TdOvButton': TdOverflowButton,
    'TbSearch': TableToolbarSearch,
    'TrExpandable': TrExpandable,
}
