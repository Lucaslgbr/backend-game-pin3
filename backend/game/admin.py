from django.contrib import admin

from backend.game.models import *

admin.site.register(BoardEntity)
admin.site.register(Board)
admin.site.register(Card)
admin.site.register(MatchCard)
admin.site.register(MatchUser)
admin.site.register(Match)
admin.site.register(Position)
admin.site.register(Room)
admin.site.register(CardThrow)
admin.site.register(Throw)
admin.site.register(User)
