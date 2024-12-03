from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class ProfileManager(BaseUserManager):
    def create_user(self,email,fn,ln,password=None):
        if not email:
            raise ValueError("Needed Email")
        normalized_Email=self.normalize_email(email)
        ProfileObject=self.model(email=normalized_Email,fst_name=fn,lst_name=ln)
        ProfileObject.set_password(password)
        ProfileObject.save()
        return ProfileObject
    

    def create_superuser(self,email,fst_name,lst_name,password):
        Normal_User_Object=self.create_user(email,fst_name,lst_name,password)
        Normal_User_Object.is_staff=True
        Normal_User_Object.is_superuser=True
        Normal_User_Object.save()

class Profile(AbstractBaseUser,PermissionsMixin):
    email=models.CharField(max_length=100,primary_key=True)
    fst_name=models.CharField(max_length=100)
    lst_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=ProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['fst_name','lst_name']