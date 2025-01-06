from django.shortcuts import render, redirect
from datetime import datetime
from blogs.models import Blog
from blogs.forms import BlogForm

# Create your views here.


def start(request):
    return render(request, 'index.html')


def create_blog(request):
    submitted = False
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("start")
        else :
            form = BlogForm()
        # return redirect(reverse('index'))
        
    return render(request, "create_blog.html", {form : form})
