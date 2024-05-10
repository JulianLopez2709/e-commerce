from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager
)

class CostomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Debes tener un correo electronico")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        return self._create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser,PermissionsMixin):
    email= models.CharField(max_length=100,unique=True)
    name= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    avatar=models.ImageField(default="avatar.png")
    date_joined=models.DateField(default=timezone.now)
    is_staff= models.BooleanField(default=False)
    objects = CostomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS=[]
    
    class Meta():
        ordering=["-date_joined"]

