from rest_framework.viewsets import ModelViewSet
from backend.game.api.v1.serializers.user_serializer import UserSerializer
from backend.game.models import User


class UserViewset(ModelViewSet):
    queryset = User.objects.all()
    serializer_class=UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = response.data.serializer.instance
        user.set_password(request.data['password'])
        user.save()
        return response