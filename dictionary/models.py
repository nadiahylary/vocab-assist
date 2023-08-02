from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class SavedWord(models.Model):
    word = models.CharField(max_length=150, unique=True),
    user = models.ForeignKey(User, related_name='saved_words', on_delete=models.CASCADE)




