from typing import List

class PotentialDSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.dist = [0] * n  # dist[i] = parity difference between i and parent[i]

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            p = self.parent[x]
            self.parent[x] = self.find(p)
            self.dist[x] ^= self.dist[p]
        return self.parent[x]

    def add_edge(self, u: int, v: int, w: int) -> bool:
        ru = self.find(u)
        rv = self.find(v)

        if ru == rv:
            # Cycle formed: valid if and only if existing parity matches edge weight
            return (self.dist[u] ^ self.dist[v]) == w
        else:
            # No cycle formed: merge components
            self.parent[ru] = rv
            self.dist[ru] = self.dist[u] ^ self.dist[v] ^ w
            return True


class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        dsu = PotentialDSU(n)
        added_count = 0

        for u, v, w in edges:
            if dsu.add_edge(u, v, w):
                added_count += 1

        return added_count
