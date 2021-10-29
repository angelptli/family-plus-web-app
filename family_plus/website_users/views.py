from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.urls import reverse_lazy, reverse
# from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from .forms import AccountSettingsForm, RegisterForm, PasswordChangingForm
from .forms import ProfilePageForm
from .models import FamilyProfile
from django.conf import settings


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
    
    def form_valid(self, form):
        # Make user info available to the user filling out the form
        # so that saving the form will save to the correct user
        form.instance.user = self.request.user

        # Change family profile set up status to true
        FamilyProfile.has_family_profile(self.request.user)
    
        return super().form_valid(form)


class FamilyProfilePageView(DetailView):
    model = FamilyProfile
    template_name = 'family_profile/family-profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = FamilyProfile.objects.all()
        page_user = get_object_or_404(FamilyProfile, id=self.kwargs['pk'])

        context = super(FamilyProfilePageView, self).get_context_data(*args, **kwargs)
        context["page_user"] = page_user

        # if self.request.POST.get('toggle_hide_on'):
        #     FamilyProfile.hide_profile(self.request.user, "toggle_on")
        # elif self.request.POST.get('toggle_hide_off'):
        #     FamilyProfile.hide_profile("toggle_off")

        return context


def toggle_hide_profile(request, pk):
    """Users can click a button on their family profile to toggle the
    visibility of their profile to other  will toggle the hide_profile status to True.
    """
    submit_on = request.POST.get('toggle_hide_on', None)
    submit_off = request.POST.get('toggle_hide_off', None)

    profile_obj = FamilyProfile.objects.get(id=pk)


    if submit_on:
        # FamilyProfile.hide_profile(request.user, "toggle_on")
        profile_obj.hidden = True
    elif submit_off:
        # FamilyProfile.hide_profile(request.user, "toggle_off")
        profile_obj.hidden = False
   
    return HttpResponseRedirect(reverse('toggle-profile', args=[str(pk)]))
    # return HttpResponseRedirect(reverse('family-profile', args=[str(request.user.id)]))


class EditProfilePageView(generic.UpdateView):
    model = FamilyProfile
    form_class = ProfilePageForm
    template_name = 'family_profile/edit-family-profile.html'

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.object.pk})


# def unhide_family_profile(request, *args, **kwargs):
#     """Users who click the "Ready To Connect" button on their family
#     profile will toggle the hide_profile status to False.
#     """
#     context = {}

#     if request.method == "POST":
#         turn_hide_off = request.POST.get('turn_hide_off', None)

#         if turn_hide_off:
#             FamilyProfile.hide_profile("toggle_off")

#     return HttpResponseRedirect(reverse('family-profile'))

# class FamilyMemberListView(ListView):
#     model = settings.AUTH_USER_MODEL
#     context_object_name = "family_members"


# class FamilyMemberCreateView(CreateView):
#     model = settings.AUTH_USER_MODEL
#     fields = ('username', 'birthdate', 'country', 'city')


# class FamilyMemberUpdateView(UpdateView):
#     model = settings.AUTH_USER_MODEL
#     context_object_name = "family_members"
