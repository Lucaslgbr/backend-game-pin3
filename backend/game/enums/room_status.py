from django.db import models


class RoomStatus(models.IntegerChoices):
    WAITING_FOR_PLAYERS = 1, 'WAITING_FOR_PLAYERS'
    IN_PROGRESS = 2, 'IN_PROGRESS'
    FINISHED = 3, 'FINISHED'