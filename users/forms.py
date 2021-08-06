from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Inform a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False,
                                 help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False,
                                help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Inform a valid email address')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image')
