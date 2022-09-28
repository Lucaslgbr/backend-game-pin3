from django.db import models


class Board(models.Model):
    lines = models.PositiveIntegerField()
    columns = models.PositiveIntegerField()
