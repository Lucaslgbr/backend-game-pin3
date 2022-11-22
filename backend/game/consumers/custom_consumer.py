import datetime
import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer

class CustomConsumer(AsyncWebsocketConsumer):
    pk = None
    room_group_name = ''

    async def connect(self):
        self.room_group_name = self.scope['path'].split('/')[2]
        self.pk = self.scope['url_route']['kwargs'].get('pk', None)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def send_message(self, event):
        message = event['message']
        instance = message['instance']
        operation = message['operation']
        if self.validate_response(instance, operation):
            await self.send(text_data=json.dumps({
                'message': {'instance': instance, 'operation': message['operation']}
            }))