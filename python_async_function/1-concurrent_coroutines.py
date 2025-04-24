#!/usr/bin/env python3
from typing import List
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Wait for n random delays between 0 and max_delay seconds."""
    delays = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )
    return sorted(delays)