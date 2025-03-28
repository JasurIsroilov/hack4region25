from django.urls import path

from clinics.views.clinics_list import clinic_list
from clinics.views.clinic_detail import clinic_detail


urlpatterns = [
    path("", clinic_list, name="clinics_list"),
    path('clinics/<int:clinic_id>/', clinic_detail, name='clinic_detail'),
]
