from django.test import TestCase
from channels.testing import WebsocketCommunicator
from backend.game.consumers import RoomConsumer
from channels.testing import HttpCommunicator
from channels.testing import HttpCommunicator

import pytest
from channels.testing import HttpCommunicator

class TestConsumer(TestCase):
    
    @pytest.mark.asyncio
    async def test_my_consumer():
        communicator = HttpCommunicator(RoomConsumer.as_asgi(), "GET", "/test/")
        response = await communicator.get_response()
        assert response["body"] == b"test response"
        assert response["status"] == 200