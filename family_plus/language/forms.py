from django import forms
from django.forms import widgets
from website_users.models import FamilyProfile
from language.models import Language
from language.utils import define_languages
from multiselectfield import MultiSelectFormField


class LanguageForm(forms.ModelForm):

    """Customize fields for Language form that allows each user to have
    a language log object that stores their hobbies and interests.
    """

    languages = MultiSelectFormField(choices=define_languages(),
                                    widget=forms.SelectMultiple(attrs={
                                        'class': 'form-select',
                                        'id': 'language_select',
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
        super(LanguageForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = FamilyProfile.objects.filter(user=self.request.user)
        self.fields['user'].empty_label = None  # Remove empty label

    class Meta:
        model = Language
        fields = ('languages', 'user')

        # Customize widgets
        widgets = {
            'user': forms.Select(attrs={
                'class': 'form-select',
                'id': 'username_form_field',
            }),
        }
