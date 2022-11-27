import asyncio
from pywsitest import WSTest, WSResponse, WSMessage

async def test_user_1():
    ws_test_1 = (
        WSTest("ws://127.0.0.1:8000/ws/room/1/")
        .with_parameter("event", "new_player")
    )

    await ws_test_1.run()
    assert ws_test_1.is_complete()


async def run_tests():
    await asyncio.gather(test_user_1())

asyncio.get_event_loop().run_until_complete(run_tests())