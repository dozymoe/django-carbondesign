# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django.test import SimpleTestCase
#-
from .base import compare_template

class FileTest(SimpleTestCase):
    maxDiff = None

    def test_rendered(self):
        template = """
{% load carbondesign %}
{% File form.image %}
"""
        expected = """
<div class="bx--form-item">
  <strong class="bx--file--label">
    Image
  </strong>
  <div class="bx--file" data-file>
    <label for="id_image" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        Drag and drop files here or upload
        <input type="file" name="image" accept="image/*" class="bx--file-input" data-file-uploader="" data-target="#container-id_image" id="id_image">
      </div>
    </label>
    <div data-file-container id="container-id_image" class="bx--file-container">
      <div class="bx--file__selected-file">
        <p class="bx--file-filename">path/image.jpeg</p>
        <span data-for="prepopulated-file-uploader"
            class="bx--file__state-container">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              class="bx--file-complete" width="16" height="16"
              viewBox="0 0 16 16" aria-hidden="true">
            <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
            <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
          </svg>
        </span>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
