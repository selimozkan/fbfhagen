from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(
        max_length=250, required=True, validators=[EmailValidator()]
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
