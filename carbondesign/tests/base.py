# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from datetime import datetime
import re
#-
from django.template import Context, Template
#-
from .forms import DummyForm

DATETIME_PATTERN = '%Y-%m-%d %H:%M:%S'


def strip_space(value):
    value = re.sub(r'\s+"', '"', value)
    value = re.sub(r'[\n\s]+>', '>', value)
    return re.sub(r'\n\s*\n', r'\n', value)


def compare_template(template, expected):
    form = DummyForm(data={
            'text': "a text",
            'choice': "val1",
            'started_at': datetime.strptime('2022-02-03 01:02:03',
                DATETIME_PATTERN),
            'stopped_at': datetime.strptime('2022-10-04 11:30:40',
                DATETIME_PATTERN)})

    context = Context({
            'form': form})

    return (
        strip_space(expected),
        strip_space(Template(template).render(context)),
    )
