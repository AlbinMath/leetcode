from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        # (1 << 30) - 1 has all bits set for integers up to 10^5
        self.and_cost = [(1 << 30) - 1] * n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, u: int, v: int, w: int):
        ru, rv = self.find(u), self.find(v)
        if ru != rv:
            self.parent[rv] = ru
            self.and_cost[ru] &= self.and_cost[rv]
        self.and_cost[ru] &= w


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)

        for u, v, w in edges:
            dsu.union(u, v, w)

        ans = []
        for s, t in query:
            if s == t:
                ans.append(0)
            elif dsu.find(s) != dsu.find(t):
                ans.append(-1)
            else:
                ans.append(dsu.and_cost[dsu.find(s)])

        return ans
