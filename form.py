from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User


class Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1' , 'password2')

        widgets = {
            'username' : forms.TextInput(attrs={
                'placeholder': 'Enter Username'
            }),
            'email' : forms.EmailInput(attrs={
                'placeholder': 'Email Address'
            }),
            'password1' : forms.PasswordInput(attrs={
                'placeholder': 'Password'
            }),
            'password2' : forms.PasswordInput(attrs={
                'placeholder': 'Repeat Password'
            }),
        }
