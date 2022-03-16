"""Custom form widgets.
"""
from django.forms.widgets import Input, TextInput

class CustomNameInput(Input):
    """Input widget where you can change html attribute: name.
    """
    def get_context(self, name, value, attrs):
        """Modify so we can override name attribute.
        """
        context = super().get_context(name, value, attrs)
        for attr in ('name', 'value'):
            if context['widget']['attrs'].get(attr) is None:
                continue
            context['widget'][attr] = context['widget']['attrs'][attr]
        return context


class CustomTextInput(TextInput, CustomNameInput):
    """TextInput widget where you can change html attribute: name.
    """
