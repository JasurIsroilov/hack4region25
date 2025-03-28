from django.urls import path

from .views import (
    register_view,
    user_login_view,
    profile_view,
    logout_view,
)
from .views.api.register import (
    RegisterView,
)


urlpatterns = [
    path("register/", register_view, name="register"),
    path("login/", user_login_view, name="login"),
    path("profile/", profile_view, name="profile"),
    path('logout/', logout_view, name='logout'),
]
