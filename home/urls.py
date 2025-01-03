from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    # path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    # path('logout/', views.logoutUser, name='logout'),
    path('users_list/', views.users_list, name= "users_list"),
    path('user_info/', views.user_info, name= "user_info"),
    path('show_info/<signup_id>', views.show_info, name="show_info"),
    path('search_user/', views.search_user, name="search_user"),
]