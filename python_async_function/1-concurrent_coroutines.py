#!/usr/bin/env python3
"""documentation for wait_n"""
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> typing.List[float]:
    """Wait for n random delays between 0 and max_delay seconds."""
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
