from django.db import models
from user.models import CustomUser

# Create your models here.

class Jwt(models.Model):
    user = models.ForeignKey(
        CustomUser,on_delete = models.CASCADE, related_name='login_user')
    access = models.TextField()
    refresh = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

