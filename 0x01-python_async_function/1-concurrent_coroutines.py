#!/usr/bin/env python3
"""Async methods"""
import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return list of delays (ascending order)
    """
    delays = []
    # spawn wait_random n times
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)

    # insert into list in ascending order (no use of sort())
    # due to concurrency
    for result in results:
        inserted = False
        for i, delay in enumerate(delays):
            if result < delay:
                delays.insert(i, result)
                inserted = True
                break
        if not inserted:
            delays.append(result)

    return delays
