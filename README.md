# AlgoForge: Algorithmic Engineering & Complexity Benchmarking Laboratory

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![CI: Passing](https://img.shields.io/badge/build-passing-brightgreen.svg)](.github/workflows/ci.yml)
[![Complexity: Strict](https://img.shields.io/badge/algorithms-classical-red.svg)]()
[![Academic: BRACU CSE221](https://img.shields.io/badge/course-CSE%20221-orange.svg)]()

## 📌 Course Context: CSE 221 (Algorithms)
*Department of Computer Science and Engineering, BRAC University*  
**Core Principles:** Divide and Conquer, Greedy Heuristics, Dynamic Programming (Optimal Substructure & Overlapping Subproblems), Graph Theory & Shortest Paths, Network Trees, and String Matching Automata.

---

## 🎯 Scope of Implemented Algorithms

### 1. Sorting & Searching
- **QuickSort:** In-place median-of-three pivot selection preventing $\mathcal{O}(N^2)$ worst-case on sorted data.
- **MergeSort:** Divide-and-conquer stable sorting ($\Theta(N \log N)$).
- **HeapSort:** In-place priority queue sorting.
- **Radix & Counting Sort:** Linear time non-comparative sorting ($\mathcal{O}(N + K)$).
- **Interpolation Search:** Probe-based searching achieving $\mathcal{O}(\log \log N)$ average complexity.

### 2. Graph Algorithms
- **Dijkstra's Algorithm:** $\mathcal{O}((V + E) \log V)$ with min-priority queue.
- **Bellman-Ford:** $\mathcal{O}(V \cdot E)$ handling negative weights and detecting negative cycles.
- **Kruskal's MST:** $\mathcal{O}(E \log E)$ utilizing Disjoint Set Union (DSU) with rank and path compression.

### 3. Dynamic Programming & Strings
- **0/1 Knapsack:** Memoized table with item subset backtracking.
- **Longest Common Subsequence (LCS):** Reconstruction of maximal shared subsequence.
- **Levenshtein Distance:** Optimal string transformation operations.
- **Knuth-Morris-Pratt (KMP):** $\mathcal{O}(N + M)$ linear pattern search with failure $\pi$-table.

---

## 🚀 Quickstart & Testing
```bash
# Run demonstration
python main.py

# Run unit tests
python -m unittest discover -s tests
```
