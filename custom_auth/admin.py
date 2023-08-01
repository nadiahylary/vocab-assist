from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from custom_auth.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)

