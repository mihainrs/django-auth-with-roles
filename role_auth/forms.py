from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignupForm(UserCreationForm):
    dob = forms.DateField(required=False, label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'dob', 'password1', 'password2')
