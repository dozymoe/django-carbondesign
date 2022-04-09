Advanced Usage
==============

How To Create Your Own Components
---------------------------------

Checkout the tags_ and templatetags_ directories.

Write your own components in your module's :code:`tags` directory, following
the examples there.

Create a file in your module's :code:`templatetags` directory, for example
**website_carbondesign.py**.

Example code:

.. code-block:: python

    from django import template
    from carbondesign.templatetags.carbondesign import TagParser
    #-
    from ..tags import mycomponent

    register = template.Library()

    CARBON_TAGS = {
        **mycomponent.components,
    }

    _parser = TagParser(CARBON_TAGS)
    for name in CARBON_TAGS:
        register.tag(name, _parser)


.. _tags: https://github.com/dozymoe/django-carbondesign/tree/main/carbondesign/tags/
.. _templatetags: https://github.com/dozymoe/django-carbondesign/tree/main/carbondesign/templatetags/
