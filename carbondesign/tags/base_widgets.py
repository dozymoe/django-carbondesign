from django.forms.widgets import Input, TextInput

class CustomNameInput(Input):

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if context['widget']['attrs'].get('name') is not None:
            context['widget']['name'] = context['widget']['attrs']['name']
        return context


class CustomTextInput(TextInput, CustomNameInput):
    pass
