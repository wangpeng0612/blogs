from django.urls import path, reverse_lazy
from . import views
from . import forms
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", views.register, name='user_register'),
    path("login/", LoginView.as_view(template_name='account/login.html', form_class=forms.AuthenticationForm1),
         name='user_login'),
    path("logout/", LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
]
