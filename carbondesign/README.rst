django-carbondesign
===================

Implements Carbon Design System as Django templatetags.

Documentations:

- https://dozymoe.github.io/django-carbondesign
- https://www.carbondesignsystem.com/components/overview/


Quick Start
-----------

1. Add :code:`carbondesign` to your :code:`INSTALLED_APPS` setting.

2. Load template tag like this :code:`{% load carbondesign %}`.

3. Add built-in assets (js/css) :code:`{% carbondesign_assets %}`.

4. Use the components :code:`{% Pagination pager=page_obj %}`.
