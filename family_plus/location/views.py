from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse

# Imports relating to views
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Import models
from website_users.models import FamilyProfile
from location.models import Location

# Import forms
from location.forms import AddLocationForm


class LocationLogView(LoginRequiredMixin, ListView):

    """Display a view that lists the locations the user added to their
    family profile.
    """

    model = Location
    template_name = "location/location-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        """Add the location object to the context dictionary."""
        context = super(LocationLogView, self).get_context_data(*args, **kwargs)
        profile = FamilyProfile.objects.get(id=self.request.user.familyprofile.id)
        location_objects = Location.objects.filter(user=profile)
        context['location_objects'] = location_objects

        return context


class AddLocationView(LoginRequiredMixin, CreateView):

    """Users who have set up a family profile can create objects to
    represent members of their family.
    """

    model = Location
    form_class = AddLocationForm
    template_name = "location/add-location.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form as foreign key
        kwargs = super(AddLocationView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        """After a user creates a location object, the user will be returned
        to the location log and will see a list of their location objects.
        """
        return reverse_lazy('location-log', kwargs={'user': self.request.user})

@login_required(login_url='/users/login/')
def delete_location(request, pk):
    """Delete a location object from the database when requested
    by the user who is clicking the delete button.
    """
    if pk:
        Location.objects.filter(pk=pk).delete()

    return HttpResponseRedirect(reverse('location-log', args=[str(request.user.username)]))