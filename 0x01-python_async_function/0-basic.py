#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random
import time


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random function
    """
    s = time.perf_counter()
    randomValue = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
    return elapsed
