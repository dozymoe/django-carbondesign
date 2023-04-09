"""Helper functions for working with datetime format strings

Django uses PHP format in templates and Python format everywhere else.
"""
from datetime import datetime
#-
from django.utils.formats import get_format
import pytz

SAMPLE_DATETIME = datetime(1979, 5, 23, 13, 59, 43, 123,
        pytz.timezone('Asia/Jakarta'))

# From Flatpickr (which is used by Carbon Design)
TOKEN_REGEX = {
    'D': "(\\w+)",
    'F': "(\\w+)",
    'G': "(\\d\\d|\\d)",
    'H': "(\\d\\d|\\d)",
    'J': "(\\d\\d|\\d)\\w+",
    # ToDo: K is ignored
    'M': "(\\w+)",
    'S': "(\\d\\d|\\d)",
    'U': "(.+)",
    'W': "(\\d\\d|\\d)",
    'Y': "(\\d\\d\\d\\d)",
    'Z': "(.+)",
    'd': "(\\d\\d|\\d)",
    'h': "(\\d\\d|\\d)",
    'i': "(\\d\\d|\\d)",
    'j': "(\\d\\d|\\d)",
    'l': "(\\w+)",
    'm': "(\\d\\d|\\d)",
    'n': "(\\d\\d|\\d)",
    's': "(\\d\\d|\\d)",
    'u': "(.+)",
    'w': "(\\d\\d|\\d)",
    'y': "(\\d\\d)",
}


def dateformat_to_pattern(value):
    """Calculate the value of HTML pattern attribute
    """
    return ''.join(TOKEN_REGEX.get(x, x) for x in value)


def dateformat_python_to_php(python_format_string):
    """Convert datetime format string from python to php

    Given a python datetime format string, attempts to convert it to the nearest
    PHP datetime format string possible. 

    See: https://djangosnippets.org/snippets/10563/
    """
    python2PHP = {
            "%a": "D", "%A": "l", "%b": "M", "%B": "F", "%c": "", "%d": "d",
            "%H": "H", "%I": "h", "%j": "z", "%m": "m", "%M": "i", "%p": "A",
            "%S": "s", "%U": "", "%w": "w", "%W": "W", "%x": "", "%X": "",
            "%y": "y", "%Y": "Y", "%Z": "e" }

    php_format_string = python_format_string
    for py, php in python2PHP.items():
        php_format_string = php_format_string.replace(py, php)

    return php_format_string


def get_field_dateformat(bound_field):
    """Calculate bound field date format

    ToDo: This is oversimplified, I think I missed some things.
    """
    field = bound_field.field
    widget = field.widget

    if getattr(widget, 'format', None):
        fmt = widget.format
    elif getattr(widget, 'format_key', None):
        fmt = get_format(widget.format_key)[0]
    elif getattr(field, 'input_formats', None):
        fmt = get_format(field.input_formats[0])[0]
    else:
        return None

    return dateformat_python_to_php(fmt)
