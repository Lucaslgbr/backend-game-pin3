from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
