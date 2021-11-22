from django import forms
from django.db.models.base import Model
from django.forms import Form
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    userName = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class': 'form-control mb-4 p-2',
                                                                            'placeholder': 'Username'}))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(
        attrs={'class': 'form-control p-2 mb-4', 'placeholder': 'Password'}))


class SingUpForm(forms.Form):
    userName = forms.CharField(max_length=40, widget=forms.TextInput(attrs={

        'class': 'form-control shadow-none no-border',
        'placeholder': 'Your Name',
        'id': 'userNameInput',

    }))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={

        'class': 'form-control no-border shadow-none',
        'placeholder': 'Password',
        'id': 'password',

    }))

    re_password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={

        'class': 'form-control no-border shadow-none',
        'placeholder': 'Repeat your password',
        'id': 're-password',

    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={

        'class': 'form-control no-border shadow-none',
        'placeholder': 'Your Email',
        'id': 'emailInput',

    }))
