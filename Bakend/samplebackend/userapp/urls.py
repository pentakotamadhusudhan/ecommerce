from django.urls import path
from rest_framework.authtoken import views
from .views import *


urlpatterns = [
    path("",UserView.as_view()),
    path("login",Login.as_view()),
     path('getbyid/<int:id>', UserGetById.as_view())   
]