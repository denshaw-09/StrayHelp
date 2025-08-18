from django.shortcuts import render,redirect,get_object_or_404
from . models import Ngo,rescue
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from users.models import post
# Create your views here.

def ngo_home(request):
    ngo = Ngo.objects.get(user=request.user)
    ani_post = post.objects.filter(operational_area__icontains=ngo.operational_area).exclude(is_rescue=True)
    return render(request,'ngo_home.html',{'animal_post':ani_post})

def register_ngo(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User(username=username,password=password,email=email)
        user.save()
        logo = request.FILES.get("logo")
        registration_number = request.POST.get("registration_number")
        year = request.POST.get("year")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        operational_area = request.POST.get("oa")
        ngo_user = Ngo(user=user,logo=logo,registration_number=registration_number,year=year,address=address,phone=phone,operational_area=operational_area)
        ngo_user.save()
        login(request,ngo_user)
        return redirect('ngo_home')
    else:
        return render(request,"register_ngo.html",{})
    
def login_ngo(request):
  
    if request.method == "POST":
        username=request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.get(username=username)
        if user:
           login(request,user)
           return redirect('ngo_home')
        
    return render(request,'ngo_login.html',{})

def logout_ngo(request):
   if request.user.is_authenticated:
        logout(request)
        return redirect('login_ngo')
    
def ngo_profile(request):
    if request.user.is_authenticated:
        
        ngo_profile = Ngo.objects.get(user=request.user)
        return render(request,'ngo_profile.html',{'ngo':ngo_profile})

def detailed_view(request,id):
    posts = post.objects.get(id=id)
    return render(request,"detailed_view.html",{'posts':posts})

def rescue_animal(request,key):
    ani_post = get_object_or_404(post,id=key)
    ani_post.is_rescue =True
    ani_post.save()

    rescue.objects.create(ngo=request.user,ani_post=ani_post,status="Rescued")
    return redirect('ngo_home')

def dashboard(request):
    rescues = rescue.objects.filter(ngo=request.user)
    for r in rescues:
        print(r.ani_post.user.username)
        print(r.ani_post.photo.url)
    return render(request, 'dashboard.html', {'rescues': rescues})