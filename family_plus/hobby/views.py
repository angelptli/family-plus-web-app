from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from hobby.models import Hobby
from hobby.forms import HobbyForm


class CreateHobbyLogView(LoginRequiredMixin, CreateView):

    """Users who have set up a family profile can create objects to
    represent members of their family.
    """

    model = Hobby
    form_class = HobbyForm
    template_name = "hobby/create-hobby-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form as foreign key
        kwargs = super(CreateHobbyLogView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.request.user.familyprofile.pk})


class EditHobbyLogView(LoginRequiredMixin, UpdateView):

    """Allow users to edit the info stored on their family member objects."""

    model = Hobby
    form_class = HobbyForm
    template_name = "hobby/edit-hobby-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        """Add the family member object to the context dictionary and
        a user object to confirm the correct user has permission to
        edit the family object.
        """
        hobby_log = get_object_or_404(Hobby, id=self.kwargs['pk'])
        context = super(EditHobbyLogView, self).get_context_data(*args, **kwargs)
        context['hobby_log'] = hobby_log

        # Pass in string username for username comparison and authentication
        str_user = str(hobby_log.user)
        context['str_user'] = str_user

        return context

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for prefilling the form with the username
        kwargs = super(EditHobbyLogView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.request.user.familyprofile.pk})
