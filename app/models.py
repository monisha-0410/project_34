from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
class UserProfileManager(BaseUserManager):
    def create_user(self,email,firstname,lastname,password=None):
        if not email:
            raise ValueError("please enter email")
        ne=self.normalize_email(email)
        user=self.model(email=ne,firstname=firstname,lastname=lastname)

        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,firstname,lastname,password):
        user=self.create_user(email,firstname,lastname,password)
        user.is_superuser=True
        user.is_staff=True
        user.save()

class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100,default='saravanan')
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['firstname','lastname']
