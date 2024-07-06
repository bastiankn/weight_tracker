from django.urls import path 
from . import views

urlpatterns = [
    path('workoutplan', views.plan, name='plan'),
]