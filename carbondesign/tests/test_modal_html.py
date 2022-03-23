# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,too-many-lines
from django.test import SimpleTestCase
#-
from .base import compare_template

class ModalHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_danger(self):
        template = """
{% load carbondesign %}
{% ModalTrigger variant="danger" target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" variant="danger" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button variant="danger" type="button" label="Danger" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--danger" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal bx--modal--danger" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content">
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--danger" type="button" data-modal-primary-focus="" aria-label="Danger">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_input(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" has_form=True %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  {% TextInput form.text_empty label="Text Input label" placeholder="Optional placeholder text" data-modal-primary-focus="" %}

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content bx--modal-content--with-form" >
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text_empty" class="bx--label">
  Text Input label
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text_empty" placeholder="Optional placeholder text" data-modal-primary-focus="" class="bx--text-input" id="id_text_empty">
  </div>
</div>
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_lg(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="lg" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--lg">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button" data-modal-primary-focus="">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nofooter_lg(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="lg" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--lg">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal" data-modal-primary-focus="">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content">
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nofooter_sm(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="sm" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--sm">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal" data-modal-primary-focus="">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nofooter_xs(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="xs" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--xs">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal" data-modal-primary-focus="">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_nofooter(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal" data-modal-primary-focus="">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_scrolling(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" can_scroll=True %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <h3>Lorem ipsum</h3>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal " role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" tabindex="0">
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <h3>Lorem ipsum</h3>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button" data-modal-primary-focus="">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_sm(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="sm" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--sm">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button" data-modal-primary-focus="">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_titleonly_nofooter_sm(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="sm" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}
    Passive modal title as the message. Should be direct and 3 lines or less.
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--sm">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
    Passive modal title as the message. Should be direct and 3 lines or less.
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal" data-modal-primary-focus="">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content">
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_titleonly_nofooter_xs(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="xs" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}
    Passive modal title as the message. Should be direct and 3 lines or less.
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--xs">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
    Passive modal title as the message. Should be direct and 3 lines or less.
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal" data-modal-primary-focus="">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_titleonly_sm(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="sm" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}
    Passive modal title as the message. Should be direct and 3 lines or less.
  {% endSlot %}

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--sm">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
    Passive modal title as the message. Should be direct and 3 lines or less.
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button" data-modal-primary-focus="">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_titleonly_xs(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="xs" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}
    Passive modal title as the message. Should be direct and 3 lines or less.
  {% endSlot %}

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--xs">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
    Passive modal title as the message. Should be direct and 3 lines or less.
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button" data-modal-primary-focus="">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_xs(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" size="xs" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container bx--modal-container--xs">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button" data-modal-primary-focus="">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_default(self):
        template = """
{% load carbondesign %}
{% ModalTrigger target="uid" type="button" %}{% endModalTrigger %}
{% Modal id="uid" %}
  {% Slot 'label' %}Optional label{% endSlot %}
  {% Slot 'heading' %}Modal heading{% endSlot %}

  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

  {% Slot 'footer' %}
    {% Button variant="secondary" type="button" data-modal-close="" %}
      Secondary button
    {% endButton %}
    {% Button type="button" data-modal-primary-focus="" %}
      Primary button
    {% endButton %}
  {% endSlot %}
{% endModal %}
"""
        expected = """
<button class="bx--btn bx--btn--primary" type="button" data-modal-target="#uid">
  Show modal
</button>
<div data-modal id="uid" class="bx--modal" role="dialog"
    aria-modal="true" tabindex="-1" aria-labelledby="label-uid" aria-describedby="heading-uid">
  <div class="bx--modal-container">
    <div class="bx--modal-header">
<p class="bx--modal-header__label bx--type-delta" id="label-uid">
  Optional label
</p>
<p class="bx--modal-header__heading bx--type-beta" id="heading-uid">
  Modal heading
</p>
      <button class="bx--modal-close" type="button" data-modal-close
          aria-label="close modal">
        <svg focusable="false" preserveAspectRatio="xMidYMid meet"
            xmlns="http://www.w3.org/2000/svg" fill="currentColor"
            class="bx--modal-close__icon" width="16" height="16"
            viewBox="0 0 32 32" aria-hidden="true">
          <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
        </svg>
      </button>
    </div>

    <div class="bx--modal-content" >
  <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean id
      accumsan augue. Phasellus consequat augue vitae tellus tincidunt posuere.
      Curabitur justo urna, consectetur vel elit iaculis, ultrices condimentum
      risus. Nulla facilisi.
      Etiam venenatis molestie tellus. Quisque consectetur non risus eu rutrum.</p>

    </div>
    <div class="bx--modal-content--overflow-indicator"></div>

    <div class="bx--modal-footer">
<button class="bx--btn bx--btn--secondary" type="button" data-modal-close="">
      Secondary button
</button>
<button class="bx--btn bx--btn--primary" type="button" data-modal-primary-focus="">
      Primary button
</button>
  </div>
  </div>
  <span tabindex="0"></span>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
