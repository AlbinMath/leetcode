from typing import List
from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]

        for u, v, d in roads:
            g[u].append((v, d))
            g[v].append((u, d))

        ans = float('inf')
        seen = {1}
        q = deque([1])

        while q:
            u = q.popleft()
            for v, d in g[u]:
                ans = min(ans, d)
                if v not in seen:
                    seen.add(v)
                    q.append(v)

        return ans
