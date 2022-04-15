"""Template tags provided by carbondesign module.

Provides built-in Carbon Design components template tags,
svg for loading svg file,
carbondesign_assets for loading css/js files.
"""
import logging
import os
import re
#-
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
#-
from ..tags import accordion, base, breadcrumb, button, checkbox, code_snippet
from ..tags import combo_box, content_switcher, copy_button, data_table
from ..tags import date_picker, file_uploader, grid, inline_loading
from ..tags import link, list_, loading, modal, multi_select
from ..tags import notification, number_input, overflow_menu, pagination
from ..tags import pagination_nav, progress_indicator, radio_button, search
from ..tags import select, slider, structured_list, tabs, tag, text_area
from ..tags import text_input, tile, time_picker, toggle, toolbar, tooltip
from ..tags import ui_shell, ui_shell_switcher

_logger = logging.getLogger(__name__)
register = template.Library()

MATERIAL_TAGS = {
    **accordion.components,
    **base.components,
    **breadcrumb.components,
    **button.components,
    **checkbox.components,
    **code_snippet.components,
    **combo_box.components,
    **content_switcher.components,
    **copy_button.components,
    **data_table.components,
    **date_picker.components,
    **file_uploader.components,
    **grid.components,
    **inline_loading.components,
    **link.components,
    **list_.components,
    **loading.components,
    **modal.components,
    **multi_select.components,
    **notification.components,
    **number_input.components,
    **overflow_menu.components,
    **pagination.components,
    **pagination_nav.components,
    **progress_indicator.components,
    **radio_button.components,
    **search.components,
    **select.components,
    **slider.components,
    **structured_list.components,
    **tabs.components,
    **tag.components,
    **text_area.components,
    **text_input.components,
    **tile.components,
    **time_picker.components,
    **toggle.components,
    **toolbar.components,
    **tooltip.components,
    **ui_shell.components,
    **ui_shell_switcher.components,
}


class TagParser:
    """Parse arguments of Django template tags.
    """
    def __init__(self, tags):
        self.tags = tags

    def __call__(self, parser, token):
        params = token.split_contents()
        tagname = params.pop(0)

        args = []
        kwargs = {}
        for param in params:
            if '=' in param:
                key, val = param.split('=', 1)
            else:
                key, val = (None, param)

            if val[0] in ('"', "'"):
                val = val.strip('"\'')
            else:
                val = base.VariableInVariable(val, parser)

            if key:
                kwargs[key] = val
            else:
                args.append(val)

        cls = self.tags[tagname]

        if getattr(cls, 'WANT_CHILDREN', False):
            nodelist = parser.parse(('end' + tagname,))
            parser.delete_first_token()
            args.insert(0, nodelist)

        return cls(*args, **kwargs)


@register.simple_tag
def svg(path):
    """This template tag will load svg files located in settings.SVG_DIRS.
    """
    # Security test.
    if not path or not re.match(r'^\w.*\.svg$', path):
        return ''
    for dirname in settings.SVG_DIRS:
        if not os.path.exists(dirname/path):
            continue
        return mark_safe(open(dirname/path, 'r', encoding='utf-8').read())
    return ''


@register.simple_tag
def carbondesign_assets():
    """This template tag will inject native carbondesign css/js files.

    Don't forget to run collectstatic!
    """
    if settings.DEBUG:
        suffix = ''
    else:
        suffix = '.min'
    tmpl = """
<link rel="stylesheet" type="text/css" href="{baseurl}carbondesign/carbon-components{suffix}.css">
<script src="{baseurl}carbondesign/carbon-components{suffix}.js"></script>
""" # pylint:disable=line-too-long
    return mark_safe(tmpl.format(baseurl=settings.STATIC_URL, suffix=suffix))


_parser = TagParser(MATERIAL_TAGS)
for name in MATERIAL_TAGS:
    register.tag(name, _parser)
