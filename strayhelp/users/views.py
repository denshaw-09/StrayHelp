from dotenv import loadenv
loadenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from .models import post 
from ngo.models import rescue
from django.contrib.auth import login,logout
from django.core.files.storage import FileSystemStorage
import os

import google.generativeai as genai
from django.contrib import messages

model = genai.GenerativeModel("gemini-1.5-flash")

def is_animal_image(file_obj) -> bool:
    """Check if uploaded image contains an animal."""
    try:
        response = model.generate_content([
            "Does this image contain an animal? Answer only 'yes' or 'no'.",
            {"mime_type": file_obj.content_type, "data": file_obj.read()}
        ])
        return "yes" in response.text.strip().lower()
    except Exception as e:
        print("Error checking image:", e)
        return False

# Create your views here.
def home(request):
    posts = post.objects.all().exclude(is_rescue=True)
    return render(request,"home.html",{"posts":posts})


def posted_images(request):
    if request.user.is_authenticated:
       posts = post.objects.all().exclude(is_rescue=True)
       return render(request,"posts.html",{"posts":posts})
    else:
        return redirect('home')

def about(request):
    return render(request,"about.html",{})


def register(request):
    if request.method == "POST":
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = User(email=email,password=password,username=username)
        user.save()
        login(request,user)
        return redirect('posted_images')
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
        op = request.POST.get("oa")
        #gemini detection
        if not image:
           
            return redirect("upload_image")

       
        if not is_animal_image(image):
            
            return redirect("upload_image")

        
        image.seek(0)

        location = request.POST.get("location")
        fs = FileSystemStorage()
        uploaded_post = post(user=user,location=location,photo=image,operational_area=op)
        uploaded_post.save()
        
        return redirect('home')
    else:
        return render(request,'upload.html',{})
            
def profile_user(request):
    if request.user.is_authenticated:
          user = request.user
          r = rescue.objects.filter(ani_post__user=request.user)
          return render(request,"profile_user.html",{"r":r,"user":user})