from django.db import models


class Position(models.Model):
    line = models.PositiveIntegerField()
    column = models.PositiveIntegerField()
