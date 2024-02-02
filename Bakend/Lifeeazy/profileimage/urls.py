from django.urls import path
from .views import ImageUpload
urlpatterns=[
    path('PostImages/',ImageUpload.as_view())
]