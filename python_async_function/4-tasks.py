#!/usr/bin/env python3
"""documentation for wait_n"""
from typing import List
import asyncio

task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Wait for n random delays between 0 and max_delay seconds."""
    delays = await asyncio.gather(
        *[task_wait_random(max_delay) for _ in range(n)]
    )
    return sorted(delays)
