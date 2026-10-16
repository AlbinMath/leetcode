from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float('inf')
        d = [[INF] * n for _ in range(n)]
        for i in range(n):
            d[i][i] = 0
        for u, v, w in edges:
            d[u][v] = d[v][u] = min(d[u][v], w)
        for k in range(n):
            dk = d[k]
            for i in range(n):
                dik = d[i][k]
                if dik == INF:
                    continue
                di = d[i]
                for j in range(n):
                    if dik + dk[j] < di[j]:
                        di[j] = dik + dk[j]
        best, ans = INF, -1
        for i in range(n):
            cnt = sum(1 for j in range(n) if j != i and d[i][j] <= distanceThreshold)
            if cnt <= best:
                best, ans = cnt, i
        return ans
