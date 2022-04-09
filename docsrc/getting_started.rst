Getting Started
===============

Introduction
------------

Provides `Carbon Design System`_ as Django_ template tags.

This module only offers the HTML markups as described in
`Carbon Design System Native`_, while the `Carbon Design System`_ itself offers
React, Angular (Community), Vue (Community) and Web Components (Community).

There are two main selling points, the slots concept and Django_ forms support.

With slots you can create complex templates, and support for Django_ forms
means creating custom admin pages is a lot easier.

You can write: :code:`{% PasswordInput form.password %}` and you are done.


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
the module where to find those svg files, and use them in the templates like
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

There are several notes:

* There is the concept of slots, where you can fill different parts of the
  components. You can see the example above, setting the icon for a button.

* Some of the components works with forms and require that you pass the form
  field to the template tags as its first argument. This is the first example
  with **form.password**.

* Some of the arguments you set for the template tag may be rendered as html
  attributes, example below.

These are the Django_ template tags:

* :code:`{% carbondesign_assets %}` that you can use in html head to include
  built-in carbon design assets (css/js).

* :code:`{% svg %}` that you can use to embed svg files.

* all the components.

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
        {% endUiShell %}
      </body>
    </html>

In the above code, argument :code:`type="submit"` that you set for the Button
component will add html attribute :code:`type`.


.. _Django: https://docs.djangoproject.com/
.. _Carbon Design System: https://www.carbondesignsystem.com/
.. _Carbon Design System Native: https://the-carbon-components.netlify.app/
