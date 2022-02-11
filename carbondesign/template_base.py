from functools import lru_cache
#-
from django.conf import settings
from django.template import engines
from django.template.exceptions import TemplateDoesNotExist


@lru_cache(maxsize=getattr(settings, 'CARBONDESIGN_CACHE_SIZE', 256))
def get_template_content(template_name, using=None):
    """Simplified django.template.loader.get_template
    """
    errors = []
    engine_list = engines.all() if using is None else [engines[using]]
    for tplengine in engine_list:
        for tplloader in tplengine.engine.template_loaders:
            try:
                for origin in tplloader.get_template_sources(template_name):
                    try:
                        contents = tplloader.get_contents(origin)
                    except TemplateDoesNotExist:
                        continue
                    else:
                        return str(contents)
            except TemplateDoesNotExist as e:
                errors.append(e)

    raise TemplateDoesNotExist(template_name, chain=errors)


class TemplateBase:

    def render(self, template_name, variables, helpers=None,
            subtemplates=None):

        template = self.get(template_name)
        return self.render_template(template, variables, helpers, subtemplates)


    def render_template(self, template, variables, helpers=None,
            subtemplates=None):
        raise NotImplementedError()


    def get(self, template_name):
        raise NotImplementedError()


    def get_raw(self, template_name):
        raise NotImplementedError()


    def create_template(self, text):
        raise NotImplementedError()
