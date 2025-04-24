#!/usr/bin/env python3
"""Module with a function that returns a multiplier function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier."""
    def multiply(n: float) -> float:
        """Returns n multiplied by multiplier."""
        return n * multiplier
    return multiply
