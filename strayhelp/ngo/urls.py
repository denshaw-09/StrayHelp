from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
   path("register_ngo/",views.register_ngo,name="register_ngo"),
   path('login_ngo/',views.login_ngo,name="login_ngo"),
   path("logout_ngo/",views.logout_ngo,name="logout_ngo"),
   path('ngo_profile/',views.ngo_profile,name="ngo_profile"),
   path('ngo_home/',views.ngo_home,name="ngo_home"),
   path('rescue_animal/<int:key>/',views.rescue_animal,name="rescue_animal"),
   path('dashboard/',views.dashboard,name="dashboard")
]
