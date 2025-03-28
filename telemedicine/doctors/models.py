from django.db import models

from specializations.models import Specialization
from clinics.models import Clinic


class Doctor(models.Model):

    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    experience = models.IntegerField()
    email = models.EmailField(unique=True)
    about = models.TextField(blank=True, null=True)
    sc_degree = models.CharField(max_length=255, blank=True, null=True)

    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE, related_name='doctors')
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, related_name="clinics")

    def __str__(self):
        return f"{self.second_name} {self.first_name} {self.patronymic}"
