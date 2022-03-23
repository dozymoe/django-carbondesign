# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms

class DummyForm(forms.Form):
    text = forms.CharField()
    text_empty = forms.CharField(required=False)
    text_missing = forms.CharField()

    number = forms.IntegerField()
    number_missing = forms.IntegerField()

    choice = forms.ChoiceField(
            choices=(('val1', "Value One"), ('val2', "Value Two")))
    choice_missing = forms.ChoiceField(
            choices=(('val1', "Value One"), ('val2', "Value Two")))

    started_at = forms.DateTimeField()
    started_at_missing = forms.DateTimeField()
    started_at_empty = forms.DateTimeField(required=False)
    stopped_at = forms.DateTimeField()
    stopped_at_missing = forms.DateTimeField()

    image = forms.ImageField(
            help_text="Only .jpg and .png files. 500kb max file size.")
    image_empty = forms.ImageField(
            required=False,
            help_text="Only .jpg and .png files. 500kb max file size.")
    image_multi = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={'multiple': True}),
            help_text="Only .jpg and .png files. 500kb max file size.")
    image_multi_missing = forms.ImageField(
            widget=forms.ClearableFileInput(attrs={'multiple': True}),
            help_text="Only .jpg and .png files. 500kb max file size.")
    image_missing = forms.ImageField(
            help_text="Only .jpg and .png files. 500kb max file size.")
    image_invalid = forms.ImageField(
            help_text="Only .jpg and .png files. 500kb max file size.")
