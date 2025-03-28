from django.urls import path

from .views.api.nearest import NearestClinicsView


urlpatterns = [
    path("nearest/", NearestClinicsView.as_view(), name="api_register"),
]
