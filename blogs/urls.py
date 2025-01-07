from django.contrib import admin
from django.urls import path, include
from blogs import views

urlpatterns = [
    path("", views.start, name='start'),
    path('create_blog/', views.create_blog, name= "create_blog"),
    path('blogs_list/', views.blogs_list, name= "blogs_list"),
    path('blog_info/', views.blog_info, name= "blog_info"),
    path('show_blog/<int:blog_id>', views.show_blog, name="show_blog"),
    path('update_blog/<blog_id>', views.update_blog, name="update_blog"),
    path('delete_blog/<blog_id>', views.delete_blog, name="delete_blog"),
    path('search_blog/', views.search_blog, name="search_blog"),
]


