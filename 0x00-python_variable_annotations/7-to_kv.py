#!/usr/bin/env python3
"""
Complex types - to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return to_kv
    """
    return (k, float(v ** 2))
