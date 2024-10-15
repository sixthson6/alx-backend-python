#!/usr/bin/env python3
"""Asynch I/O"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Generate a random float
    implement async funcs
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return (num)
