from typing import List
from collections import defaultdict

class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        g = defaultdict(list)
        for u, v, t in edges:
            g[u].append((v, t))
            g[v].append((u, t))

        seen = [0] * len(values)
        seen[0] = 1
        ans = values[0]

        def dfs(u, time, score):
            nonlocal ans
            if u == 0:
                ans = max(ans, score)

            for v, t in g[u]:
                if time + t <= maxTime:
                    add = values[v] if seen[v] == 0 else 0
                    seen[v] += 1
                    dfs(v, time + t, score + add)
                    seen[v] -= 1

        dfs(0, 0, values[0])
        return ans
