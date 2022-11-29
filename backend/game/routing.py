from backend.wsgi import *
from .consumers import RoomConsumer
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        [
            path('ws/room/<int:pk>/<int:user_id>/', RoomConsumer),
        ]
    ),
})
