from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
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
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control',
    }), required=True)
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control',
        }),
        required=True,
    )


# class ProfileUpdateForm(forms.ModelForm):

#     # Additional fields from the Profile model
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'User name',
#         'class': 'form-control'
#         }), required=False)
    
#     first_name = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Firstname',
#         'class': 'form-control',
#     }), max_length=15, required=False)

#     last_name = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Lastname',
#         'class': 'form-control',
#     }), max_length=15, required=False)

#     email = forms.EmailField(widget=forms.EmailInput(attrs={
#             'placeholder': 'Email Address',
#             'class': 'form-control'
#         }), required=False)
    

#     address = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Address',
#         'class': 'form-control',
#     }), max_length=250, required=False)

#     phone = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Phone',
#         'class': 'form-control',
#     }), max_length=20, required=False)

#     country = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Country',
#         'class': 'form-control',
#     }), max_length=20, required=False)

#     class Meta:
#         model = User  # Use the User model
#         fields = ['username', 'first_name', 'last_name', 'email','address', 'phone', 'country']


# class ContactForm(forms.ModelForm):

#     name = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Enter your name',
#         'class': 'form-control'
#         }), required=True)
    
#     email = forms.EmailField(widget=forms.EmailInput(attrs={
#             'placeholder': 'Enter your email address',
#             'class': 'form-control'
#         }), required=True)
    
#     subject = forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Enter Subject',
#         'class': 'form-control'
#         }), required=True)
        
#     message = forms.CharField(widget=forms.Textarea(attrs={
#         'placeholder': 'Enter Message',
#         'class': 'form-control'
#         }), required=True)
            
    
#     class Meta:
#         model = Contact
#         fields = ('name', 'email',  'subject', 'message' )
