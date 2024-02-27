from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ProfileModel


class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in  ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]
    
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in  ['username',]:
            self.fields[fieldname].help_text = None


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'lastname'}))
    image = forms.ImageField(label="Profile Picture")
    profile_bio = forms.CharField(label='Profile Bio', widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Profile Bio', 'rows': 4,}))
    website_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website Link'}))
    medium_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meduim Link'}))
    reddit_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reddit Link'}))
    quora_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Quora Link'}))
    pinterest_link = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Pinterest Link'}))
    
    class Meta:
        model = ProfileModel
        fields = ['first_name', 'last_name', 'image', 'profile_bio', 'website_link', 'medium_link', 'reddit_link', 'quora_link', 'pinterest_link',]
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

        for fieldname in  ['image', 'profile_bio', 'website_link', 'medium_link', 'reddit_link', 'quora_link', 'pinterest_link',]:
            self.fields[fieldname].required = False
