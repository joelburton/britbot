#!/usr/bin/env python

"""Watches websocket and forwards up/down commands to microcontroller via serial."""

import serial
import time
import asyncio
import websockets

port = input("Enter port address: ").strip()
s = serial.Serial(f"/dev/{port}")

async def hello():
    async with websockets.connect("ws://britbot.joelburton.net:8765") as websocket:
        print("waiting")
        while True:
            msg = await websocket.recv()
            print("msg", msg)
            if msg == "U":
                s.write(b'U\r\n')
            if msg == "D":
                s.write(b'D\r\n')

asyncio.run(hello())
