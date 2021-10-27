from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.urls import reverse_lazy
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import AccountSettingsForm, RegisterForm, PasswordChangingForm
from .forms import ProfilePageForm
from .models import FamilyProfile

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


class AccountSettingsView(generic.UpdateView):

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


class CreateProfileView(CreateView):
    model = FamilyProfile
    form_class = ProfilePageForm
    template_name = "family_profile/create-profile.html"
    # fields = '__all__'

    def form_valid(self, form):
        # Make user info available to the user filling out the form
        # so that saving the form will save to the correct user
        form.instance.user = self.request.user

        return super().form_valid(form)


class FamilyProfilePageView(DetailView):
    model = FamilyProfile
    template_name = 'family_profile/family-profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = FamilyProfile.objects.all()
        page_user = get_object_or_404(FamilyProfile, id=self.kwargs['pk'])

        context = super(FamilyProfilePageView, self).get_context_data(*args, **kwargs)
        context["page_user"] = page_user

        return context


class EditProfilePageView(generic.UpdateView):
    model = FamilyProfile
    form_class = ProfilePageForm
    template_name = 'family_profile/edit-family-profile.html'

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.object.pk})