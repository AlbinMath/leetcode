import heapq
from collections import defaultdict

class Solution:
    def countRestrictedPaths(self, n, edges):
        mod = 10**9 + 7
        g = defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        d = [float('inf')] * (n+1)
        d[n] = 0
        q = [(0, n)]

        while q:
            dist, u = heapq.heappop(q)
            if dist > d[u]:
                continue
            for v, w in g[u]:
                nd = dist + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(q, (nd, v))

        dp = [0] * (n+1)
        dp[n] = 1
        for u in sorted(range(1, n+1), key=lambda x: d[x]):
            if u == n:
                continue
            dp[u] = sum(dp[v] for v, _ in g[u] if d[v] < d[u]) % mod

        return dp[1]
