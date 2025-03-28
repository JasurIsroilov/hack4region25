from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required")

        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone_number, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, null=False)
    second_name = models.CharField(max_length=50, null=False)
    patronymic = models.CharField(max_length=50, blank=False, null=False)
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=False)
    role = models.CharField(max_length=20,
                            choices=[("admin", "Admin"), ("user", "User"), ("secretary", "Secretary")],
                            default="user")

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = [
        "first_name",
        "second_name",
        "patronymic",
        "email",
        "birth_date",
    ]

    def __str__(self):
        return f"{self.first_name} {self.second_name} ({self.email})"
