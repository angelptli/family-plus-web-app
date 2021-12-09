from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView
from language.models import Language
from language.forms import LanguageForm


class CreateLanguageLogView(LoginRequiredMixin, CreateView):

    """Users can indicate the languages know and/or are interesting in and
    display on their family profile.
    """

    model = Language
    form_class = LanguageForm
    template_name = "language/create-language-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form as foreign key
        kwargs = super(CreateLanguageLogView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        """After a user successfully creates a language object, the user will
        be returned to their family profile.
        """
        return reverse_lazy('family-profile', kwargs={'pk': self.request.user.familyprofile.pk})


class EditLanguageLogView(LoginRequiredMixin, UpdateView):

    """Users can edit their list of languages displayed on their family
    profile.
    """

    model = Language
    form_class = LanguageForm
    template_name = "language/edit-language-log.html"
    login_url = '/users/login/'
    redirect_field_name = 'redirect_to'

    def get_context_data(self, *args, **kwargs):
        """Add user's language list and username to the context dictionary."""
        language_log = get_object_or_404(Language, id=self.kwargs['pk'])
        context = super(EditLanguageLogView, self).get_context_data(*args, **kwargs)
        context['language_log'] = language_log

        # Pass in string username for username comparison and authentication
        str_user = str(language_log.user)
        context['str_user'] = str_user

        return context

    def get_form_kwargs(self):
        """Pass request object to the form class to request current user's
        username and prefill their username field.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for prefilling the form with the username
        kwargs = super(EditLanguageLogView, self).get_form_kwargs()
        kwargs['request'] = self.request

        return kwargs

    def get_success_url(self):
        """After a user successfully updates a language object, the user will
        be returned to their family profile.
        """
        return reverse_lazy('family-profile', kwargs={'pk': self.request.user.familyprofile.pk})
