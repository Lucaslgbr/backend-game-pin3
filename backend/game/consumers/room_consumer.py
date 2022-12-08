import datetime
import json
from django.db.models import F
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
from backend.game.models import Room, Match, User
from channels.db import database_sync_to_async


class RoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # utiliza o pk enviado na url como nome da sala
        self.room_group_name = str(self.scope['url_route']['kwargs'].get('pk', None))
        # pega o user_id da url
        self.user = self.scope['url_route']['kwargs'].get('user_id', None)
        # aumenta em 1 o número de connections do usuário
        user_connections = await self.update_user_incr(self.user)
        # enviar apenas se as connections do usuario forem maior que 0, ou seja, se o usuário estiver online
        if user_connections > 0:
            # envia para todos da mesma sala a mensagem 
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'user': self.user,
                "event": "new_player"
            })

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # pega o user_id da url
        self.user = self.scope['url_route']['kwargs'].get('user_id', None)
        user_connections = await self.update_user_decr(self.user)
        # se a quantidade de connections do usuário for igual a 0, 
        # todos do grupo irão receber uma mensagem avisando que o player foi desconectado e está offline
        if user_connections == 0:
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'user': self.user,
                "event": "disconnected_player"
            })
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        Get the event and send the appropriate event
        """
        response = json.loads(text_data)
        event = response.get("event", None)
        message = response.get("message", None)
        if event == 'finish_room':
            try:
                room = await Room.objects.aget(id=self.room_group_name)
                await room.finish()
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'send_message',
                    'message': message,
                    "event": event
                })
            except Exception as e:
                print(e)
        if event == 'finish_match':
            match_id = response.get('match', None)
            try:
                match = await Match.objects.aget(id=match_id)
                await match.finish()
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'send_message',
                    'match': match.id,
                    "event": event
                })
            except Exception as e:
                print(e)

        if event == 'start_match':
            try:
                room = await Room.objects.aget(id=self.room_group_name)
                match = await Match.objects.acreate(room=room)
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'send_message',
                    'match': match.id,
                    "event": event
                })
            except Exception as e:
                print(e)

        if event == 'message':
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'sender': self.user,
                'message': message,
                "event": event
            })

    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))

    def validate_response(self, instance, operation):
        return True

    @database_sync_to_async
    def update_user_incr(self, user_id):
        # incrementa o numero de connections do usuário em 1
        user = User.objects.get(id=user_id)
        user.connections = user.connections + 1
        user.save()
        return user.connections

    @database_sync_to_async
    def update_user_decr(self, user_id):
        # decrementa o numero de connections do usuário em 1
        user = User.objects.get(id=user_id)
        user.connections = user.connections - 1 if user.connections > 0 else 0
        user.save()
        return user.connections
