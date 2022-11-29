import datetime
import json
from django.db.models import F
from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
from backend.game.models import Room, Match, User
from channels.db import database_sync_to_async
class RoomConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_group_name = str(self.scope['url_route']['kwargs'].get('pk', None))
        self.pk = self.scope['url_route']['kwargs'].get('pk', None)
        user = self.scope['url_route']['kwargs'].get('user_id', None)
        await self.update_user_incr(user)
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
        user = self.scope['url_route']['kwargs'].get('user_id', None)
        await self.update_user_decr(user)
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
        if 'remove_player':
            user_id = response.get('user', None)
            try:
                room = await Room.objects.aget(id=self.room_group_name)
                user = await User.objects.aget(id=user_id)
                await room.users.remove(user)
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'send_message',
                    'message': message,
                    'user': user,
                    "event": event
                })
            except Exception as e:
                print(e)
        if event == 'finish_room':
            try:
                room = await Room.objects.aget(id=self.room_group_name)
                await room.finish()
                instance_data = ''
                message =  {'instance': instance_data }
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
                message = 'success'
                await self.channel_layer.group_send(self.room_group_name, {
                    'type': 'send_message',
                    'message': 'success',
                    "event": event
                    })
            except Exception as e:
                print(e)

        if event == 'start_match':
            try:
                room = await Room.objects.aget(id=self.room_group_name)
                match = await Match.objects.acreate(room=room)
                message = 'success'
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
                'message': message,
                "event": message
            })
    async def send_message(self, res):
        """ Receive message from room group """
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "payload": res,
        }))

    def validate_response(self, instance, operation):
        if not self.players:
            return True
        return instance['id'] in self.players
        
    @database_sync_to_async
    def update_user_incr(self, user_id):
        User.objects.filter(id=user_id).update(connections=F('connections') + 1)

    @database_sync_to_async
    def update_user_decr(self, user_id):
        User.objects.filter(id=user_id).update(connections=F('connections') - 1)