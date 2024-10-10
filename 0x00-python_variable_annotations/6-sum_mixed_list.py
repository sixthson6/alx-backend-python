#!/usr/bin/env python3
"""Annotations"""
from typing import Union


def sum_mixed_list(mxd_lst: list[Union[int, float]]) -> float:
    """Returns sum of mixed list as float"""
    return float(sum(mxd_lst))
