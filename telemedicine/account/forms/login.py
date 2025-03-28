from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Telefon raqamingiz",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Telefon raqamingiz"})
    )
    password = forms.CharField(
        label="Parol",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Parolingiz"})
    )
