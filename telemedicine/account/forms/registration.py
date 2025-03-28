from django import forms
from django.contrib.auth.forms import UserCreationForm
from ..models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = [
            "phone_number",
            "first_name",
            "second_name",
            "patronymic",
            "email",
            "birth_date",
            "password1",
            "password2",
        ]
