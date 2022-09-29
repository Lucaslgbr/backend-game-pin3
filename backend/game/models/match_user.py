from django.db import models
from backend.game.enums.match_user_status import MatchUserStatus


class MatchUser(models.Model):
    position = models.ForeignKey('Position', on_delete=models.DO_NOTHING)
    match = models.ForeignKey('Match', on_delete=models.DO_NOTHING)
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    status = models.IntegerField(choices=MatchUserStatus.choices, default=MatchUserStatus.ONLINE, verbose_name='Status')
    throws = models.ManyToManyField('Throw', verbose_name="Jogadas", related_name='throws', blank=True)
    available_cards = models.ManyToManyField('MatchCard', verbose_name="Cartas disponíveis",
                                             related_name='available_cards', blank=True)
