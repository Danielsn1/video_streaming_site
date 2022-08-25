from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext as _


class UserForm(forms.ModelForm):
    email = forms.EmailField(label='Enter Email:', required=True)
    password = forms.CharField(
        label='Enter Password:', widget=forms.PasswordInput, required=True, strip=True)
    confirm = forms.CharField(
        label='Confirm Password:', widget=forms.PasswordInput, required=True, strip=True)

    def save(self, commit=True):
        usr = super(UserForm, self).save(commit=False)

        if commit:
            usr = User.objects.create_user(usr.email, usr.email, usr.password)

        return usr

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

    class Meta:
        model = User
        fields = ('email', 'password', 'confirm')
