#!/usr/bin/python3
"""documentation for wait_n"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay):
    """documentation"""
    return asyncio.create_task(wait_random(max_delay))
