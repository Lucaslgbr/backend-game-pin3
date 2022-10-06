from django.db import models
from backend.game.enums.room_status import RoomStatus


class Room(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    status = models.IntegerField(choices=RoomStatus.choices, default=RoomStatus)
    max_players = models.PositiveIntegerField()
    board = models.ForeignKey('Board', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    users = models.ManyToManyField('User', verbose_name="Jogadores", related_name='users', blank=True)

