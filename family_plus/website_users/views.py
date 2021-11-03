from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse

# Imports relating to views and forms
from django.views import generic
from django.views.generic import CreateView, DetailView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AccountSettingsForm, RegisterForm, PasswordChangingForm
from .forms import ProfilePageForm
from .models import FamilyProfile
from custom_user_model.models import CustomUserModel


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


class AccountSettingsView(LoginRequiredMixin, generic.UpdateView):

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
    raise_exception = True  # 403 Forbidden view when not logged in

    def get_object(self):
        """Prefill the text boxes with already saved info on the user."""
        return self.request.user      


class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):

    """Allow user to change password and redirect to password changed
    success page.
    """

    # form_class = PasswordChangeForm
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password-success')
    raise_exception = True  # 403 Forbidden view when not logged in


def password_success(request):
    """Allows user to be redirected to a password changed success page."""
    return render(request, 'registration/password-success.html')


class CreateProfileView(CreateView):
    model = FamilyProfile
    form_class = ProfilePageForm
    template_name = "family_profile/create-profile.html"
    
    def form_valid(self, form):
        # Make user info available to the user filling out the form
        # so that saving the form will save to the correct user
        form.instance.user = self.request.user

        # Change family profile set up status to true
        FamilyProfile.has_family_profile(self.request.user)
    
        return super().form_valid(form)


class FamilyProfilePageView(DetailView):
    
    """This view displays the family profiles of users."""

    # Inspired by: https://www.youtube.com/watch?v=dwgIi8dspa4
    # Learned how to create a profile page view.

    model = FamilyProfile
    template_name = 'family_profile/family-profile.html'

    def get_context_data(self, *args, **kwargs):
        """Define the different states of family profiles to determine
        the different displays for different user connections. 
        """
        # Add to the context dictionary the family profile id of the
        # profile being visited
        page_user = get_object_or_404(FamilyProfile, id=self.kwargs['pk'])
        context = super(FamilyProfilePageView, self).get_context_data(*args, **kwargs)

        # Status of 1 for hidden family profile, 0 elsewise
        profile_page = get_object_or_404(FamilyProfile, id=self.kwargs['pk'])
        is_hidden = profile_page.profile_hidden()  # 1 for hidden, 0 elsewise

        # Toggler for hide family profile button
        profile_hidden = False
        if profile_page.hidden.filter(id=self.request.user.id).exists():
            profile_hidden = True

        # Determine whether the profile being viewed is hidden
        view_hidden = False
        if FamilyProfile.objects.filter(hidden__username=page_user).exists():
            view_hidden = True

        # Determine whether the user is already on the other user's
        # pending list
        request_sent = False
        if profile_page.pending_requests.filter(id=self.request.user.id).exists():
            request_sent = True

        # Add the variables to the context dictionary
        context["page_user"] = page_user
        context["is_hidden"] = is_hidden
        context['profile_hidden'] = profile_hidden
        context['view_hidden'] = view_hidden
        context['request_sent'] = request_sent

        return context


class EditProfilePageView(generic.UpdateView):
    model = FamilyProfile
    form_class = ProfilePageForm
    template_name = 'family_profile/edit-family-profile.html'

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.object.pk})


def toggle_hide_profile(request, pk):
    """Users can click a button on their family profile to toggle the
    visibility of their profile to other  will toggle the hide_profile status to True.
    """

    # Credit: https://www.youtube.com/watch?v=dwgIi8dspa4
    # Learned how to define states for a toggle on/off button for hiding
    # family profiles from other users.

    profile_page = get_object_or_404(FamilyProfile, id=request.POST.get('profile_id'))

    profile_hidden = False
    if profile_page.hidden.filter(id=request.user.id).exists():
        profile_page.hidden.remove(request.user)
        profile_hidden = False
    else:
        profile_page.hidden.add(request.user)
        profile_hidden = True

    return HttpResponseRedirect(reverse('family-profile', args=[str(pk)]))


def no_profile_view(request, *args, **kwargs):
    """Return a profile not found view when visiting a user who has not
    set up a family profile.
    """
    return render(request, 'family_profile/no-profile.html')
