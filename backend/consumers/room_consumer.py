import datetime
import json

from channels.generic.websocket import AsyncWebsocketConsumer
from backend.consumers.custom_consumer import CustomConsumer

class RoomConsumer(CustomConsumer):
    position = None
    _from = None

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        position = data.get('position')
        if position:
            self.position = position.split('_')
            return

    def validate_response(self, instance, operation):
        inicio = datetime.datetime.strptime(self.position[0], '%Y-%m-%d').date()
        fim = datetime.datetime.strptime(self.position[1], '%Y-%m-%d').date()
        data_evento = datetime.datetime.strptime(instance['start'], '%Y-%m-%d %H:%M').date()
        _from = datetime.datetime.strptime(self._from, '%Y-%m-%d').date()
        if not inicio or not fim:
            return True
        if inicio <= data_evento <= fim or inicio <= _from <= fim:
            return True
        return False

    async def _pass(self):
        return

    async def send_message(self, event):
        _from = event['message'].get('from', '')
        if _from:
            self._from = _from
            # qq eu vou te dizer ne cara
            return await self._pass()
        await super(RoomConsumer, self).send_message(event)