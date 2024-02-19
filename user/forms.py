from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import PasswordChangeForm

from .models import CustomUser


class RegistrationForm(UserCreationForm):

    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control',
            'autocomplete': 'off',
        }), required=True)
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        required=True,
        min_length=8 
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control',
            'autocomplete': 'off',
        }),
        required=True
    )
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error('password2', "Passwords do not match.")

        email = cleaned_data.get('email')
        email_validator = EmailValidator(message="Enter a valid email address.")

        if CustomUser.objects.filter(email=email).exists():
            self.add_error('email', 'An account with this email already exists. Please use a different email address.')
        
        try:
            email_validator(email)
        except forms.ValidationError as e:
            self.add_error('email', e)
    
    class Meta:
        model = CustomUser
        fields = ('email',  'password1', 'password2' )



class LoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'form-control',
        'id': 'login-email',
    }), required=True)
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
            'id': 'login-password',
        }),
        required=True,
    )



class PasswordChangeForm(PasswordChangeForm):
   
    def cleaned_data(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')

        if old_password and old_password == new_password1:
            raise forms.ValidationError("New password must be different from the old password.")

        return new_password1

    