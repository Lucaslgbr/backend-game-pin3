from django.db import models
#tabuleiro
class Board(models.Model):
    lines = models.PositiveIntegerField()
    columns = models.PositiveIntegerField()