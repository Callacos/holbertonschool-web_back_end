#!/usr/bin/python3
import asyncio
import random
"""documentation for wait_random"""

async def wait_random(max_delay: int = 10):
    """Wait for a random delay between 0 and max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
