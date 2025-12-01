from django import forms
from .models import Link

class LinkForm(forms.ModelForm): #Form to add or edit links
    class Meta: 
        model = Link  #The form is based on the Link model
        fields = ['title', 'url', 'description', 'tags'] #Fields to be included in the form
        

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):  #Form for user signup
    class Meta:
        model = User  #The form is based on the User model
        fields = ['username', 'password1', 'password2']  #Fields to be included in the signup form

