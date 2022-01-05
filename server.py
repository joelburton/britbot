#!/usr/bin/env python

"""Websocket echo server."""

import asyncio
import websockets

USERS = set()

async def echo(websocket):
    try:
        USERS.add(websocket)
        async for message in websocket:
            print(USERS, message)
            websockets.broadcast(USERS, message)
            print("Done")
    finally:
        print("finally")
        USERS.remove(websocket)

async def main():
    async with websockets.serve(echo, "0.0.0.0", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
