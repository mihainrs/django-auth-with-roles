from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(("email address"), unique=True)
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  #having email here means users can sign up with the email
    objects =CustomUserManager()
    
    class Meta:
        verbose_name = "custom user"
        verbose_name_plural= "custom users"