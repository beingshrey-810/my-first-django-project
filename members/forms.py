from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm



class RegisterUserForm(UserCreationForm):
    is_superuser = forms.BooleanField(required=False, label="Register as Superuser")
    email = forms.EmailField(widget = forms.EmailInput(attrs= {'class' : 'form-control', }))
    first_name = forms.CharField(max_length=50 , widget = forms.TextInput(attrs= {'class' : 'form-control', 'style': 'width: 100%;'}))
    last_name = forms.CharField(max_length=50 , widget = forms.TextInput(attrs= {'class' : 'form-control'}))
    
    
    
    class Meta :
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', "is_superuser")
    
    
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    
