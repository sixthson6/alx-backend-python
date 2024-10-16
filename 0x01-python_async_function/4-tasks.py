#!/usr/bin/env python3
"""Async methods"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return list of delays (ascending order)
    """
    return [await delay
            for delay in asyncio.as_completed([task_wait_random(max_delay)
                                               for _ in range(n)])]
