from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('register/', views.register,name="register"),
    path('about/', views.about,name="about"),
    path('login_user/',views.login_user,name="login_user"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('upload/',views.upload_image,name="upload_image"),
    path('profile_user/',views.profile_user,name="profile_user")
]
