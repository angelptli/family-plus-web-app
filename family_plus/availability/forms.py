from django import forms
from django.forms import widgets
from website_users.models import FamilyProfile
from availability.models import Availability
from availability.utils import define_days
from multiselectfield import MultiSelectFormField


class AvailabilityForm(forms.ModelForm):

    """Customize fields for Availability form that allows each user to have
    an availability log object that stores their days of availability.
    """

    days = MultiSelectFormField(choices=define_days(),
                                widget=forms.SelectMultiple(attrs={
                                    'class': 'form-select',
                                    'id': 'availability_select',
                                    'multiple': 'multiple'
                                }))
    
    def __init__(self, *args, **kwargs):
        """Filter FamilyProfile objects to get the current user and assign
        to the user field queryset.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form as related object
        self.request = kwargs.pop('request')
        super(AvailabilityForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = FamilyProfile.objects.filter(user=self.request.user)
        self.fields['user'].empty_label = None  # Remove empty label

    class Meta:
        model = Availability
        fields = ('days','user')

        # Customize widgets
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-select',
                'id': 'username_form_field',
            }),
        }
