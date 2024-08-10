from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required 
from django.urls import reverse_lazy

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
] 
