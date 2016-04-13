from django import forms


class CheckKeyForm(forms.Form):
    key = forms.CharField(max_length=4)
