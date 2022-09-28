from django.db import models


class MatchCard(models.Model):
    match = models.ForeignKey('Match', on_delete=models.DO_NOTHING)
    card = models.ForeignKey('Card', on_delete=models.DO_NOTHING)
