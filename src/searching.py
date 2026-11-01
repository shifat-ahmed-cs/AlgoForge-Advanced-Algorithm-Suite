"""
Searching Algorithms: Binary, Interpolation, Exponential Search.
"""
from typing import List, Optional

def binary_search(arr: List[int], target: int) -> Optional[int]:
    """O(log N) Binary search on sorted array."""
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

def interpolation_search(arr: List[int], target: int) -> Optional[int]:
    """O(log log N) average search for uniformly distributed sorted array."""
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            return low if arr[low] == target else None
        # Interpolation probe formula
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))
        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1
    return None
