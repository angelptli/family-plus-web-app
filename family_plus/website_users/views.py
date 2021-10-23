from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import AccountSettingsForm, RegisterForm, PasswordChangingForm


class UserRegisterView(generic.CreateView):

    """Create user register view for registering new users with a form.
    The success_url redirects the user to the login page after a successful
    registration.
    """

    # Credit: https://youtu.be/mpfHDSmqHds
    # Learned how to create a class-based view and specify a redirect
    # page for a successful user registration from this video tutorial by
    # John Elder, owner and instructor of Codemy.com.
    
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class AccountSettingsView(generic.CreateView):

    """Create edit profile view for users to edit the info on their profile
    page. The success_url redirects the user to their profile page after a
    successful save.
    """

    # Credit: https://youtu.be/R6-pB5PAA6s
    # Learned how to apply this form class to allow users to edit their
    # profile info. Video tutorial by John Elder, owner and instructor of
    # Codemy.com.
    
    form_class = AccountSettingsForm
    template_name = 'registration/account-settings.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        """Prefill the text boxes with already saved info on the user."""
        return self.request.user


class PasswordsChangeView(PasswordChangeView):

    """Allow user to change password and redirect to password changed
    success page.
    """

    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password-success')


def password_success(request):
    """Allows user to be redirected to a password changed success page."""
    return render(request, 'registration/password-success.html')