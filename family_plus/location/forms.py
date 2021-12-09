from django import forms
from website_users.models import FamilyProfile
from location.models import Location


class AddLocationForm(forms.ModelForm):

    """Customize fields for form that allows each user to add a
    sub-profile for each family member they add to their family profile.
    """

    def __init__(self, *args, **kwargs):
        """Filter FamilyProfile objects to get the current user and assign
        to the user field queryset.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form
        self.request = kwargs.pop('request')
        super(AddLocationForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = FamilyProfile.objects.filter(user=self.request.user)
        self.fields['user'].empty_label = None  # Remove empty label

    class Meta:

        """Specify the fields to include in the register form."""

        model = Location
        fields = ('state', 'city', 'user')

        # Customize widgets
        widgets = {
            'state': forms.Select(attrs={
                'class': 'form-select',
                'id': 'state_select',
                'required': 'required'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'city_select'
            }),
            'user': forms.Select(attrs={
                'class': 'form-select border',
                'id': 'user_select',
                # 'style': 'max-height: 200px; width: fit-content; border-color: #137ac483;'
            }),
        }
