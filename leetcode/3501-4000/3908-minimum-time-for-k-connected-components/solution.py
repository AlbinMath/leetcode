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
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        # Sort edges in descending order of time
        edges.sort(key=lambda x: x[2], reverse=True)

        dsu = DSU(n)
        components = n

        for u, v, t in edges:
            ru, rv = dsu.find(u), dsu.find(v)
            if ru != rv:
                # If merging would drop components below k, this edge must be removed
                if components == k:
                    return t
                dsu.union(u, v)
                components -= 1

        return 0
