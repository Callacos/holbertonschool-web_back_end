#!/usr/bin/python3
"""documentation for wait_n"""
import asyncio
import typing
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """docstring for wait_n"""
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
