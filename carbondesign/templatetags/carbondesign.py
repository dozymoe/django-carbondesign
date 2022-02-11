import logging
#-
from django import template
#-
from ..tags import base, button, checkbox, data_table, grid, text_area
from ..tags import text_input, ui_shell

_logger = logging.getLogger(__name__)
register = template.Library()


MATERIAL_TAGS = {
    **base.components,
    **button.components,
    **checkbox.components,
    **data_table.components,
    **grid.components,
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


_parser = TagParser(MATERIAL_TAGS)
for name in MATERIAL_TAGS:
    register.tag(name, _parser)
