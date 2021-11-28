from custom_user_model.models import CustomUserModel
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from website_users.models import FamilyMember, FamilyProfile
import string


class RegisterForm(UserCreationForm):

    """Define the email and name variables to include as additional
    fields in the register form.
    """

    # Inspired by: https://youtu.be/TBGRYkzXiTg
    # Learned how to customize and connect additional form fields
    # for the register form from this video tutorial.
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control',
                             'id': 'email_input'}))

    username = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username_input'}))

    password1 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'type': 'password',
                                    'id': 'password1_input'}))

    password2 = forms.CharField(max_length=100,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'type': 'password',
                                    'id': 'password2_input'}))
    
    class Meta:

        """Specify the fields to include in the register form."""

        model = CustomUserModel
        fields = ('email', 'username', 'password1', 'password2',
                  'family_relation_status', 'is_adult')

        widgets = {
            'family_relation_status': forms.Select(attrs={
                'class': 'form-select',
                'id': 'family_relation_status_select',
                'style': 'max-height: 200px; width: fit-content; border-color: #137ac483;'
            }),
            'is_adult': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': 'checkbox',
                'id': 'is_adult_check_box',
                'required': 'required'
            }),
        }

    def clean(self):
        """Validate username input and return cleaned data."""
        cleaned_data = super(RegisterForm, self).clean()
        username = cleaned_data.get("username")

        # Raise error if username contains space
        if username.isspace():
            raise forms.ValidationError(
                "Username can only contain the following: a-z A-Z 0-9 _")

        # Raise error if username contains special characters
        special_chars = set(string.punctuation.replace("_", ""))
        if any(char in special_chars for char in username):
            raise forms.ValidationError(
                "Username can only contain the following: a-z A-Z 0-9 _")

        return cleaned_data

    def __init__(self, *args, **kwargs):
        """Apply bootstrap form control to the remaining fields."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class AccountSettingsForm(UserChangeForm):

    """Define the fields that a user can edit to adjust their account
    settings.
    """

    username = forms.CharField(max_length=20,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username_input'}))

    class Meta:

        """Specify the fields to include in the register form."""

        model = CustomUserModel
        fields = ('username',)
        

class PasswordChangingForm(PasswordChangeForm):
    
    """Define the fields to include in the sign up form."""
    
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'type': 'password',
                                   'id': 'current_password_input'}))

    new_password1 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'type': 'password',
                                        'id': 'new_password1_input'}))

    new_password2 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'type': 'password',
                                        'id': 'new_password2_input'}))

    class Meta:
        model = CustomUserModel
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfilePageForm(forms.ModelForm):

    """Define the fields to incude in the profile page form."""

    family_name = forms.CharField(max_length=15,
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'style': 'border-color: #137ac483;',
                                  }))

    class Meta:
        model = FamilyProfile
        fields = ('family_name', 'family_bio', 'contact_info', 'profile_image')

        # Customize form field widgets
        widgets = {
            'family_bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'style': 'max-height: 200px; border-width: 1px; border-color: #137ac483; border-color: #137ac483;'
            }),
            'contact_info': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'style': 'max-height: 200px; border-width: 1px; border-color: #137ac483; border-color: #137ac483;'
            }),
        }


class FamilyMemberForm(forms.ModelForm):

    """Customize fields for form that allows each user to add a
    sub-profile for each family member they add to their family profile.
    """
    
    def __init__(self, *args, **kwargs):
        """Filter FamilyProfile objects to get the current user and assign
        to the user field queryset.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form as foreign key
        self.request = kwargs.pop('request')
        super(FamilyMemberForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = FamilyProfile.objects.filter(user=self.request.user)
        self.fields['user'].empty_label = None  # Remove empty label

    class Meta:
        model = FamilyMember
        fields = ('first_name', 'last_name', 'relation', 'age_range', 'about', 'user')

        # Customize widgets
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border-color: #137ac483;'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border-color: #137ac483;'
            }),
            'relation': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-color: #137ac483;'
            }),
            'age_range': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-color: #137ac483;'
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'style': 'max-height: 200px; border-width: 1px; border-color: #137ac483;'
            }),
            'user': forms.Select(attrs={
                'class': 'form-select',
                'style': 'max-height: 200px; width: fit-content; border-color: #137ac483;'
            }),
        }


class EditFamilyMemberForm(forms.ModelForm):

    """Customize fields for form that allows each user to add a
    sub-profile for each family member they add to their family profile.
    """
    
    def __init__(self, *args, **kwargs):
        """Filter FamilyProfile objects to get the current user and assign
        to the user field queryset.
        """
        # Credit: https://medium.com/analytics-vidhya/django-how-to-pass-the-user-object-into-form-classes-ee322f02948c
        # Learned to pass the request object to the form in order to request
        # the current user for saving to the form as foreign key
        self.request = kwargs.pop('request')
        super(EditFamilyMemberForm, self).__init__(*args, **kwargs)
        self.fields['user'].queryset = FamilyProfile.objects.filter(user=self.request.user)
        self.fields['user'].empty_label = None  # Remove empty label

    class Meta:
        model = FamilyMember
        fields = ('first_name', 'last_name', 'relation', 'age_range', 'about', 'user')

        # Customize widgets
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border-color: #137ac483;'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'style': 'border-color: #137ac483;'
            }),
            'relation': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-color: #137ac483;'
            }),
            'age_range': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-color: #137ac483;'
            }),
            'about': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '4',
                'style': 'max-height: 200px; border-width: 1px; border-color: #137ac483;'
            }),
            'user': forms.Select(attrs={
                'class': 'form-select',
                'style': 'max-height: 200px; width: fit-content; border-color: #137ac483;'
            }),
        }