from django.db import models
from backend.game.models.card_throw import CardThrow


class Throw(models.Model):
    cards = models.ManyToManyField('Card', through=CardThrow, blank=True)
