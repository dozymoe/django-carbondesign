# pylint:disable=missing-module-docstring,missing-class-docstring,missing-function-docstring
from django import forms

class DummyForm(forms.Form):
    text = forms.CharField()
    text_missing = forms.CharField()
    choice = forms.ChoiceField(
            choices=(('val1', "Value One"), ('val2', "Value Two")))
    choice_missing = forms.ChoiceField(
            choices=(('val1', "Value One"), ('val2', "Value Two")))
    started_at = forms.DateTimeField()
    stopped_at = forms.DateTimeField()
    started_at_missing = forms.DateTimeField()
    stopped_at_missing = forms.DateTimeField()
