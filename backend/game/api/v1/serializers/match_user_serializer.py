from rest_framework import serializers

from backend.game.models import MatchUser

class MatchUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=MatchUser
        fields='__all__'