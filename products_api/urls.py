from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.GetCategories.as_view()),
    path('category/<str:idioma>/', views.GetCategories.as_view()),
    path('category/<int:category>/<str:idioma>/', views.Get_Products_Of_Category.as_view()),
]

