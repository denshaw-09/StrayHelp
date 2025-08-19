from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from .models import post 
from ngo.models import rescue
from django.contrib.auth import login,logout
from django.core.files.storage import FileSystemStorage
import os
# Create your views here.
def home(request):
    posts = post.objects.all().exclude(is_rescue=True)
    return render(request,"home.html",{"posts":posts})
def register(request):
    if request.method == "POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User(email=email,password=password,username=username)
        user.save()
        login(request,user)
        return redirect('home')
    else:
        return render(request,"register.html",{})
    

def login_user(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username=username)
        if user:
           login(request,user)
           return redirect('home')
        
    return render(request,'login.html',{})

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')

def upload_image(request):
    if request.method == "POST":
        user = request.user
        image = request.FILES.get('image')
        location = request.POST.get("location")
        fs = FileSystemStorage()
        uploaded_post = post(user=user,location=location,photo=image)
        uploaded_post.save()
        
        return redirect('home')
    else:
        return render(request,'upload.html',{})
            
def profile_user(request):
    if request.user.is_authenticated:
          user = request.user
          r = rescue.objects.filter(ani_post__user=request.user)
          return render(request,"profile_user.html",{"r":r,"user":user})