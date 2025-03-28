from django.urls import path

from results.views.results_list import results_list


urlpatterns = [
    path("", results_list, name="results_list"),
]
