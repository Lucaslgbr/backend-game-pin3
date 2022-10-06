from rest_framework import serializers

from backend.game.models import Board

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields='__all__'