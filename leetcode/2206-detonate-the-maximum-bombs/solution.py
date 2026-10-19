from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = [[] for _ in range(n)]
        for i in range(n):
            xi, yi, ri = bombs[i]
            r2 = ri * ri
            for j in range(n):
                if i != j:
                    dx, dy = xi - bombs[j][0], yi - bombs[j][1]
                    if dx * dx + dy * dy <= r2:
                        adj[i].append(j)

        best = 0
        for s in range(n):
            seen = {s}
            stack = [s]
            while stack:
                u = stack.pop()
                for v in adj[u]:
                    if v not in seen:
                        seen.add(v)
                        stack.append(v)
            best = max(best, len(seen))
        return best
