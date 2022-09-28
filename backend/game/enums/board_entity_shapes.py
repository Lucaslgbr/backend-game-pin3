from django.db import models


class BoardEntityShapes(models.IntegerChoices):
    BALL = 1, 'BALL'
    TRIANGLE = 2, 'TRIANGLE'
    SQUARE = 3, 'SQUARE'