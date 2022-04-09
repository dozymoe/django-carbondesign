"""
Inline Loading
==============

See: https://www.carbondesignsystem.com/components/inline-loading/usage/

The inline loading component provides visual feedback that data is being
processed.

Overview
--------

Inline loading spinners are used when performing actions. They notify to
the user that their request is being processed. Although they do not provide
details about what is occurring on the back-end, they reassure the user that
their action is being processed.

Common actions that benefit from inline loading include any create, update,
or delete actions that may have a lot of data to process. It can be used in
a table, after a primary or secondary button click, or even in a modal.
""" # pylint:disable=line-too-long
# pylint:disable=too-many-lines

from django.utils.translation import gettext as _
#-
from .base import Node

class InlineLoading(Node):
    """Inline Loading component.
    """

    def prepare(self, values, context):
        """Prepare values for rendering the templates.
        """
        values['txt_loading'] = _("Loading data...")
        values['txt_loaded'] = _("Data loaded.")
        values['txt_failed'] = _("Loading data failed.")


    def render_default(self, values, context):
        """Output html of the component.
        """
        template = """
<div data-inline-loading class="bx--inline-loading" role="alert"
    aria-live="assertive">
  <div class="bx--inline-loading__animation">
    <div data-inline-loading-spinner class="bx--loading bx--loading--small">
      <svg class="bx--loading__svg" viewBox="0 0 100 100">
        <circle class="bx--loading__background" cx="50%" cy="50%" r="42" />
        <circle class="bx--loading__stroke" cx="50%" cy="50%" r="42" />
      </svg>
    </div>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--inline-loading__checkmark-container" hidden=""
        data-inline-loading-finished="" width="16" height="16"
        viewBox="0 0 16 16" aria-hidden="true">
      <path d="M8,1C4.1,1,1,4.1,1,8c0,3.9,3.1,7,7,7s7-3.1,7-7C15,4.1,11.9,1,8,1z M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z"></path>
      <path d="M7,11L4.3,8.3l0.9-0.8L7,9.3l4-3.9l0.9,0.8L7,11z" data-icon-path="inner-path" opacity="0"></path>
    </svg>
    <svg focusable="false" preserveAspectRatio="xMidYMid meet"
        xmlns="http://www.w3.org/2000/svg" fill="currentColor"
        class="bx--inline-loading--error" hidden="" data-inline-loading-error=""
        width="20" height="20" viewBox="0 0 32 32" aria-hidden="true">
      <path d="M2,16H2A14,14,0,1,0,16,2,14,14,0,0,0,2,16Zm23.15,7.75L8.25,6.85a12,12,0,0,1,16.9,16.9ZM8.24,25.16A12,12,0,0,1,6.84,8.27L23.73,25.16a12,12,0,0,1-15.49,0Z"></path>
    </svg>
  </div>
  <p data-inline-loading-text-active class="bx--inline-loading__text">
    {txt_loading}
  </p>
  <p data-inline-loading-text-finished hidden class="bx--inline-loading__text">
    {txt_loaded}
  </p>
  <p data-inline-loading-text-error hidden class="bx--inline-loading__text">
    {txt_failed}
  </p>
</div>
"""
        return self.format(template, values)


components = {
    'InlineLoading': InlineLoading,
}
