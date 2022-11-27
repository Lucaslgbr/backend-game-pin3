from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers.room_serializer import RoomSerializer
from backend.game.models import Room, User


class  RoomViewset(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class=RoomSerializer

    def update(self, request, *args, **kwargs):
        users = request.data.get('users')
        request.data.pop('users')
        response = super().update(request, *args, **kwargs)
        instance = self.get_object()
        for instance_user in instance.users.all():
            instance.users.remove(instance_user)
        for user in users:
            instance.users.add(User.objects.get(id=user))
        response.data['users'] = users
        return response
