from django import forms
from django.forms import ModelForm
from .models import Signup


class SignUpForm(ModelForm):
    class Meta: 
        model = Signup
        fields = ('name', 'department','email', 'password', 'date')
        labels = {
            'name' : '',
            'department' : '',
            'email' : '',
            'password' : '',
            'date' : '',
        }
