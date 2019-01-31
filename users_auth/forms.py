from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("username")
        psw = cleaned_data.get("password")

        if name and psw:
            user = authenticate(username=name, password=psw)
            if user is None:
                msg = forms.ValidationError("Check the field!", code='invalid')
                self.add_error("username", msg)
                self.add_error("password", msg)
                raise forms.ValidationError(
                    "User with specified data does not exist! "
                    "Check username and password."
                )


class SignUpForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("username")
        psw = cleaned_data.get("password")
        psw2 = cleaned_data.get("password2")

        if name and psw and psw2:
            try:
                User.objects.get(username=name)
            except User.DoesNotExist:
                if psw != psw2:
                    msg = forms.ValidationError("Check the field!", code='invalid')
                    self.add_error("password", msg)
                    self.add_error("password2", msg)
                    raise forms.ValidationError(
                        "Password and Password2 must be the same!"
                    )
            else:
                self.add_error("username", forms.ValidationError("Please, type other username!", code='invalid'))
                raise forms.ValidationError(
                    "The username already exists!"
                )
