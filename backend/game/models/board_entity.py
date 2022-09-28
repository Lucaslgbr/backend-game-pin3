from django.db import models

from backend.game.enums.board_entity_shapes import BoardEntityShapes


class BoardEntity(models.Model):
    match = models.ForeignKey('Match', on_delete=models.DO_NOTHING)
    position = models.ForeignKey('Position', on_delete=models.DO_NOTHING)
    board = models.ForeignKey('Board', on_delete=models.DO_NOTHING)
    shape = models.IntegerField(choices=BoardEntityShapes.choices, default=BoardEntityShapes.BALL)
