# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from datetime import datetime
from io import BytesIO
import re
#-
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import Paginator
from django.template import Context, Template
from PIL import Image
#-
from .forms import DummyForm

DATETIME_PATTERN = '%Y-%m-%d %H:%M:%S'


def strip_space(value):
    value = re.sub(r'\s+"', '"', value)
    value = re.sub(r'[\n\s]+>', '>', value)
    #value = re.sub(r'>\s+', '>', value)
    #value = re.sub(r'\n\s+', '\n', value)
    return re.sub(r'\n\s*\n', '\n', value)


def compare_template(template, expected, context=None):
    if context is None:
        im_io = BytesIO()
        im = Image.new(mode='RGB', size=(200, 200))
        im.save(im_io, 'PNG')
        im_size = im_io.tell()
        im_io.seek(0)

        files = {
            'image': InMemoryUploadedFile(im_io, None,
                'path/image.png', 'image/png', im_size, None),
            'image_multi': InMemoryUploadedFile(im_io, None,
                'Lorem ipsum dolor sit amet consectetur adipisicing elit. '
                'Libero vero sapiente illum reprehenderit molestiae '
                'perferendis voluptatem temporibus laudantium ducimus magni '
                'voluptatum veniam, odit nesciunt corporis numquam maxime '
                'sunt excepturi sint!.png',
                'image/png', im_size, None),
            'image_invalid': InMemoryUploadedFile(im_io, None,
                'color', 'image/png', im_size, None),
        }
        form = DummyForm(data={
                'text': "a text",
                'choice': "val1",
                'started_at': datetime.strptime('2022-02-03 01:02:03',
                    DATETIME_PATTERN),
                'started_at_missing': '',
                'stopped_at': datetime.strptime('2022-10-04 11:30:40',
                    DATETIME_PATTERN),
                'stopped_at_missing': '',
                'number': 24},
                files=files)

        pager = Paginator(range(100), 10)
        context = Context({
                'form': form,
                'page': pager.page(3),
                'page_first': pager.page(1),
                'page_last': pager.page(10)})
    else:
        context = Context(context)

    return (
        strip_space(expected),
        strip_space(Template(template).render(context)),
    )
