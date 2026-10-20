import heapq
from collections import defaultdict

class Graph:
    def __init__(self, n, edges):
        self.g = defaultdict(list)
        for u, v, w in edges:
            self.g[u].append((v, w))

    def addEdge(self, edge):
        u, v, w = edge
        self.g[u].append((v, w))

    def shortestPath(self, node1, node2):
        q, d = [(0, node1)], {}
        while q:
            cost, u = heapq.heappop(q)
            if u == node2:
                return cost
            if u in d:
                continue
            d[u] = cost
            for v, w in self.g[u]:
                if v not in d:
                    heapq.heappush(q, (cost + w, v))
        return -1
