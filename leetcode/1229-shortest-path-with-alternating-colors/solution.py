from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n, redEdges, blueEdges):
        g = [[[] for _ in range(n)] for _ in range(2)]
        for u, v in redEdges:
            g[0][u].append(v)
        for u, v in blueEdges:
            g[1][u].append(v)

        d = [[-1] * n for _ in range(2)]
        d[0][0] = d[1][0] = 0
        q = deque([(0, 0), (0, 1)])

        while q:
            u, c = q.popleft()
            for v in g[1-c][u]:
                if d[1-c][v] == -1:
                    d[1-c][v] = d[c][u] + 1
                    q.append((v, 1-c))

        return [min((x for x in (d[0][i], d[1][i]) if x != -1), default=-1) for i in range(n)]
