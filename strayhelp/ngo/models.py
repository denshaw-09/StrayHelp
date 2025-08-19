from django.db import models
from django.contrib.auth.models import User 
from users.models import post 
# Create your models here.
class Ngo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=100,blank=True,null=True)
    year = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    operational_area = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="ngo_logo/",blank=True,null=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.user.username 

class rescue(models.Model):
    ngo = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ngo_rescues')
    ani_post = models.ForeignKey(post,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default="In Progress")
    created_at = models.DateTimeField(auto_now_add=True)
    
from django.db import models
from django.contrib.auth.models import User 
from users.models import post 
# Create your models here.
class Ngo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=100,blank=True,null=True)
    year = models.IntegerField(blank=True,null=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    operational_area = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="ngo_logo/",blank=True,null=True)

    def __str__(self):
        return self.user.username 

class rescue(models.Model):
    ngo = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ngo_rescues')
    ani_post = models.ForeignKey(post,on_delete=models.CASCADE)
    status = models.CharField(max_length=50,default="In Progress")
    created_at = models.DateTimeField(auto_now_add=True)
    