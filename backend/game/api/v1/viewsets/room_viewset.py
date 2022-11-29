from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers.room_serializer import RoomSerializer
from backend.game.models import Room, User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class RoomViewset(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class=RoomSerializer

    @action(detail=True, methods=['put'])
    def add_user(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id =  self.request.data.get('user')
        user = User.objects.get(id=user_id)
        instance.users.add(user)
        return Response({'success':True}, status=status.HTTP_200_OK)

    
    @action(detail=True, methods=['put'])
    def remove_user(self, request, *args, **kwargs):
        instance = self.get_object()
        user_id =  self.request.data.get('user')
        user = User.objects.get(id=user_id)
        instance.users.remove(user)
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
