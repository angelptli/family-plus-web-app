from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):

    """Create user register view for registering new users with a form.
    The success_url redirects the user to the login page after a successful
    registration.

    Inspried by: https://youtu.be/mpfHDSmqHds
    """

    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')