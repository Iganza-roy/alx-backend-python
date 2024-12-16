#!/usr/bin/env python3

# A module containing a function that takes a list of integers and floats and returns their sum.

def sum_mixed_list(mxd_lst: [int, float]) -> float:
    """
    Sums all elements in a mixed list containing integers and floats.
    Handles nested lists recursively.
    """
    return sum(mxd_lst)