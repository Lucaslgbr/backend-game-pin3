from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=255)
    lines = models.PositiveIntegerField()
    columns = models.PositiveIntegerField()
