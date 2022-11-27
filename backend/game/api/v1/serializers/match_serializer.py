from rest_framework import serializers

from backend.game.models import Match

class MatchSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Match
        fields='__all__'