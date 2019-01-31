from django import forms
from django.contrib.auth import authenticate, login


class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("username")
        psw = cleaned_data.get("password")

        if name and psw:
            # Only do something if both fields are valid so far.
            user = authenticate(username=name, password=psw)

            if user is None:
                msg = forms.ValidationError("Check the field!", code='invalid')
                self.add_error("username", msg)
                self.add_error("password", msg)
                raise forms.ValidationError(
                    "User with specified data does not exist! "
                    "Check username and password."
                )
