from custom_user_model.models import CustomUserModel
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import FamilyProfile

class RegisterForm(UserCreationForm):

    """Define the email and name variables to include as additional
    fields in the register form.
    """

    # Credit: https://youtu.be/TBGRYkzXiTg
    # Learned how to customize and connect additional form fields
    # for the register form from this video tutorial by John Elder,
    # owner and instructor of Codemy.com.
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control',
                             'placeholder': 'email@example.com'}))

    class Meta:

        """Specify the fields to include in the register form."""

        model = CustomUserModel
        fields = ('email', 'username', 'password1', 'password2')
        
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

    family_name = forms.CharField(max_length=30,
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
