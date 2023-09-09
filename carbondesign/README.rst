django-carbondesign
===================

The development of this module has been halted per 20 May 2023 because Carbon
Design System from IBM no longer support vanilla js. Previously I developed
similar module using Material Design System from Google. The reason I moved from
Material Design was because the documentation doesn't match their releases, I
found better documentation support in Carbon Design. The documentation was meant
for the users of the library.

For the next iteration I will be using Engie's Fluid Design System, the
python module will be named django-fluid-design and can be found here
https://github.com/dozymoe/django-fluid-design

Hopefully it will last longer.


Summary
-------

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
