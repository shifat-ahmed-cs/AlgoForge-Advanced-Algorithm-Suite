"""
Comprehensive Sorting Suite with Classical Time Complexity Guarantees.
"""
from typing import List

def quick_sort(arr: List[int]) -> List[int]:
    """In-place QuickSort with median-of-three pivot selection."""
    a = list(arr)
    def _quick_sort(low: int, high: int):
        if low < high:
            pivot_idx = _partition(low, high)
            _quick_sort(low, pivot_idx - 1)
            _quick_sort(pivot_idx + 1, high)

    def _partition(low: int, high: int) -> int:
        mid = (low + high) // 2
        # Median of three
        triplet = sorted([(a[low], low), (a[mid], mid), (a[high], high)])
        med_idx = triplet[1][1]
        a[med_idx], a[high] = a[high], a[med_idx]
        pivot = a[high]

        i = low - 1
        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    _quick_sort(0, len(a) - 1)
    return a

def merge_sort(arr: List[int]) -> List[int]:
    """Stable O(N log N) MergeSort."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def heap_sort(arr: List[int]) -> List[int]:
    """O(N log N) HeapSort in-place."""
    a = list(arr)
    n = len(a)

    def heapify(n: int, i: int):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and a[l] > a[largest]:
            largest = l
        if r < n and a[r] > a[largest]:
            largest = r
        if largest != i:
            a[i], a[largest] = a[largest], a[i]
            heapify(n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(i, 0)
    return a

def counting_sort(arr: List[int]) -> List[int]:
    """O(N + K) Counting sort for non-negative integers."""
    if not arr:
        return []
    max_val = max(arr)
    min_val = min(arr)
    offset = -min_val if min_val < 0 else 0
    range_k = max_val + offset + 1

    counts = [0] * range_k
    for x in arr:
        counts[x + offset] += 1
    res = []
    for val_idx, c in enumerate(counts):
        res.extend([val_idx - offset] * c)
    return res

def radix_sort(arr: List[int]) -> List[int]:
    """O(D * (N + B)) LSD Radix sort for non-negative integers."""
    if not arr or min(arr) < 0:
        return sorted(arr)
    max_val = max(arr)
    exp = 1
    a = list(arr)
    while max_val // exp > 0:
        output = [0] * len(a)
        count = [0] * 10
        for x in a:
            digit = (x // exp) % 10
            count[digit] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        for i in range(len(a) - 1, -1, -1):
            digit = (a[i] // exp) % 10
            output[count[digit] - 1] = a[i]
            count[digit] -= 1
        a = output
        exp *= 10
    return a
