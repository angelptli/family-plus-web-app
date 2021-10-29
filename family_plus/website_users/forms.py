from custom_user_model.models import CustomUserModel
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import FamilyProfile
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
                             'placeholder': 'email@example.com'}))

    is_adult = forms.BooleanField(label="I confirm that I am 18 years old or over")
    
    class Meta:

        """Specify the fields to include in the register form."""

        model = CustomUserModel
        fields = ('email', 'username', 'password1', 'password2',
                  'family_relation_status', 'is_adult')
    
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

    username = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control'}))

    class Meta:

        """Specify the fields to include in the register form."""

        model = CustomUserModel
        fields = ('username', 'password')
        

class PasswordChangingForm(PasswordChangeForm):
    
    """Define the fields to include in the sign up form."""
    
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
                                   'class': 'form-control',
                                   'type': 'password'}))

    new_password1 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'type': 'password'}))

    new_password2 = forms.CharField(max_length=100,
                                    widget=forms.PasswordInput(attrs={
                                        'class': 'form-control',
                                        'type': 'password'}))

    class Meta:
        model = CustomUserModel
        fields = ('old_password', 'new_password1', 'new_password2')


class ProfilePageForm(forms.ModelForm):

    """Define the fields to incude in the profile page form."""

    family_name = forms.CharField(max_length=15,
                                  widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'placeholder': 'What is a nickname for your family?'}))

    class Meta:
        model = FamilyProfile
        fields = ('family_name', 'family_bio', 'contact_info', 'hobbies',
                  'interests', 'locations', 'schedule', 'languages',
                  'family_members', 'profile_image')

        # Apply bootstrap styling (form-control) to the text boxes of
        # these fields
        widgets = {
            'family_name': forms.TextInput(attrs={'class': 'form-control'}),
            'family_bio': forms.Textarea(attrs={'class': 'form-control'}),
            'contact_info': forms.Textarea(attrs={'class': 'form-control'}),
            'hobbies': forms.Textarea(attrs={'class': 'form-control'}),
            'interests': forms.Textarea(attrs={'class': 'form-control'}),
            'locations': forms.Textarea(attrs={'class': 'form-control'}),
            'schedule': forms.Textarea(attrs={'class': 'form-control'}),
            'languages': forms.Textarea(attrs={'class': 'form-control'}),
            'family_members': forms.Textarea(attrs={'class': 'form-control'}),
            # 'profile_image': forms.ImageField(attrs={'class': 'form-control'}),
        }
