from django.db import models

from cities.models import City


class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    about = models.TextField(blank=True, null=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='clinics')

    def __str__(self):
        return self.name
