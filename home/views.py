from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Signup
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import SignUpForm




# Create your views here.

# @login_required(login_url='/login/')  # Protect the index view


def index(request):
    # user_name = request.session.get('user_name', 'Guest') #{'user_name': user_name}
    return render(request, "index.html")

# def login(request):
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         try:
#             # Check if user exists in Signup table
#             user = Signup.objects.get(email=email, password=password)
            
#             request.session['user_id'] = user.id
#             request.session['user_name'] = user.name
            
#             # If user exists, redirect to index page
#             return redirect("index")
#         except Signup.DoesNotExist:
#             # If user does not exist, show an error message
#             messages.error(request, "Invalid email or password. Please try again.")
    
#     if request.session.get('user_id'):
#         return redirect("index")   
#     return render(request, "login.html")

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        department = request.POST.get("department")
        email = request.POST.get("email")
        password = request.POST.get("password")
        signup = Signup(name=name, department=department, email=email, password=password, date=datetime.today())
        signup.save()
        return redirect("index")
        # return redirect(reverse('index'))
        
    return render(request, "signup.html")

# def logoutUser(request):
#     request.session.flush()
#     return redirect("login")

def users_list(request):
    user_list = Signup.objects.all()
    return render(request, 'users_list.html', {'user_list' : user_list})

def user_info(request):
    user_info = Signup.objects.all()
    return render(request, 'user_info.html', {'user_info' : user_info})

def show_info(request, signup_id):
    show_info = Signup.objects.get(pk = signup_id)
    return render(request, 'show_info.html', {'show_info' : show_info})

def search_user(request) :
    if request.method == "POST" :
        searched = request.POST['searched']
        users = Signup.objects.filter(name__contains = searched )
        return render(request, "search_user.html", {'searched' : searched, 'users' : users})

    else :
        return render(request, 'search_user.html', {} )
    

def update_user(request, signup_id):
    user = Signup.objects.get(pk = signup_id)
    form = SignUpForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_info')

    return render(request, "update_user.html", 
                  {
                      'user' : user,
                      'form' :  form,
                  })


def delete_user(request, signup_id):
     user = Signup.objects.get(pk = signup_id)
     user.delete()
     return redirect('user-info')



