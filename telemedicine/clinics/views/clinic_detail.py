from django.shortcuts import render, get_object_or_404
from clinics.models import Clinic


def clinic_detail(request, clinic_id):
    clinic = get_object_or_404(Clinic, clinic_id=clinic_id)
    clinic.region = clinic.city.region

    return render(
        request,
        'clinics/clinic_detail.html',
        {'clinic': clinic})
