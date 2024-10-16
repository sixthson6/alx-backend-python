#!/usr/bin/env python3
"""Async funcs"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure execution time for wait_n()
    """
    s = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.time() - s
    return elapsed / n
