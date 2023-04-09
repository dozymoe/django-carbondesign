# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from .base import compare_template, SimpleTestCase

class FileHtmlTest(SimpleTestCase):
    maxDiff = None

    def test_default(self):
        template = """
{% load carbondesign %}
{% File form.image_empty label="Account photo" %}
"""
        expected = """
<div class="bx--form-item">
  <strong class="bx--file--label">
    Account photo
  </strong>
<p id="hint-id_image_empty" class="bx--label-description">
  Only .jpg and .png files. 500kb max file size.
</p>
  <div class="bx--file" data-file>
    <label for="id_image_empty" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        Drag and drop files here or upload
        <input type="file" name="image_empty" accept="image/*" class="bx--file-input" aria-controls="hint-id_image_empty" aria-describedby="hint-id_image_empty" data-file-uploader="" data-target="#container-id_image_empty" id="id_image_empty">
      </div>
    </label>
    <div data-file-container id="container-id_image_empty" class="bx--file-container">
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_state_success(self):
        template = """
{% load carbondesign %}
{% File form.image_multi label="Account photo" %}
"""
        expected = """
<div class="bx--form-item">
  <strong class="bx--file--label">
    Account photo
  </strong>
<p id="hint-id_image_multi" class="bx--label-description">
  Only .jpg and .png files. 500kb max file size.
</p>
  <div class="bx--file" data-file>
    <label for="id_image_multi" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        Drag and drop files here or upload
        <input type="file" name="image_multi" multiple accept="image/*" class="bx--file-input" aria-controls="hint-id_image_multi" aria-describedby="hint-id_image_multi" data-file-uploader="" data-target="#container-id_image_multi" required id="id_image_multi">
      </div>
    </label>
    <div data-file-container id="container-id_image_multi" class="bx--file-container">
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_state_invalid(self):
        template = """
{% load carbondesign %}
{% File form.image_invalid label="Account photo" %}
"""
        expected = """
<div class="bx--form-item">
  <strong class="bx--file--label">
    Account photo
  </strong>
<p id="hint-id_image_invalid" class="bx--label-description">
  Only .jpg and .png files. 500kb max file size.
</p>
  <div class="bx--file" data-file>
    <label for="id_image_invalid" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        Drag and drop files here or upload
        <input type="file" name="image_invalid" accept="image/*" class="bx--file-input" aria-controls="hint-id_image_invalid" aria-describedby="hint-id_image_invalid" data-file-uploader="" data-target="#container-id_image_invalid" required id="id_image_invalid">
      </div>
    </label>
    <div data-file-container id="container-id_image_invalid" class="bx--file-container">
      <div class="bx--file__selected-file bx--file__selected-file--invalid"
          data-invalid>
        <p class="bx--file-filename"></p>
        <span data-for="prepopulated-file-uploader"
            class="bx--file__state-container">
          <svg focusable="false" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              class="bx--file--invalid" width="16" height="16"
              viewBox="0 0 16 16" aria-hidden="true">
            <path d="M8,1C4.2,1,1,4.2,1,8s3.2,7,7,7s7-3.1,7-7S11.9,1,8,1z M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2  c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z"></path>
            <path d="M7.5,4h1v5h-1C7.5,9,7.5,4,7.5,4z M8,12.2c-0.4,0-0.8-0.4-0.8-0.8s0.3-0.8,0.8-0.8 c0.4,0,0.8,0.4,0.8,0.8S8.4,12.2,8,12.2z" data-icon-path="inner-path" opacity="0"></path>
          </svg>
          <svg focusable="true" preserveAspectRatio="xMidYMid meet"
              xmlns="http://www.w3.org/2000/svg" fill="currentColor"
              aria-label="Remove uploaded file" class="bx--file-close"
              width="16" height="16" viewBox="0 0 32 32" role="img"
              tabindex="0">
            <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
          </svg>
        </span>
        <div class="bx--form-requirement">
          <div class="bx--form-requirement__title">File extension “” is not allowed.</div>
<p class="bx--form-requirement__supplement">Allowed extensions are: bmp, dib, gif, jfif, jpe, jpg, jpeg, pbm, pgm, ppm, pnm, png, apng, blp, bufr, cur, pcx, dcx, dds, ps, eps, fit, fits, fli, flc, ftc, ftu, gbr, grib, h5, hdf, jp2, j2k, jpc, jpf, jpx, j2c, icns, ico, im, iim, mpg, mpeg, tif, tiff, mpo, msp, palm, pcd, pdf, pxr, psd, qoi, bw, rgb, rgba, sgi, ras, tga, icb, vda, vst, webp, wmf, emf, xbm, xpm.</p>
        </div>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)

    def test_state_loading(self):
        template = """
{% load carbondesign %}
{% File form.image label="Account photo" is_loading=True %}
"""
        expected = """
<div class="bx--form-item">
  <strong class="bx--file--label">
    Account photo
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
      <div class="bx--file__selected-file">
        <p class="bx--file-filename"></p>
        <span data-for="prepopulated-file-uploader" class="bx--file__state-container">
          <div class="bx--inline-loading__animation">
            <div data-inline-loading-spinner="" class="bx--loading bx--loading--small">
              <svg class="bx--loading__svg" viewBox="-75 -75 150 150">
                <circle class="bx--loading__background" cx="0" cy="0" r="26.8125"></circle>
                <circle class="bx--loading__stroke" cx="0" cy="0" r="26.8125"></circle>
              </svg>
            </div>
          </div>
        </span>
      </div>
    </div>
  </div>
</div>
"""
        rendered = compare_template(template, expected)
        self.assertEqual(*rendered)
