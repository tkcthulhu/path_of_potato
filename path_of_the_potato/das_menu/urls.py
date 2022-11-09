from django.urls import path, include

from . import views

urlpatterns = [
    path('full_menu/', views.get_full_menu),
]