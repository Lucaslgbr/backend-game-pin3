from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers.room_serializer import RoomSerializer
from backend.game.models import Room, User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from backend.game.enums.room_status import RoomStatus

class RoomViewset(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class=RoomSerializer

    @action(detail=True, methods=['put'])
    def add_user(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id =  self.request.data.get('user')
        user = User.objects.get(id=user_id)
        if not user.current_room:
            instance.users.add(user)
            user.current_room = instance
            user.save()
            return Response({'success':True}, status=status.HTTP_200_OK)
        else:
            if instance == user.current_room:
                return Response({'success':True}, status=status.HTTP_200_OK)
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

    
    @action(detail=True, methods=['put'])
    def remove_user(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id =  self.request.data.get('user')
        user = User.objects.get(id=user_id)
        instance.users.remove(user)
        user.current_room = None
        user.save()
        if instance.users.count() > 0:
            if user == instance.owner:
                instance.owner = instance.users.first()
        else:
            instance.active = False
            instance.status = RoomStatus.FINISHED
        instance.save()
        user.connections = 0
        user.save()
        channel_layer = get_channel_layer()
        room_name = str(instance.id)
        async_to_sync(channel_layer.group_send)(room_name, {"type": "send_message",
                                                            "user":user.id,
                                                            "event":"remove_player"})
        return Response({'success':True}, status=status.HTTP_200_OK)


    @action(detail=True, methods=['get'])
    def users(self, request, *args, **kwargs):
        instance = self.get_object()
        users = []
        for user in instance.users.all():
            users.append({
                'id': user.id,
                'name': user.get_full_name(),
                'status':'Online' if user.connections > 0 else 'Offline',
                })
        return Response({'users':users},status=status.HTTP_200_OK)

    def get_queryset(self):
        return super().get_queryset().filter(active=True)
        
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
