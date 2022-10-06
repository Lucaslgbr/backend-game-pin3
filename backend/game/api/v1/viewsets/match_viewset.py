from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers.match_serializer import MatchSerializer
from backend.game.models import Match


class  MatchViewset(ModelViewSet):
    queryset = Match.objects.all()
    serializer_class=MatchSerializer
