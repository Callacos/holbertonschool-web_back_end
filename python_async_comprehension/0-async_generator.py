#!/usr/bin/env python3
"""docstring for async_generator"""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float, None, None]:
    """docstring for async_generator"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
