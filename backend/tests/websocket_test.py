import asyncio
import websockets
from  pywsitest import WSTest, WSResponse, WSMessage
from threading import Thread
import asyncio
import logging
import threading
from time import sleep
from asgiref.sync import async_to_sync, sync_to_async
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
import time
from rest_framework.test import APIRequestFactory
import json
from backend.game.models import User, Room, Board
class WebsocketTest(TestCase):
    
    def setUp(self) -> None:
        self.user_1 = User.objects.create_user(password='lucas',birth_date='2000-06-19', first_name='Lucas', last_name='Gonçalves', username='lucas', connections=0)
        self.user_2 = User.objects.create_user(password='andre',birth_date='2000-06-19', first_name='André', last_name='Cristen', username='andre', connections=0)
        self.board = Board.objects.create(name='mapa1', lines=10, columns=4)
        self.room = Room.objects.create(board=self.board, name='sala1', max_players=4, owner=self.user_1)
        self.room.users.add(self.user_1)
        self.room.users.add(self.user_2)
        super().setUp()

    async def websocket_new_player():
        async with websockets.connect(f"ws://127.0.0.1:8000/ws/room/1/2/") as websocket:
            response_new_player = await websocket.recv()
            print(response_new_player)
            assert response_new_player == '{"payload": {"type": "send_message", "user": 3, "event": "new_player"}}'
            await websocket.close()


    async def websocket_disconnect_player():
        async with websockets.connect(f"ws://127.0.0.1:8000/ws/room/1/3/") as websocket:
            response_disconnected_player = await websocket.recv()
            print(response_disconnected_player)
            assert response_disconnected_player == '{"payload": {"type": "send_message", "user": 2, "event": "disconnected_player"}}'
            response_remove_player = await websocket.recv()
            print(response_remove_player)
            assert response_remove_player == '{"payload": {"type": "send_message", "user": 2, "event": "remove_player"}}'
            await websocket.close()
            return response_disconnected_player

    def between_callback(callback):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(callback)
        loop.close()

    def test_websocket_events(self):
        t1 = Thread(target=WebsocketTest.between_callback, args=[WebsocketTest.websocket_new_player()])
        t1.start()
        time.sleep(2)
        t2 = Thread(target=WebsocketTest.between_callback, args=[WebsocketTest.websocket_disconnect_player()])
        t2.start()
        time.sleep(2)
        response = self.client.put('/api/v1/room/1/remove_user/', json.dumps({'user': '2'}), content_type='application/json')
        assert response.status_code == 200
        

