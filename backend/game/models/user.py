from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    birth_date = models.DateField()
    email = models.EmailField()
    date_joined = models.DateTimeField(blank=True, null=True, default=timezone.now)
    connections = models.IntegerField(default=0)
    current_room = models.ForeignKey('Room', null=True, blank=True, on_delete=models.DO_NOTHING)
