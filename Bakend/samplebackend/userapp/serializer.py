from rest_framework import serializers
from django.contrib.auth.models import User
from .models import CustomUser,CustomUserrr
from django.contrib.auth.hashers import make_password

class Userserilaizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
    

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomUserrr
        fields = "username","password"


# myapp/serializers.py
from rest_framework import serializers
from .models import CustomUserrr

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserrr
        fields = "first_name",'last_name','username','password','email','is_active','is_staff','mobile','address','gender'
        # fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}, }

    def  create(self,validated_data):
            user = CustomUserrr.objects.create(first_name=validated_data['first_name'],
                                                    last_name = validated_data['last_name'],
                                                    username = validated_data['username'],
                                                    password = make_password(validated_data['password']),
                                                    email = validated_data['email'],
                                                    is_active = validated_data['is_active'],
                                                    is_staff = validated_data['is_staff'],
                                                    mobile = validated_data['mobile'],
                                                    address = validated_data['address'],
                                                    gender = validated_data['gender'],
                                                    
                                                    )
            print('------------',make_password(validated_data['password']))
            
            

            user.save()

            return user



# class CustomUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUserrr
#         fields = ["first_name", 'last_name', 'username', 'password', 'email', 'is_active', 'is_staff', 'mobile', 'address', 'gender']

#     def create(self, validated_data):
#         user = CustomUserrr.objects.create(
#             first_name=validated_data['first_name'],
#             last_name=validated_data['last_name'],
#             username=validated_data['username'],
#             password=make_password(validated_data['password']),
#             email=validated_data['email'],
#             is_active=validated_data['is_active'],
#             is_staff=validated_data['is_staff'],
#             mobile=validated_data['mobile'],
#             address=validated_data['address'],
#             gender=validated_data['gender']
#         )

#         user.save()

#         return user

