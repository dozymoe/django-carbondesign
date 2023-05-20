"""Custom form widgets.
"""
from django.forms.widgets import CheckboxInput, Input, Textarea, TextInput

class CustomNameInput(Input):
    """Input widget where you can change html attribute: name.
    """
    def get_context(self, name, value, attrs):
        """Modify so we can override name attribute.
        """
        name =  attrs.pop('name', name)
        value =  attrs.pop('value', value)
        return super().get_context(name, value, attrs)


class CustomCheckboxInput(CustomNameInput, CheckboxInput):
    """Checkbox widget where you can change html attribute: name.
    """
    def use_required_attribute(self, initial):
        """Checkbox that is part of a fieldset doesn't need required attribute
        """
        return False


class CustomTextarea(CustomNameInput, Textarea):
    """Textarea widget where you can change html attribute: name.
    """

class CustomTextInput(CustomNameInput, TextInput):
    """TextInput widget where you can change html attribute: name.
    """
