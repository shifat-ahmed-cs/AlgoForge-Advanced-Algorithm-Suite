"""
String Algorithms: Knuth-Morris-Pratt (KMP) and Rabin-Karp Rolling Hash.
"""
from typing import List

def kmp_search(text: str, pattern: str) -> List[int]:
    """O(N + M) KMP string matching with prefix pi-table."""
    if not pattern:
        return []
    # Build pi table
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k

    matches = []
    q = 0
    for i in range(len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = pi[q - 1]
        if pattern[q] == text[i]:
            q += 1
        if q == m:
            matches.append(i - m + 1)
            q = pi[q - 1]
    return matches
