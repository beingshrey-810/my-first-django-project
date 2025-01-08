from django import forms
from django.forms import ModelForm
from .models import Blog


class BlogForm(ModelForm):
    class Meta: 
        model = Blog
        fields = ('title', 'description', 'date', 'author', 'blog_image')
        labels = {
            'title' : 'Blog Title',
            'description' : 'Description',
            'date' : 'Date',
            'author' : 'Written By',
            'blog_image' : 'Uplaod Image',
            
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 50}), 
        }