"""
Demonstration of AlgoForge Core Algorithms across Sorting, Graphs, DP, and String Matching.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.sorting import quick_sort, merge_sort, radix_sort
from src.searching import binary_search, interpolation_search
from src.graph_algos import Graph, dijkstra, kruskal_mst
from src.dynamic_programming import knapsack_01, longest_common_subsequence, edit_distance
from src.string_algos import kmp_search

def main():
    print("=" * 65)
    print("         ALGOFORGE: ALGORITHM ENGINEERING LABORATORY          ")
    print("=" * 65)

    # 1. Sorting Algorithms
    raw = [64, 34, 25, 12, 22, 11, 90, 88, 76, 45]
    print(f"[+] Raw List: {raw}")
    print(f"    - QuickSort (Median-of-3): {quick_sort(raw)}")
    print(f"    - RadixSort (LSD Base-10): {radix_sort(raw)}")

    # 2. Searching
    sorted_arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    idx = interpolation_search(sorted_arr, 70)
    print(f"[+] Interpolation Search for 70 in array -> Index: {idx}")

    # 3. Graph Shortest Path & MST
    g = Graph(directed=False)
    edges = [
        (0, 1, 4.0), (0, 7, 8.0), (1, 2, 8.0), (1, 7, 11.0),
        (2, 3, 7.0), (2, 8, 2.0), (2, 5, 4.0), (3, 4, 9.0),
        (3, 5, 14.0), (4, 5, 10.0), (5, 6, 2.0), (6, 7, 1.0),
        (6, 8, 6.0), (7, 8, 7.0)
    ]
    for u, v, w in edges:
        g.add_edge(u, v, w)

    dist = dijkstra(g, 0)
    print(f"[+] Dijkstra Shortest Distances from Node 0: {dist}")

    mst_edges, mst_cost = kruskal_mst(9, edges)
    print(f"[+] Kruskal MST Total Cost: {mst_cost} (Edges: {len(mst_edges)})")

    # 4. Dynamic Programming
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    max_val, items = knapsack_01(weights, values, capacity=5)
    print(f"[+] 0/1 Knapsack (Cap=5) -> Max Value: {max_val}, Items Chosen: {items}")

    lcs_len, lcs_str = longest_common_subsequence("ALGORITHM", "LOGARITHM")
    print(f"[+] LCS('ALGORITHM', 'LOGARITHM') -> Length: {lcs_len}, String: '{lcs_str}'")

    ed = edit_distance("INTENTION", "EXECUTION")
    print(f"[+] Levenshtein Edit Distance('INTENTION', 'EXECUTION') -> {ed}")

    # 5. KMP String Matching
    haystack = "ABABDABACDABABCABAB"
    needle = "ABABCABAB"
    matches = kmp_search(haystack, needle)
    print(f"[+] KMP String Search '{needle}' in '{haystack}' -> Indices: {matches}")
    print("=" * 65)

if __name__ == "__main__":
    main()
