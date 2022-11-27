from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers import MatchUserSerializer
from backend.game.models import MatchUser


class  MatchUserViewset(ModelViewSet):
    queryset = MatchUser.objects.all()
    serializer_class=MatchUserSerializer
