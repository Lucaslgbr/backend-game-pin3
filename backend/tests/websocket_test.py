import asyncio
import websockets
from  pywsitest import WSTest, WSResponse, WSMessage

async def test_ws_connection(room, user):
    ws_test_1 = (
        WSTest(f"ws://127.0.0.1:8000/ws/room/{room}/{user}/")
    )
    await ws_test_1.run()
    assert ws_test_1.is_complete()


async def run_tests():
    await asyncio.gather(test_ws_connection(1,1))

asyncio.get_event_loop().run_until_complete(run_tests())

