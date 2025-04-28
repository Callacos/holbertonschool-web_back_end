#!/usr/bin/env python3
""" async generator that yields random integers"""

import asyncio
import random


async def async_generator():
    """ async generator that yields random integers"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
