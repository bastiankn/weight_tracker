from django.urls import path
from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("register/", views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    #path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
