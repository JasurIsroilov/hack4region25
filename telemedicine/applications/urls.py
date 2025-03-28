from django.urls import path

from applications.views.application_list import applications_list


urlpatterns = [
    path("", applications_list, name="applications_list"),
]
