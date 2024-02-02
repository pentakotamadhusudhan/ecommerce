from django.urls import path

from .views import *

urlpatterns =[
    path('testapp/',Testpost.as_view()),
    path('SecondTestpost/',SecondTestpost.as_view()),

]