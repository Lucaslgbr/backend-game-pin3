from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers.user_serializer import UserSerializer
from backend.game.models import User
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data.serializer.instance
        user.set_password(request.data['password'])
        user.save()
        return response

    
    @action(detail=True, methods=['get'])
    def get_room(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({'room':instance.current_room.id if instance.current_room else None}, status=status.HTTP_200_OK)

    