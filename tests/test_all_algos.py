"""
Unit tests validating correctness of Sorting, Searching, Graph, DP, and String algorithms.
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from src.sorting import quick_sort, merge_sort, radix_sort, heap_sort, counting_sort
from src.searching import binary_search, interpolation_search
from src.graph_algos import Graph, dijkstra, bellman_ford, kruskal_mst
from src.dynamic_programming import knapsack_01, longest_common_subsequence, edit_distance
from src.string_algos import kmp_search

class TestAlgoForge(unittest.TestCase):
    def test_sorting(self):
        arr = [5, 2, 9, 1, 5, 6, 0]
        expected = [0, 1, 2, 5, 5, 6, 9]
        self.assertEqual(quick_sort(arr), expected)
        self.assertEqual(merge_sort(arr), expected)
        self.assertEqual(heap_sort(arr), expected)
        self.assertEqual(radix_sort(arr), expected)
        self.assertEqual(counting_sort(arr), expected)

    def test_searching(self):
        arr = [10, 25, 33, 47, 59, 81]
        self.assertEqual(binary_search(arr, 47), 3)
        self.assertIsNone(binary_search(arr, 99))
        self.assertEqual(interpolation_search(arr, 47), 3)

    def test_graph_dijkstra(self):
        g = Graph(directed=True)
        g.add_edge(0, 1, 10.0)
        g.add_edge(0, 2, 5.0)
        g.add_edge(2, 1, 3.0)
        dist = dijkstra(g, 0)
        self.assertEqual(dist[1], 8.0)
        self.assertEqual(dist[2], 5.0)

    def test_dp_knapsack_and_lcs(self):
        w = [1, 2, 3]
        v = [10, 15, 40]
        val, items = knapsack_01(w, v, 6)
        self.assertEqual(val, 65)

        lcs_len, lcs_str = longest_common_subsequence("ABCDGH", "AEDFHR")
        self.assertEqual(lcs_len, 3)
        self.assertEqual(lcs_str, "ADH")

        self.assertEqual(edit_distance("kitten", "sitting"), 3)

    def test_kmp(self):
        text = "AABAACAADAABAABA"
        pat = "AABA"
        self.assertEqual(kmp_search(text, pat), [0, 9, 12])

if __name__ == "__main__":
    unittest.main()
