from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from availability.models import Availability
from availability.forms import AvailabilityForm


class CreateAvailabilityLogView(LoginRequiredMixin, CreateView):

    """Save user availability schedules indicating which days they are
    usually free to connect and interact with other users.
    """

    model = Availability
    form_class = AvailabilityForm
    template_name = "availability/create-availability-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form
        kwargs = super(CreateAvailabilityLogView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.request.user.familyprofile.pk})


class EditAvailabilityLogView(LoginRequiredMixin, UpdateView):

    """Update user family availability schedules."""

    model = Availability
    form_class = AvailabilityForm
    template_name = "availability/edit-availability-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        """Add user's availability schedules and username to the context
        dictionary.
        """
        availability_log = get_object_or_404(Availability, id=self.kwargs['pk'])
        context = super(EditAvailabilityLogView, self).get_context_data(*args, **kwargs)
        context['availability_log'] = availability_log

        # Pass in string username for username comparison and authentication
        str_user = str(availability_log.user)
        context['str_user'] = str_user

        return context

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for prefilling the form with the username
        kwargs = super(EditAvailabilityLogView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        return reverse_lazy('family-profile', kwargs={'pk': self.request.user.familyprofile.pk})
