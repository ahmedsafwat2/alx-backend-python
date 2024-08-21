#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random function
    """
    rand_value = random.uniform(0, max_delay)
    await asyncio.sleep(rand_value)
    return rand_value
