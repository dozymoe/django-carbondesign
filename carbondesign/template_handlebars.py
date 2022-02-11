from functools import lru_cache
from itertools import chain
import logging
#-
from django.conf import settings
from django.utils.decorators import method_decorator
from pybars import Compiler
#-
from .template_base import get_template_content, TemplateBase

_logger = logging.getLogger(__name__)


class TemplateHandlebars(TemplateBase):

    def __init__(self):
        self.compiler = Compiler()
        self.empty = self.compiler.compile('')

        self.helpers = {}
        for name, helper in getattr(settings, 'HANDLEBARS_HELPERS', {}).items():
            self.helpers[name] = helper


    def render_template(self, template, variables, helpers=None,
            subtemplates=None):

        if helpers:
            with_helpers = dict(chain(self.helpers.items(), helpers.items()))
        else:
            with_helpers = self.helpers
        return template(variables, helpers=with_helpers, partials=subtemplates)


    @method_decorator(lru_cache)
    def get(self, template_name):
        source = get_template_content('carbondesign/%s.hbs' % template_name)
        return self.compiler.compile(source)


    def get_raw(self, template_name):
        return get_template_content('carbondesign/%s.hbs' % template_name)


    @method_decorator(lru_cache)
    def create_template(self, text):
        return self.compiler.compile(text)
