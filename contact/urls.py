from django.contrib import admin
from django.urls import path,include
from .views import Contact

urlpatterns = [
    path('', Contact.as_view()),
]