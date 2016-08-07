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
        fields = ['city', 'contact_number', 'country', 'postal_code', 'province', 'street']


class UserLoginForm(forms.Form):
    username = forms.CharField(min_length=3)
    password = forms.CharField(min_length=3, widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super(UserLoginForm, self).clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            cleaned_data['user'] = user
        else:
            raise forms.ValidationError(
                'Username and/or password is incorrect.')
        return cleaned_data