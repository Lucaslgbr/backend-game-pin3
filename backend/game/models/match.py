from django.db import models

from backend.game.enums.match_status import MatchStatus


class Match(models.Model):
    room = models.ForeignKey('Room', on_delete=models.DO_NOTHING)
    winner = models.ForeignKey('User', null=True, blank=True, on_delete=models.DO_NOTHING)
    duration = models.IntegerField(null=True)    
    status = models.IntegerField(choices=MatchStatus.choices, default=MatchStatus.WAITING_FOR_PLAYERS, verbose_name='Status')

    def finish(self):
        self.status = MatchStatus.FINISHED
        self.save()