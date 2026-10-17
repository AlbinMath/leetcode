import heapq
from collections import defaultdict

class Solution:
    def reachableNodes(self, edges, maxMoves, n):
        g = defaultdict(list)
        for u, v, c in edges:
            g[u].append((v, c+1))
            g[v].append((u, c+1))

        d = [float('inf')] * n
        d[0] = 0
        q = [(0, 0)]

        while q:
            dist, u = heapq.heappop(q)
            if dist > d[u]:
                continue
            for v, w in g[u]:
                nd = dist + w
                if nd < d[v]:
                    d[v] = nd
                    heapq.heappush(q, (nd, v))

        ans = sum(x <= maxMoves for x in d)
        for u, v, c in edges:
            a = max(0, maxMoves - d[u]) if d[u] <= maxMoves else 0
            b = max(0, maxMoves - d[v]) if d[v] <= maxMoves else 0
            ans += min(c, a + b)

        return ans
