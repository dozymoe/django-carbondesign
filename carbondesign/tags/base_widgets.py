from django.forms.widgets import Input, TextInput

class CustomNameInput(Input):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        for attr in ('name', 'value'):
            if context['widget']['attrs'].get(attr) is None:
                continue
            context['widget'][attr] = context['widget']['attrs'][attr]
        return context


class CustomTextInput(TextInput, CustomNameInput):
    pass
