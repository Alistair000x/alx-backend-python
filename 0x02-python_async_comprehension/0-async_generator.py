#!/usr/bin/env python3
import asyncio
import random

async def async_generator():
    # Loop 10 times
    for _ in range(10):
        # Asynchronously wait for 1 second
        await asyncio.sleep(1)
        # Yield a random number between 0 and 10
        yield random.randint(0, 10)
