import heapq

class Solution:
    def countPaths(self, n, roads):
        mod = 10**9 + 7
        g = [[] for _ in range(n)]

        for u, v, t in roads:
            g[u].append((v, t))
            g[v].append((u, t))

        d = [float('inf')] * n
        ways = [0] * n
        d[0], ways[0] = 0, 1
        q = [(0, 0)]

        while q:
            t, u = heapq.heappop(q)
            if t > d[u]:
                continue

            for v, w in g[u]:
                nt = t + w
                if nt < d[v]:
                    d[v] = nt
                    ways[v] = ways[u]
                    heapq.heappush(q, (nt, v))
                elif nt == d[v]:
                    ways[v] = (ways[v] + ways[u]) % mod

        return ways[n - 1]
