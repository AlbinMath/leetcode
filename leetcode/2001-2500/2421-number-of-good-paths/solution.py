from typing import List

class DSU:
    def __init__(self, vals: List[int]):
        n = len(vals)
        self.parent = list(range(n))
        self.max_val = list(vals)
        self.count = [1] * n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, u: int, v: int) -> int:
        ru, rv = self.find(u), self.find(v)
        if ru == rv:
            return 0

        new_paths = 0
        if self.max_val[ru] == self.max_val[rv]:
            new_paths = self.count[ru] * self.count[rv]
            self.parent[rv] = ru
            self.count[ru] += self.count[rv]
        elif self.max_val[ru] > self.max_val[rv]:
            self.parent[rv] = ru
        else:
            self.parent[ru] = rv

        return new_paths


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        # Sort edges by max(vals[u], vals[v])
        edges.sort(key=lambda e: max(vals[e[0]], vals[e[1]]))

        dsu = DSU(vals)
        # Each single node forms a valid path
        good_paths = n

        for u, v in edges:
            good_paths += dsu.union(u, v)

        return good_paths
