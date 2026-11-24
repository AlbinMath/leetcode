from collections import deque

class Solution:
    def secondMinimum(self, n, edges, time, change):
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        d = [[float('inf')] * 2 for _ in range(n + 1)]
        d[1][0] = 0
        q = deque([(1, 0)])

        while q:
            u, t = q.popleft()
            if u == n and t == d[n][1]:
                return t

            nt = t
            if (nt // change) % 2:
                nt = (nt // change + 1) * change
            nt += time

            for v in g[u]:
                if nt < d[v][0]:
                    d[v][0] = nt
                    q.append((v, nt))
                elif d[v][0] < nt < d[v][1]:
                    d[v][1] = nt
                    q.append((v, nt))

        return -1
