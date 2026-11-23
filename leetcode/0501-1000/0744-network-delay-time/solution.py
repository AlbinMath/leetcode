import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times, n, k):
        g = defaultdict(list)
        for u, v, w in times:
            g[u].append((v, w))

        d = [float('inf')] * (n + 1)
        d[k] = 0
        q = [(0, k)]

        while q:
            t, u = heapq.heappop(q)
            if t > d[u]:
                continue
            for v, w in g[u]:
                if t + w < d[v]:
                    d[v] = t + w
                    heapq.heappush(q, (d[v], v))

        ans = max(d[1:])
        return ans if ans < float('inf') else -1
