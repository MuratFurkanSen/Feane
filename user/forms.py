from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from user.models import UserProfile
from django.forms.widgets import PasswordInput, TextInput, Textarea, EmailInput, FileInput


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {'username': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Username'}),
            'email': EmailInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'first_name': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your First Name'}),
            'last_name': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Last Name'})
        }

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Password'})
        self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control',
                                                               'placeholder': 'Password Again'})


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {'username': TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Username'}),
            'password': PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Your Password'})
        }
