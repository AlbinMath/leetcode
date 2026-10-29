from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.components = n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry
            self.components -= 1


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n = len(properties)
        
        # Convert each row to a set of distinct values
        unique_sets = [set(row) for row in properties]
        dsu = DSU(n)

        # Check all pairs (i, j)
        for i in range(n):
            for j in range(i + 1, n):
                # Count common unique elements
                if len(unique_sets[i] & unique_sets[j]) >= k:
                    dsu.union(i, j)

        return dsu.components
