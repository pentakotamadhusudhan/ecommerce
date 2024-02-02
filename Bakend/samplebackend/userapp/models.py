from django.db import models
from django.contrib.auth.models import User,AbstractBaseUser,AbstractUser
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

class CustomUser(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    mobile = models.CharField(max_length=12)
    address = models.TextField()
    
    USERNAME_FIELD = 'email'

    
    
# myapp/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUserrr(AbstractUser):
    mobile = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length = 10)

    # def create_superuser(self,password=None, **kwargs):

    #     user  = User()
    #     user.username =self.username
    #     print(password)
    #     user.first_name =self.first_name
    #     user.last_name =self.last_name
    #     user.password =user.set_password(password)
    #     print(user.password)
    #     user.email =self.email
    #     user.mobile =self.mobile
    #     user.address =self.address
    #     user.gender =self.gender
    #     user.save()


    #     return user



    # def  create_superuser(self,validated_data):
    #         user = CustomUserrr.objects.create_superuser(first_name=validated_data['first_name'],
    #                                                 last_name = validated_data['last_name'],
    #                                                 username = validated_data['username'],
    #                                                 password = make_password(validated_data['password']),
    #                                                 email = validated_data['email'],
    #                                                 is_active = validated_data['is_active'],
    #                                                 is_staff = validated_data['is_staff'],
    #                                                 mobile = validated_data['mobile'],
    #                                                 address = validated_data['address'],
    #                                                 gender = validated_data['gender'],
                                                    
    #                                                 )
            

    #         user.save()

    #         return
        

        
