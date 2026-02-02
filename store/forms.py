from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': 'Логин',
            'email': 'Email address',
            'password': 'Пароль',
        }
        help_texts = {
            'username': ('')
        }

class LoginForm(AuthenticationForm):
    pass

