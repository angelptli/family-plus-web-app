from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse

# Imports relating to views and forms
from django.views import generic
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Import models
from website_users.models import FamilyProfile, FamilyMember

# Import forms
from website_users.forms import (
    AccountSettingsForm,
    RegisterForm,
    PasswordChangingForm,
    ProfilePageForm,
    FamilyMemberForm,
    EditFamilyMemberForm
)

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


@login_required(login_url='/users/login/')
def password_success(request):
    """Allows user to be redirected to a password changed success page."""
    return render(request, 'registration/password-success.html')


class CreateProfileView(LoginRequiredMixin, CreateView):

    """Allow user to create a family profile."""

    model = FamilyProfile
    form_class = ProfilePageForm
    template_name = "family_profile/create-profile.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'
    
    def form_valid(self, form):
        # Make user info available to the user filling out the form
        # so that saving the form will save to the correct user
        form.instance.user = self.request.user

        # Change family profile set up status to true
        FamilyProfile.has_family_profile(self.request.user)
    
        return super().form_valid(form)


class FamilyProfilePageView(LoginRequiredMixin, DetailView):
    
    """This view displays the family profiles of users."""

    # Inspired by: https://www.youtube.com/watch?v=dwgIi8dspa4
    # Learned how to create a profile page view.

    model = FamilyProfile
    template_name = 'family_profile/family-profile.html'
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        """Define the different states of family profiles to determine
        the different displays for different user connections. 
        """
        # Add to the context dictionary the family profile object of the
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
       
        # Make each user's family member objects available to the template
        family_members = FamilyMember.objects.filter(user=page_user)

        # Add the variables to the context dictionary
        context["page_user"] = page_user
        context["is_hidden"] = is_hidden
        context['profile_hidden'] = profile_hidden
        context['view_hidden'] = view_hidden
        context['family_members'] = family_members

        return context


class EditProfilePageView(LoginRequiredMixin, generic.UpdateView):

    """Allow user to edit the info stored on their family profile."""

    model = FamilyProfile
    form_class = ProfilePageForm
    template_name = 'family_profile/edit-family-profile.html'
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.object.pk})


@login_required(login_url='/users/login/')
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


class FamilyMemberView(LoginRequiredMixin, ListView):

    """Show an individual view for each family member object where the
    user can choose to edit data or delete the object.
    """

    model = FamilyMember
    template_name = "family_profile_body/family-member-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        """Add the family member object to the context dictionary and
        a string username to confirm the correct user has permission to
        edit and the delete family objects.
        """
        member = get_object_or_404(FamilyMember, id=self.kwargs['pk'])
        context = super(FamilyMemberView, self).get_context_data(*args, **kwargs)
        context['member'] = member

        # Pass in string username for username comparison and authentication
        str_user = str(member.user)
        context['str_user'] = str_user

        return context


class AddFamilyMemberView(LoginRequiredMixin, CreateView):

    """Users who have set up a family profile can create objects to
    represent members of their family.
    """

    model = FamilyMember
    form_class = FamilyMemberForm
    template_name = "family_profile_body/add-family-member.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form as foreign key
        kwargs = super(AddFamilyMemberView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.request.user.familyprofile.pk})


class EditMemberInfoView(LoginRequiredMixin, UpdateView):

    """Allow users to edit the info stored on their family member objects."""

    model = FamilyMember
    form_class = EditFamilyMemberForm
    template_name = "family_profile_body/edit-member-info.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        """Add the family member object to the context dictionary and
        a user object to confirm the correct user has permission to
        edit the family object.
        """
        member = get_object_or_404(FamilyMember, id=self.kwargs['pk'])
        context = super(EditMemberInfoView, self).get_context_data(*args, **kwargs)
        context['member'] = member

        # Pass in string username for username comparison and authentication
        str_user = str(member.user)
        context['str_user'] = str_user

        return context

    def get_success_url(self):
        return reverse_lazy('family-member-log', kwargs={'pk': self.object.pk})


@login_required(login_url='/users/login/')
def delete_member_view(request, pk):
    """Delete the family member object from the database when requested
    by the user who is clicking the delete button.
    """
    if pk:
        FamilyMember.objects.filter(pk=pk).delete()

    return HttpResponseRedirect(reverse('family-profile', args=[str(request.user.familyprofile.pk)]))