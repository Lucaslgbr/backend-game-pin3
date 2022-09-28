from django.db import models

from backend.game.enums.card_direction import CardDirections

class Card(models.Model):
    direction = models.IntegerField(choices=CardDirections.choices, default=CardDirections.FORWARD, verbose_name='Direção')
    lines = models.PositiveIntegerField()
    moves_amount = models.PositiveIntegerField()