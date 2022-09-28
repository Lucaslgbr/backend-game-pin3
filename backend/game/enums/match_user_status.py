from django.db import models


class MatchUserStatus(models.IntegerChoices):
    ONLINE = 1, 'ONLINE'
    OFFLINE = 2, 'OFFLINE'