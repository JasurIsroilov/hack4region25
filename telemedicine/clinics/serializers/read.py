from rest_framework import serializers
from ..models import Clinic


class ClinicReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clinic
        fields = ["clinic_id", "name", "latitude", "longitude"]
