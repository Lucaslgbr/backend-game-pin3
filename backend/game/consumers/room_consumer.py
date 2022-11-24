import datetime
import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer


class RoomConsumer(AsyncWebsocketConsumer):
    players = []

    async def connect(self):
        self.room_group_name = self.scope['path'].split('/')[2]
        self.pk = self.scope['url_route']['kwargs'].get('pk', None)
        print('CONSUMER CONNECT')
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        print("Disconnected")
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
        if event == 'new_player':
            new_player = response.get('player')
            if new_player:
                self.players.append(new_player)
            await self.channel_layer.group_send(self.room_group_name, {
                'type': 'send_message',
                'message': message,
                "event": "new_player"
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
