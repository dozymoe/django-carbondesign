from .template_base import TemplateBase


class IgnoreMissing(dict):
    def __missing__(self, key):
        return '{' + key + '}'


class TemplateString(TemplateBase):

    empty = ''

    def render_template(self, template, variables, helpers=None,
            subtemplates=None):

        # Format twice for subtemplates.
        return template.format_map(IgnoreMissing(**subtemplates))\
                .format(**variables)


    def get(self, template_name):
        return ''


    def get_raw(self, template_name):
        return ''


    def create_template(self, text):
        return text
