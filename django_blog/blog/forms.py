from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Registration form that also asks for email
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# Simple form to edit basic profile fields (username & email)
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email")
