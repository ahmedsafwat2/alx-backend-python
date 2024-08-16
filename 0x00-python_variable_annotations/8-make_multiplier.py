#!/usr/bin/env python3
"""
make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_multiplier
    """
    def multiplier_func(n: float) -> float:
        """
        multiplier by n
        """
        return n * multiplier
    return multiplier_func
