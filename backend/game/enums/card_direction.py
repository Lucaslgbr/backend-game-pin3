from django.db import models


class CardDirections(models.IntegerChoices):
    FORWARD = 1, 'FORWARD'
    LEFT = 2, 'LEFT'
    RIGHT = 3, 'RIGHT'
    BACKWARD = 4, 'BACKWARD'