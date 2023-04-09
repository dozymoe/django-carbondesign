# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

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
<p id="hint-id_image" class="bx--label-description">
  Only .jpg and .png files. 500kb max file size.
</p>
  <div class="bx--file" data-file>
    <label for="id_image" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        Drag and drop files here or upload
        <input type="file" name="image" accept="image/*" class="bx--file-input" aria-controls="hint-id_image" aria-describedby="hint-id_image" data-file-uploader="" data-target="#container-id_image" required id="id_image">
      </div>
    </label>
    <div data-file-container id="container-id_image" class="bx--file-container">
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
