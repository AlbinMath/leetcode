from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        # Fast path: when threshold is 0, 1 divides everything, all nodes are connected
        if threshold == 0:
            return [True] * len(queries)

        dsu = DSU(n)

        # Sieve approach: connect every multiple of z to z
        for z in range(threshold + 1, n + 1):
            for multiple in range(2 * z, n + 1, z):
                dsu.union(z, multiple)

        # Answer queries in O(alpha(n)) time each
        return [dsu.find(a) == dsu.find(b) for a, b in queries]
