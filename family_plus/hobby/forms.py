from django import forms
from django.forms import widgets
from website_users.models import FamilyProfile
from hobby.models import Hobby
from hobby.utils import define_hobbies
from multiselectfield import MultiSelectFormField


class HobbyForm(forms.ModelForm):

    """Customize fields for Hobby form that allows each user to have
    a hobby log object that stores their hobbies and interests.
    """

    hobbies = MultiSelectFormField(choices=define_hobbies(),
                                    widget=forms.SelectMultiple(attrs={
                                        'class': 'form-select',
                                        'id': 'hobby_select',
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
        super(HobbyForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = FamilyProfile.objects.filter(user=self.request.user)
        self.fields['user'].empty_label = None  # Remove empty label

    class Meta:

        """Specify the fields to include in the register form."""

        model = Hobby
        fields = ('hobbies', 'other', 'user')

        # Customize widgets
        widgets = {
            # 'other': forms.Textarea(attrs={
            #     'class': 'form-control',
            #     'rows': '4',
            #     'style': 'max-height: 200px; border-width: 1px; border-color: #137ac483;'
            # }),
            'user': forms.Select(attrs={
                'class': 'form-select',
                'id': 'username_form_field',
            }),
        }
