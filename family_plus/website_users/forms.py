from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):

    """Define the email and name variables to include as additional
    fields in the register form.
    """

    # Credit: https://youtu.be/TBGRYkzXiTg
    # Learned how to customize and connect additional form fields
    # for the register form from this video tutorial by John Elder,
    # owner and instructor of Codemy.com.
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
                             'class': 'form-control'}))

    first_name = forms.CharField(max_length=100,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control'}))

    last_name = forms.CharField(max_length=100,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control'}))

    class Meta:

        """Specify the fields to include in the register form."""

        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')
        
    def __init__(self, *args, **kwargs):
        """Apply bootstrap form control to the remaining fields."""
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
