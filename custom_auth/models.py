from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
