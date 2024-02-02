from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserrr


# class CustomInline(admin.StackedInline):
#     model = CustomUser
#     can_delete = False
#     verbose_name = "CustomUser"

# class CustomerUerAdmin(UserAdmin):
#     inlines = (CustomInline, )

# admin.site.unregister(User)
# admin.site.register(User,CustomerUerAdmin)
admin.site.register(CustomUserrr)