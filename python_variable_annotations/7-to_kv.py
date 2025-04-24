#!/usr/bin/env python3
"""Module with a type-annotated function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """documentation"""
    return (k, float(v ** 2))
