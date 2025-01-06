from django.contrib import admin
from django.urls import path, include
from blogs import views

urlpatterns = [
    path("", views.start, name='start'),
    path('create_blog/', views.create_blog, name= "create_blog"),
    
]

