from django.conf import settings
from django.utils.module_loading import import_string
#
from ..template_handlebars import TemplateHandlebars


_tpl_mgr = None


def get_template_manager():
    global _tpl_mgr # pylint:disable=global-statement
    if not _tpl_mgr:
        classname = getattr(settings, 'CARBONDESIGN_TEMPLATE_MANAGER', None)
        if classname:
            _tpl_mgr = import_string(classname)()
        else:
            _tpl_mgr = TemplateHandlebars()

    return _tpl_mgr
