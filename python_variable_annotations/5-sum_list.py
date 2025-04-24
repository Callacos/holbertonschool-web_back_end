#!/usr/bin/env python3
"""Module with a type-annotated function to sum a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """documentation"""
    return sum(input_list)
