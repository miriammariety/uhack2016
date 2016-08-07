from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Person

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email', 'username', 'password1', 'password2']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['city', 'contact_number', 'country', 'gender', 'postal_code', 'province', 'street']