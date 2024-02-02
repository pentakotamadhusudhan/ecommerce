from .models import * 
from rest_framework import generics,status,response
from .serializer import *
from django.contrib.auth import authenticate,login
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework_simplejwt.views import TokenObtainPairView

response = response.Response

class UserView (generics.ListCreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUserrr.objects.all()
    # permission_classes= (IsAuthenticated,)
    # filter_backends = [OrderingFilter]
    # ordering_fields = ['username', 'email']
    # ordering = ['username']

    def post(self, request):
        try:
            ser = CustomUserSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                return response({
                    "status": 200,
                    "result" : ser.data,
                })
            else:
                 return response({
                "status": 404,
                "result" : "Something went wrong",
            })
        except Exception as e:
            return response({
                "status": 500,
                "result" : "User Name or email is already used ",
            })
    

class Login(generics.GenericAPIView):
    serializer_class  = LoginSerializer
   

    def post(self,request):
        try:
            username = request.data.get("username")
            password = request.data.get("password")
            print(username,password)
            userdetails = CustomUserrr.objects.get(username = username)
            user = authenticate(request,username=username,password=password)
            if user:
                # token = RefreshToken()
                login(request=request,user=user)
                # toke = Token.objects.create(user=userdetails)
                # print("-----------------",toke)
                
                return response({
                                "status":status.HTTP_200_OK,
                                'result' : CustomUserSerializer(user,context= {'request': request}).data,
                                "hasherror": True,
                                
                            })
            else:
                return response({
                                "status":status.HTTP_404_NOT_FOUND,
                                'result' : [],
                                "hasherror": True
                            })
        except Exception as e:
                return response({
                                "status":status.HTTP_500_INTERNAL_SERVER_ERROR,
                                'result' : [],
                                "hasherror": True
                            })


class UserGetById(generics.RetrieveAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUserrr.objects.all()
    lookup_field = 'id'
  
    