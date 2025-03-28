from django.urls import path

from .views.api.register import (
    RegisterView,
)
from .views.api.login import CustomTokenObtainPairView


urlpatterns = [
    path("register/", RegisterView.as_view(), name="api_register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair")
]
