from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create Custom User  Manager
class CustomUserManager(BaseUserManager):

    # Override _create_user  
    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("Email field required")

        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    # Override create_superuser
    def create_superuser(self,email,password,**extra_fields):
        # Set all boolean is true
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('name',"admin")

        # If the any mismatch raise Error 
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff = True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser = True")
        if extra_fields.get("is_active") is not True:
            raise ValueError("Superuser must have is_active = True")
        

        return self._create_user(email, password, **extra_fields)


# Create Custom User model 
class CustomUser(AbstractBaseUser,PermissionsMixin):
    # initalize necessary fields
    email = models.EmailField(unique = True)
    name = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)

    USERNAME_FIELD = "email"  # Set email  as username
    objects = CustomUserManager() # use CustomUserManager as object

    def __str__(self):
        return self.email

