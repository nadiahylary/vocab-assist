from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Word(models.Model):
    name = models.CharField(max_length=150, unique=True),
    meaning = models.CharField(max_length=250),


