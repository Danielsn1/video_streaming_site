from django import forms
from django.utils.translation import gettext as _

class UserForm(forms.Form):
    email = forms.EmailField(label='Enter Email:', required=True)
    password = forms.CharField(label='Enter Password:', widget=forms.PasswordInput, required=True, strip=True)
    confirm = forms.CharField(label='Confirm Passowrd:', widget=forms.PasswordInput, required=True, strip=True)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm")

        if password and confirm:
            
            if password != confirm:
                raise forms.ValidationError(
                    _("Passwords don't match"),
                    code='invalid',
                )