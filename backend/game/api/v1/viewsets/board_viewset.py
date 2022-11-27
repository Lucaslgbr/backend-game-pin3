from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers import BoardSerializer
from backend.game.models import Board


class BoardViewset(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class=BoardSerializer
