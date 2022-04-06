# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class TextInputTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% TextInput form.text %}
"""
        expected = """
<div class="bx--form-item bx--text-input-wrapper">
<label for="id_text" class="bx--label">
  Text
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="text" name="text" value="a text" class="bx--text-input" required id="id_text">
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)


class PasswordInputTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% PasswordInput form.text %}
"""
        expected = """
<div data-text-input
    class="bx--form-item bx--text-input-wrapper bx--password-input-wrapper">
<label for="id_text" class="bx--label">
  Text
</label>
  <div class="bx--text-input__field-wrapper">
    <input type="password" name="text" class="bx--text-input bx--password-input" data-toggle-password-visibility="" required id="id_text">
<button type="button"
    class="bx--text-input--password__visibility__toggle bx--tooltip__trigger bx--tooltip--a11y bx--tooltip--bottom bx--tooltip--align-center">
  <span class="bx--assistive-text">Show password</span>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      hidden="true" class="bx--icon--visibility-off" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M2.6,11.3l0.7-0.7C2.6,9.8,1.9,9,1.5,8c1-2.5,3.8-4.5,6.5-4.5c0.7,0,1.4,0.1,2,0.4l0.8-0.8C9.9,2.7,9,2.5,8,2.5	C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3C1,9.3,1.7,10.4,2.6,11.3z"></path>
    <path d="M6 7.9c.1-1 .9-1.8 1.8-1.8l.9-.9C7.2 4.7 5.5 5.6 5.1 7.2 5 7.7 5 8.3 5.1 8.8L6 7.9zM15.5 7.8c-.6-1.5-1.6-2.8-2.9-3.7L15 1.7 14.3 1 1 14.3 1.7 15l2.6-2.6c1.1.7 2.4 1 3.7 1.1 3.3-.1 6.3-2.2 7.5-5.3C15.5 8.1 15.5 7.9 15.5 7.8zM10 8c0 1.1-.9 2-2 2-.3 0-.7-.1-1-.3L9.7 7C9.9 7.3 10 7.6 10 8zM8 12.5c-1 0-2.1-.3-3-.8l1.3-1.3c1.4.9 3.2.6 4.2-.8.7-1 .7-2.4 0-3.4l1.4-1.4c1.1.8 2 1.9 2.6 3.2C13.4 10.5 10.6 12.5 8 12.5z"></path>
  </svg>
  <svg focusable="false" preserveAspectRatio="xMidYMid meet"
      xmlns="http://www.w3.org/2000/svg" fill="currentColor"
      class="bx--icon--visibility-on" width="16" height="16"
      viewBox="0 0 16 16" aria-hidden="true">
    <path d="M15.5,7.8C14.3,4.7,11.3,2.6,8,2.5C4.7,2.6,1.7,4.7,0.5,7.8c0,0.1,0,0.2,0,0.3c1.2,3.1,4.1,5.2,7.5,5.3	c3.3-0.1,6.3-2.2,7.5-5.3C15.5,8.1,15.5,7.9,15.5,7.8z M8,12.5c-2.7,0-5.4-2-6.5-4.5c1-2.5,3.8-4.5,6.5-4.5s5.4,2,6.5,4.5	C13.4,10.5,10.6,12.5,8,12.5z"></path>
    <path d="M8,5C6.3,5,5,6.3,5,8s1.3,3,3,3s3-1.3,3-3S9.7,5,8,5z M8,10c-1.1,0-2-0.9-2-2s0.9-2,2-2s2,0.9,2,2S9.1,10,8,10z"></path>
  </svg>
</button>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
