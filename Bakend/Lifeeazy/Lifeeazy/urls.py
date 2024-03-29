"""Lifeeazy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
from django.conf.urls import *
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
from rest_framework.schemas import get_schema_view, openapi
from django.views.generic import TemplateView
# from rest_framework_simplejwt import views as jwt_views

from rest_framework import permissions

# from revproxy.views import ProxyView


# schema_view = get_schema_view(
#    openapi.Info(
#       title="LifeEazy",
#       default_version='v1',
#       name='openapi-schema',
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )
urlpatterns = [
    path('admin/', admin.site.urls),

    path('User/', include('user.urls')),
    path('HCP/', include('hcpapi.urls')),
    path('UserAppointment/', include("userappointment.urls")),
    path('HcpAppointment/', include('hcpappointment.urls')),
    path('HcpPrescription/', include('hcpprescription.urls')),
    path('Partner/', include('partners.urls')),
    path('ImageUpload/', include('profileimage.urls')),
    path('testapp/', include('testapp.urls')),
    path('LifeEazy/', get_schema_view(
        title="LifeEazyApi",
    ), name='openapi-schema'),
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),

    # path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
