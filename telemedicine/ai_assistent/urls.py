from django.urls import path

from ai_assistent.views import get_ai_page


urlpatterns = [
    path("", get_ai_page, name="ai_page"),
]
