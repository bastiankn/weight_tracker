from django.urls import path
from . import views

urlpatterns = [
    path('shutdown/', views.shutdown, name='shutdown'),
]