from django.db import models


class CardThrow(models.Model):
    card = models.ForeignKey('Card', on_delete=models.DO_NOTHING)
    throw = models.ForeignKey('Throw', on_delete=models.DO_NOTHING)
    sequence = models.PositiveIntegerField()
