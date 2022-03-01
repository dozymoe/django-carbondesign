import logging
import os
import re
#-
from django import template
from django.conf import settings
from django.utils.safestring import mark_safe
#-
from ..tags import base, button, checkbox, data_table, date_picker, grid, modal
from ..tags import text_area, text_input, ui_shell

_logger = logging.getLogger(__name__)
register = template.Library()


MATERIAL_TAGS = {
    **base.components,
    **button.components,
    **checkbox.components,
    **data_table.components,
    **date_picker.components,
    **grid.components,
    **modal.components,
    **text_area.components,
    **text_input.components,
    **ui_shell.components,
}


class TagParser:

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
                val = template.Variable(val)

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


_parser = TagParser(MATERIAL_TAGS)
for name in MATERIAL_TAGS:
    register.tag(name, _parser)
