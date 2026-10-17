import heapq
from collections import defaultdict

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)
        g = defaultdict(list)
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))

        d = [[float('inf')] * n for _ in range(maxTime + 1)]
        d[0][0] = passingFees[0]
        q = [(passingFees[0], 0, 0)]

        while q:
            cost, t, u = heapq.heappop(q)
            if u == n - 1:
                return cost
            if cost > d[t][u]:
                continue
            for v, w in g[u]:
                nt = t + w
                nc = cost + passingFees[v]
                if nt <= maxTime and nc < d[nt][v]:
                    d[nt][v] = nc
                    heapq.heappush(q, (nc, nt, v))

        return -1
