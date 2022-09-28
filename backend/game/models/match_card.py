from django.db import models

from backend.game.enums.match_user_status import MatchUserStatus

class MatchCard(models.Model):
    match = models.ForeignKey('Match', on_delete=models.DO_NOTHING)
    card = models.ForeignKey('User', on_delete=models.DO_NOTHING)