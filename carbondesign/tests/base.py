# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from datetime import datetime
import re
#-
from django.core.paginator import Paginator
from django.template import Context, Template
#-
from .forms import DummyForm

DATETIME_PATTERN = '%Y-%m-%d %H:%M:%S'


def strip_space(value):
    value = re.sub(r'\s+"', '"', value)
    value = re.sub(r'[\n\s]+>', '>', value)
    return re.sub(r'\n\s*\n', r'\n', value)


def compare_template(template, expected):
    form = DummyForm(initial={
            'text': "a text",
            'choice': "val1",
            'started_at': datetime.strptime('2022-02-03 01:02:03',
                DATETIME_PATTERN),
            'stopped_at': datetime.strptime('2022-10-04 11:30:40',
                DATETIME_PATTERN),
            'image': 'path/image.jpeg',
            'number': 24})

    pager = Paginator(range(100), 10)
    context = Context({
            'form': form,
            'page': pager.page(3),
            'page_first': pager.page(1),
            'page_last': pager.page(10)})

    return (
        strip_space(expected),
        strip_space(Template(template).render(context)),
    )
