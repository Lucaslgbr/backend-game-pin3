from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers.user_serializer import RoomSerializer
from backend.game.models import Room


class  RoomViewset(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class=RoomSerializer
