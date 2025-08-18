from django.shortcuts import render,redirect 
from django.contrib.auth.models import User
from .models import post 
from ngo.models import rescue
from django.contrib import messages
import google.generativeai as genai
from django.contrib.auth import login,logout
from django.core.files.storage import FileSystemStorage
import os
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")  # or gemini-1.5-pro for better accuracy
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
    
def about(request):
    return render(request,"about.html",{})

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
        op=request.POST.get("op")
        if not image:
            messages.error(request, "Please upload an image.")
            return redirect("upload_post")

        # Check with Gemini
        if not is_animal_image(image):
            messages.error(request, "Please upload a valid animal image.")
            return redirect("upload_image")

        
        image.seek(0)


        uploaded_post = post(user=user,location=location,photo=image,operational_area=op)
        uploaded_post.save()
        messages.success(request, "Animal post uploaded successfully!")
        return redirect('home')
    else:
        return render(request,'upload.html',{})
            
def profile_user(request):
    if request.user.is_authenticated:
          user = request.user
          r = rescue.objects.filter(ani_post__user=request.user)
          return render(request,"profile_user.html",{"r":r,"user":user})