import heapq
from collections import defaultdict

class Solution:
    def minimumWeight(self, n, edges, src1, src2, dest):
        g, rg = defaultdict(list), defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))

        def dij(s, graph):
            d = [float('inf')] * n
            d[s] = 0
            q = [(0, s)]
            while q:
                w, u = heapq.heappop(q)
                if w > d[u]:
                    continue
                for v, c in graph[u]:
                    if w + c < d[v]:
                        d[v] = w + c
                        heapq.heappush(q, (d[v], v))
            return d

        a = dij(src1, g)
        b = dij(src2, g)
        c = dij(dest, rg)

        ans = min((a[i] + b[i] + c[i] for i in range(n)
                   if a[i] < float('inf') and b[i] < float('inf')
                   and c[i] < float('inf')), default=float('inf'))
        return ans if ans < float('inf') else -1
