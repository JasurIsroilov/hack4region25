from django.urls import path

from doctors.views.doctors_list import doctors_list


urlpatterns = [
    path("", doctors_list, name="doctors_list"),
]
