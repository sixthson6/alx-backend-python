#!/usr/bin/env python3
"""Annotations"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of mixed list as float"""
    return float(sum(mxd_lst))
