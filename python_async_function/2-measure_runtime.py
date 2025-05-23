#!/usr/bin/env python3
"""documentation for wait_n"""

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime of wait_n."""
    import time
    import asyncio

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    return (end_time - start_time) / n
