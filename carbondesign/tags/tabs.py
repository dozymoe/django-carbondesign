"""
Tabs
====

See: https://www.carbondesignsystem.com/components/tabs/usage/

Use tabs to allow users to navigate easily between views within the same
context.

Overview
--------

Tabs are used to quickly navigate between views within the same context.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class Tabs(Node):
    """Tabs component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    SLOTS = ('header',)
    "Named children."
    NODE_PROPS = ('container',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if self.eval(self.kwargs.get('container'), context):
            values['class'].append('bx--tabs--container')


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-tabs class="bx--tabs {class}" {props}>
  <div class="bx--tabs-trigger" tabindex="0">
    <a href="javascript:void(0)" class="bx--tabs-trigger-text" tabindex="-1"></a>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor" width="16"
        height="16" viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8 11L3 6 3.7 5.3 8 9.6 12.3 5.3 13 6z"></path>
    </svg>
  </div>
  <ul class="bx--tabs__nav bx--tabs__nav--hidden" role="tablist">
    {slot_header}
  </ul>
</div>
<div class="bx--tab-content">
  {child}
</div>
"""
        return self.format(template, values, context)


class TabItem(Node):
    """Tabs item component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('active', 'target', 'disabled')
    "Extended Template Tag arguments."
    CLASS_AND_PROPS = ('tab',)
    "Prepare xxx_class and xxx_props values."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        active = self.eval(self.kwargs.get('active'), context)
        if active:
            values['tab_class'].append('bx--tabs__nav-item--selected')
            values['tab_props'].append(('aria-selected', 'true'))

        target = self.eval(self.kwargs.get('target'), context)
        values['target'] = target or ''
        if target:
            values['props'].append(('id', f'tab-link-{target}'))

        if self.eval(self.kwargs.get('disabled'), context):
            values['tab_class'].append('bx--tabs__nav-item--disabled')
            values['tab_props'].append(('aria-disabled', 'true'))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<li class="bx--tabs__nav-item {tab_class}" data-target="#{target}"
    role="tab" {tab_props}>
  <a tabindex="0" class="bx--tabs__nav-link {class}" href="javascript:void(0)"
      role="tab" aria-controls="{target}" {props}>
    {child}
  </a>
</li>
"""
        return self.format(template, values)


class TabContent(Node):
    """Tabs content component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('id', 'active', 'target')
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        active = self.eval(self.kwargs.get('active'), context)
        if active:
            values['props'].append(('aria-hidden', 'false'))
        else:
            values['props'].append(('aria-hidden', 'true'))
            values['props'].append(('hidden', True))

        values['target'] = self.eval(self.kwargs.get('target'), context)


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div id="{id}" role="tabpanel" aria-labelledby="tab-link-{id}" {props}>
  <div>{child}</div>
</div>
"""
        return self.format(template, values)


components = {
    'Tabs': Tabs,
    'TabItem': TabItem,
    'TabContent': TabContent,
}
