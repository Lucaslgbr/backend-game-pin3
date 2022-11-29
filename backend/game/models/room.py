from django.db import models
from backend.game.enums.room_status import RoomStatus
from backend.game.models.user import User
from asgiref.sync import sync_to_async
class Room(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(choices=RoomStatus.choices, default=RoomStatus.WAITING_FOR_PLAYERS)
    max_players = models.PositiveIntegerField()
    board = models.ForeignKey('Board', on_delete=models.DO_NOTHING)
    owner = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    users = models.ManyToManyField('User', verbose_name="Jogadores", related_name='users', blank=True)
    active = models.BooleanField(default=True)

    @sync_to_async
    def finish(self):
        self.status = RoomStatus.FINISHED
        self.save()