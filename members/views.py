from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm




def login_user(request):
    if request.method == "POST":
        username = request.POST ['username']
        password = request.POST ['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.success(request, "There was an error. Please try again with the correct credentials.")
            return redirect("login")
    
    return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return redirect("index")


def register_user(request):
    if request.method == "POST" :
        form = RegisterUserForm(request.POST)
        if form.is_valid() :
            user = form.save(commit=False)
            user.is_superuser = form.cleaned_data.get("is_superuser", False)
            user.is_staff = user.is_superuser  # Superusers must also be staff
            user.save()  # Save to DB
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            messages.success(request, "Registrtion successfull")
            return redirect("index")
        else :
            messages.error(request, "There was an error with your registration form. Please try again.")
        
    else:
        form = RegisterUserForm()   
    
    return render(request, 'authenticate/register_user.html', {
        'form' : form,
    })

# Create your views here.
