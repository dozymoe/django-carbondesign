"""
Content Switcher
================

See: https://www.carbondesignsystem.com/components/content-switcher/usage/

Content switchers allow users to toggle between two or more content sections
within the same space on screen.

Overview
--------

Content switchers allow users to toggle between alternate views of similar or
related content. Only one content section is shown at a time.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from .base import Node

class ContentSwitcher(Node):
    """Content Switcher component.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        if values['label']:
            values['props'].append(('aria-label',
                    values['label'] + values['label_suffix']))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-content-switcher class="bx--content-switcher {class}" role="tablist"
    {props}>
  {child}
</div>
        """
        return self.format(template, values)


class ContentSwitcherItem(Node):
    """Content Switcher item.
    """
    WANT_CHILDREN = True
    "Template Tag needs closing end tag."
    NODE_PROPS = ('target', 'active', 'disabled')
    "Extended Template Tag arguments."
    DEFAULT_TAG = 'button'
    "Rendered HTML tag."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['target'] = self.eval(self.kwargs['target'], context)

        if self.eval(self.kwargs.get('active'), context):
            values['class'].append('bx--content-switcher--selected')
            values['props'].append(('aria-selected', 'true'))

        if self.eval(self.kwargs.get('disabled'), context):
            values['props'].append(('disabled', True))


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<{astag} class="bx--content-switcher-btn {class}" data-target="{target}"
    role="tab" {props}>
  <span class="bx--content-switcher__label">{child}</span>
</{astag}>
"""
        return self.format(template, values)


components = {
    'ContentSwitcher': ContentSwitcher,
    'ContentSwitcherItem': ContentSwitcherItem,
}
