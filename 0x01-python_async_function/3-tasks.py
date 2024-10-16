#!/usr/bin/env python3
"""
Async tasks
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_integer: int) -> asyncio.Task:
    """
    Returns a class
    """
    return asyncio.create_task(wait_random(max_delay))
