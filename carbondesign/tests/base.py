# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
import re
#-
from django.template import Context, Template

def strip_space(value):
    return re.sub(r'\n\s*\n', r'\n', value)


def compare_template(template, expected, context):
    return (
        strip_space(Template(template).render(Context(context))),
        strip_space(expected),
    )
