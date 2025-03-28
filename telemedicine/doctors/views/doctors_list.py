from django.shortcuts import render
from doctors.models import Doctor
from specializations.models import Specialization


def doctors_list(request):
    doctors = Doctor.objects.select_related('clinic').all()
    specs = Specialization.objects.all()

    return render(
        request,
        "doctors/doctors_list.html",
        {
            "doctors": doctors,
            "specs": specs,
        },
    )
