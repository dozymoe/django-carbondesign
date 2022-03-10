Getting Started
===============

Introduction
------------

Provides `Carbon Design System`_ as Django_ template tags.

This project only offers the HTML markups as described in
`Carbon Design System Native`_, but it can be extended easily with your own
components.

Some components work with forms and require that you pass the form fields to the
template tags as its first argument.

There is the concept of slots, where you can fill in different parts of the
components.

The arguments you set for the template tags will be added to the html element's
attributes.


Installation
------------

.. code-block:: sh

    pip install django-carbondesign


Configuration
-------------

Add :code:`carbondesign` to your :code:`INSTALLED_APPS` setting.

Set the following in settings.py:

.. code-block:: python

    SVG_DIRS = []

`Carbon Design System`_ makes heavy use of svg html elements, you have to tell
the project where to find those svg files, and use them in the templates like
this:

.. code-block:: jinja

    {% load carbondesign %}

    {% Button %}
      {% Slot 'icon' %}
        {% svg 'fa/solid/sign-in-alt.svg' %}
      {% endSlot %}
    {% endButton %}

Usage
-----

The project provides template tags that you can use in Django templates.

There is :code:`{% carbondesign_assets %}` that you can use in html head to
include built-in carbon design assets (css/js) in your templates.

There is :code:`{% svg %}` that you can use to embed svg files.

And template tags that represents `Carbon Design System`_'s components.

How to use them in your templates is simple:

.. code-block:: jinja

    {% load i18n carbondesign %}
    <html>
      <head>
        {% carbondesign_assets %}
      </head>
      <body>
        {% url 'home' as url %}
        {% UiShell label=request.site.name href=url %}
          {% Slot 'navigation' %}
            {% UiNavSection %}
              {% if user.is_authenticated %}
                {% url 'account_logout' as url %}
                {% UiNavItem href=url %}
                  {% Slot 'icon' %}
                    {% svg 'fa/solid/sign-out-alt.svg' %}
                  {% endSlot %}
                  {% trans "Sign Out" %}
                {% endUiNavItem %}
              {% else %}
                {% url 'account_login' as url %}
                {% UiNavItem href=url %}
                  {% Slot 'icon' %}
                    {% svg 'fa/solid/sign-in-alt.svg' %}
                  {% endSlot %}
                  {% trans "Sign In" %}
                {% endUiNavItem %}
              {% endif %}
            {% endUiNavSection %}
          {% endSlot %}
        {% endUiShell %}

        {% for msg in messages %}
          {% Notification mode='toast' variant=msg.level %}
            {% NotificationSubtitle %}
              {{msg.message}}
            {% endNotificationSubtitle %}
          {% endNotification %}
        {% endfor %}

        <main>
          <form action="" method="post">
            {% csrf_token %}

            <div class="form-group">
              {% TextInput form.address %}
            </div>

            {% Button type="submit" %}
              {% trans "Search" %}
            {% endButton %}
          </form>
        </main>
      </body>
    </html>

In the above code, argument :code:`type="submit"` that you set for the Button
component will create html attribute type for the button element.


Advanced Usage
--------------

How to extends this project with your own components.

Checkout the tags_ and templatetags_ directories.

Write your own components in your module's :code:`tags` directory, following the
examples in this project`s tags_.

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


.. _Django: https://docs.djangoproject.com/
.. _Carbon Design System: https://www.carbondesignsystem.com/
.. _Carbon Design System Native: https://the-carbon-components.netlify.app/
.. _tags: https://github.com/dozymoe/django-carbondesign/tree/main/carbondesign/tags/
.. _templatetags: https://github.com/dozymoe/django-carbondesign/tree/main/carbondesign/templatetags/
