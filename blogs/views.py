from django.shortcuts import render, redirect
from datetime import datetime
from blogs.models import Blog
from blogs.forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def start(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs': blogs})

@login_required
def create_blog(request):
    if not request.user.is_authenticated:
        messages.error(request, "You need to log in to create a blog.")
        return render(request, 'blogs/create_blog.html')  # Render the same page with the error message
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


def blogs_list(request):
    blog_list = Blog.objects.all()
    return render(request, 'blogs_list.html', {'blog_list' : blog_list})



def show_blog(request, blog_id):
    show_blog = Blog.objects.get(pk = blog_id)
    return render(request, 'show_blog.html', {'show_blog' : show_blog})



def blog_info(request):
    blog_info = Blog.objects.all()
    return render(request, 'blog_info.html', {'blog_info' : blog_info})


@login_required
def update_blog(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('blog_info')

    return render(request, "update_blog.html", 
                  {
                      'blog' : blog,
                      'form' :  form,
                  })


def delete_blog(request, blog_id):
     blog = Blog.objects.get(pk = blog_id)
     blog.delete()
     return redirect('blog-info')


def search_blog(request) :
    if request.method == "POST" :
        searched = request.POST['searched']
        blogs = Blog.objects.filter(title__contains = searched )
        return render(request, "search_blog.html", {'searched' : searched, 'blogs' : blogs})

    else :
        return render(request, 'search_user.html', {} )