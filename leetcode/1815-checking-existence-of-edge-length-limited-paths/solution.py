from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[rx] = ry

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Sort edges by weight
        edgeList.sort(key=lambda x: x[2])

        # Attach original indices to queries and sort by limit
        indexed_queries = [(p, q, limit, i) for i, (p, q, limit) in enumerate(queries)]
        indexed_queries.sort(key=lambda x: x[2])

        dsu = DSU(n)
        ans = [False] * len(queries)
        edge_idx = 0
        num_edges = len(edgeList)

        for p, q, limit, orig_idx in indexed_queries:
            # Add all edges with distance strictly less than limit
            while edge_idx < num_edges and edgeList[edge_idx][2] < limit:
                u, v, _ = edgeList[edge_idx]
                dsu.union(u, v)
                edge_idx += 1

            # Check connectivity
            ans[orig_idx] = (dsu.find(p) == dsu.find(q))

        return ans
