# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class DummyForm(forms.Form):
    text = forms.CharField()
    text_empty = forms.CharField(required=False)
    text_missing = forms.CharField()

    number = forms.IntegerField()
    number_empty = forms.IntegerField(required=False)
    number_help = forms.IntegerField(required=False,
            label="Number input label",
            validators=[MaxValueValidator(100), MinValueValidator(0)],
            help_text="Optional helper text here; if message is more than one "
                "line text should wrap (~100 character count maximum)")
    number_invalid = forms.IntegerField(required=False,
            label="Number input label",
            validators=[MaxValueValidator(100), MinValueValidator(0)])
    number_helpinvalid = forms.IntegerField(required=False,
            label="Number input label",
            validators=[MaxValueValidator(100), MinValueValidator(0)],
            help_text="Optional helper text here; if message is more than one "
                "line text should wrap (~100 character count maximum)")
    number_missing = forms.IntegerField()

    choice = forms.ChoiceField(
            choices=(('val1', "Value One"), ('val2', "Value Two")))
    choice_missing = forms.ChoiceField(
            choices=(('val1', "Value One"), ('val2', "Value Two")))
    choice_empty = forms.ChoiceField(
            required=False,
            choices=(('val1', "Value One"), ('val2', "Value Two")),
            help_text="Optional helper text here")
    choice2 = forms.ChoiceField(
            required=False,
            choices=(
                ('red', "Radio button label"),
                ('green', "Radio button label"),
                ('blue', "Radio button label"),
            ))

    started_at = forms.DateTimeField()
    started_at_missing = forms.DateTimeField()
    started_at_empty = forms.DateTimeField(required=False)
    stopped_at = forms.DateTimeField()
    stopped_at_missing = forms.DateTimeField()

    time_tm = forms.TimeField(required=False)
    time_tm_missing = forms.TimeField(required=True)

    image = forms.ImageField(
            help_text="Only .jpg and .png files. 500kb max file size.")
    image_empty = forms.ImageField(
            required=False,
            help_text="Only .jpg and .png files. 500kb max file size.")
    #image_multi = forms.ImageField(
    #        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    #        help_text="Only .jpg and .png files. 500kb max file size.")
    #image_multi_missing = forms.ImageField(
    #        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    #        help_text="Only .jpg and .png files. 500kb max file size.")
    image_missing = forms.ImageField(
            help_text="Only .jpg and .png files. 500kb max file size.")
    image_invalid = forms.ImageField(
            help_text="Only .jpg and .png files. 500kb max file size.")

    toggle = forms.BooleanField(required=False,
            label="example toggle with state indicator text")
