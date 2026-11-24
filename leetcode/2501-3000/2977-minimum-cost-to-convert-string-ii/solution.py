from typing import List
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        words = set(original + changed)
        ids = {w: i for i, w in enumerate(words)}
        m = len(ids)
        g = [[] for _ in range(m)]
        for a, b, c in zip(original, changed, cost):
            g[ids[a]].append((ids[b], c))

        d = [[float('inf')] * m for _ in range(m)]
        for s in range(m):
            d[s][s] = 0
            h = [(0, s)]
            while h:
                c, u = heappop(h)
                if c != d[s][u]:
                    continue
                for v, w in g[u]:
                    nc = c + w
                    if nc < d[s][v]:
                        d[s][v] = nc
                        heappush(h, (nc, v))

        lens = set(map(len, words))
        n = len(source)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            if dp[i] == float('inf'):
                continue
            if source[i] == target[i]:
                dp[i + 1] = min(dp[i + 1], dp[i])
            for l in lens:
                j = i + l
                if j > n:
                    continue
                a, b = source[i:j], target[i:j]
                if a in ids and b in ids:
                    c = d[ids[a]][ids[b]]
                    if c < float('inf'):
                        dp[j] = min(dp[j], dp[i] + c)

        return dp[n] if dp[n] < float('inf') else -1
