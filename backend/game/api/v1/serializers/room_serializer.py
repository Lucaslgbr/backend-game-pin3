from rest_framework import serializers

from backend.game.models import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'