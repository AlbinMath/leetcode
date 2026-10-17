import heapq
from collections import defaultdict

class Solution:
    def maxProbability(self, n, edges, succProb, start, end):
        g = defaultdict(list)
        for (u, v), p in zip(edges, succProb):
            g[u].append((v, p))
            g[v].append((u, p))

        d = [0.0] * n
        d[start] = 1.0
        q = [(-1.0, start)]

        while q:
            p, u = heapq.heappop(q)
            p = -p
            if u == end:
                return p
            if p < d[u]:
                continue
            for v, w in g[u]:
                np = p * w
                if np > d[v]:
                    d[v] = np
                    heapq.heappush(q, (-np, v))

        return 0.0
