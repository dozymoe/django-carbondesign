"""
File Uploader
=============

See: https://www.carbondesignsystem.com/components/file-uploader/usage/

File uploaders allow users to select one or more files to upload to a specific
location.

Overview
--------

File uploaders allow users to upload content of their own. A file uploader is
commonly found in forms, but can also live as a standalone element. There are
two variants of file uploaders—our default file uploader and a drag and drop
file uploader.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import FormNode

class FileUploader(FormNode):
    """File Uploader component.
    """
    NODE_PROPS = ('is_loading',)
    "Extended Template Tag arguments."

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_drop'] = _("Drag and drop files here or upload")
        values['txt_clear'] = _("Remove uploaded file")


    def prepare_element_props(self, props, context):
        """Prepare html attributes for rendering the form element.
        """
        props['class'].append('bx--file-input')
        props['data-file-uploader'] = ''
        props['data-target'] = '#container-' + self._id


    def render_default(self, values, context):
        """Output html of the component.
        """
        values['filename'] = self.bound_field.value() or ''

        if self.bound_field.errors:
            template = """
<div class="bx--form-item">
  <strong class="bx--file--label {label_class}" {label_props}>
    {label}{label_suffix}
  </strong>
  {tmpl_help}
  <div class="bx--file" data-file>
    <label for="{id}" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        {txt_drop}
        {tmpl_element}
      </div>
    </label>
    <div data-file-container id="container-{id}" class="bx--file-container">
      <div class="bx--file__selected-file bx--file__selected-file--invalid"
          data-invalid>
        <p class="bx--file-filename">{filename}</p>
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
              aria-label="{txt_clear}" class="bx--file-close"
              width="16" height="16" viewBox="0 0 32 32" role="img"
              tabindex="0">
            <path d="M24 9.4L22.6 8 16 14.6 9.4 8 8 9.4 14.6 16 8 22.6 9.4 24 16 17.4 22.6 24 24 22.6 17.4 16 24 9.4z"></path>
          </svg>
        </span>
        <div class="bx--form-requirement">
          {tmpl_errors}
        </div>
      </div>
    </div>
  </div>
</div>
"""
        elif self.eval(self.kwargs.get('is_loading'), context):
            template = """
<div class="bx--form-item">
  <strong class="bx--file--label {label_class}" {label_props}>
    {label}{label_suffix}
  </strong>
  {tmpl_help}
  <div class="bx--file" data-file>
    <label for="{id}" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        {txt_drop}
        {tmpl_element}
      </div>
    </label>
    <div data-file-container id="container-{id}" class="bx--file-container">
      <div class="bx--file__selected-file">
        <p class="bx--file-filename">{filename}</p>
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
        elif values['filename']:
            template = """
<div class="bx--form-item">
  <strong class="bx--file--label {label_class}" {label_props}>
    {label}{label_suffix}
  </strong>
  {tmpl_help}
  <div class="bx--file" data-file>
    <label for="{id}" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        {txt_drop}
        {tmpl_element}
      </div>
    </label>
    <div data-file-container id="container-{id}" class="bx--file-container">
      <div class="bx--file__selected-file">
        <p class="bx--file-filename">{filename}</p>
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
        else:
            template = """
<div class="bx--form-item">
  <strong class="bx--file--label {label_class}" {label_props}>
    {label}{label_suffix}
  </strong>
  {tmpl_help}
  <div class="bx--file" data-file>
    <label for="{id}" class="bx--file-browse-btn" role="button" tabindex="0">
      <div data-file-drop-container class="bx--file__drop-container">
        {txt_drop}
        {tmpl_element}
      </div>
    </label>
    <div data-file-container id="container-{id}" class="bx--file-container">
    </div>
  </div>
</div>
"""
        return self.format(template, values, context)


    def render_tmpl_help(self, values, context):
        """Dynamically render a part of the component's template.
        """
        if self.bound_field.help_text:
            tmpl = """
<p id="hint-{id}" class="bx--label-description {class}" {props}>
  {child}
</p>
"""
            help_values = {
                'child': self.bound_field.help_text,
                'id': values['id'],
                'class': values['help_class'],
                'props': values['help_props'],
            }
            return tmpl.format(**help_values)
        return ''


components = {
    'File': FileUploader,
}
