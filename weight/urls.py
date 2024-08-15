from django.urls import path 
from . import views

urlpatterns = [
    path('mass_input', views.mass_input, name='mass input'),
]