from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from backend.game.api.v1.serializers.user_serializer import UserSerializer
from rest_framework.response import Response


class CustomObtainAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        response = {
            'token': token.key,
            **UserSerializer(user).data
        }
        return Response(response)


def index(request):
    return render(request, "chat/index.html")

def room(request, room_name, user_id):
    return render(request, "chat/room.html", {"room_name": room_name, "user_id":user_id})