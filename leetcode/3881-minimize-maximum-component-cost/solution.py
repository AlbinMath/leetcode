from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int) -> bool:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx
            return True
        return False


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        if k >= n:
            return 0

        # Sort edges by weight in ascending order
        edges.sort(key=lambda e: e[2])

        dsu = DSU(n)
        components = n

        for u, v, w in edges:
            if dsu.union(u, v):
                components -= 1
                if components <= k:
                    return w

        return 0
