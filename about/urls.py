from django.urls import path
from .views import About_api, Email_api

urlpatterns = [
    path('email/', Email_api.as_view()),
    path('<str:idioma>/', About_api.as_view()),
]
