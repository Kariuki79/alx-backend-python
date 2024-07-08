#!/usr/bin/env python3
"""
Module containing the asynchronous coroutine `wait_random`.
"""

import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> Union[int, float]:
    """
    Waits for a random delay between 0 and max_delay (included and float value) seconds and returns it.
    
    Args:
        max_delay (int): The maximum delay time in seconds (default is 10).
        
    Returns:
        float: The actual delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
