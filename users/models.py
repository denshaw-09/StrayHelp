from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/",null=True)
    location = models.TextField(max_length=500,blank=True,null=True,default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_rescue = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.user.username}'