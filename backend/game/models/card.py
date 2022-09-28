from django.db import models

from backend.game.enums.card_direction import CardDirections

class Card(models.Model):
    direction = models.IntegerField(choices=CardDirections.choices, default=CardDirections.FORWARD)
    lines = models.PositiveIntegerField()
    moves_amount = models.PositiveIntegerField(default=1)