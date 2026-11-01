"""
Graph Algorithms: Shortest Path, Spanning Trees, Topological Sort, Negative Cycles.
"""
import heapq
from typing import Dict, List, Tuple, Optional

class Graph:
    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: Dict[int, List[Tuple[int, float]]] = {}

    def add_edge(self, u: int, v: int, weight: float = 1.0) -> None:
        if u not in self.adj:
            self.adj[u] = []
        if v not in self.adj:
            self.adj[v] = []
        self.adj[u].append((v, weight))
        if not self.directed:
            self.adj[v].append((u, weight))

def dijkstra(graph: Graph, source: int) -> Dict[int, float]:
    """O((V + E) log V) Dijkstra's algorithm using priority queue."""
    distances = {node: float('inf') for node in graph.adj}
    distances[source] = 0.0
    pq: List[Tuple[float, int]] = [(0.0, source)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > distances[u]:
            continue
        for v, w in graph.adj.get(u, []):
            if distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                heapq.heappush(pq, (distances[v], v))
    return distances

def bellman_ford(graph: Graph, source: int, num_nodes: int) -> Tuple[Optional[Dict[int, float]], bool]:
    """O(V * E) Bellman-Ford algorithm with negative cycle detection."""
    dist = {i: float('inf') for i in range(num_nodes)}
    dist[source] = 0.0

    edges = []
    for u in graph.adj:
        for v, w in graph.adj[u]:
            edges.append((u, v, w))

    for _ in range(num_nodes - 1):
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    # Negative cycle check
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break

    return (None if has_negative_cycle else dist), has_negative_cycle

class DisjointSetUnion:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskal_mst(num_nodes: int, edges: List[Tuple[int, int, float]]) -> Tuple[List[Tuple[int, int, float]], float]:
    """O(E log E) Kruskal's Minimum Spanning Tree using Disjoint Set Union."""
    sorted_edges = sorted(edges, key=lambda x: x[2])
    dsu = DisjointSetUnion(num_nodes)
    mst = []
    total_weight = 0.0

    for u, v, w in sorted_edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            total_weight += w
            if len(mst) == num_nodes - 1:
                break
    return mst, total_weight
