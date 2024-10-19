from django import forms
from django.contrib.auth.models import User
from .models import Profile

class ChangeUsernameForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
        labels = {'username': 'Nuevo nombre de usuario'}

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['foto']
