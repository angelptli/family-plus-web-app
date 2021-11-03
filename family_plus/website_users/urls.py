"""family_plus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.forms import UserChangeForm
from django.urls import path
from user_connections.views import send_request_view, cancel_request
from .views import (
    AccountSettingsView,
    UserRegisterView,
    PasswordsChangeView,
    FamilyProfilePageView,
    EditProfilePageView,
    CreateProfileView,
    password_success,
    toggle_hide_profile,
    no_profile_view,
)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('account_settings/', AccountSettingsView.as_view(), name='account-settings'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_success', password_success, name='password-success'),
    path('<int:pk>/family_profile/', FamilyProfilePageView.as_view(), name='family-profile'),
    path('<int:pk>/edit_family_profile/', EditProfilePageView.as_view(), name='edit-family-profile'),
    path('create_profile/', CreateProfileView.as_view(), name='create-profile'),
    path('toggle/<int:pk>', toggle_hide_profile, name='toggle-profile'),
    path('profile_not_found/', no_profile_view, name='profile-not-found'),
    path('send_request/<int:pk>', send_request_view, name='send-request'),
    path('cancel_request/<int:pk>', cancel_request, name='cancel-request'),
]
