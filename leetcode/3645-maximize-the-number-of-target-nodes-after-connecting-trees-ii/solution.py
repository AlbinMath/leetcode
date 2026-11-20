from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def color(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            col = [-1] * n
            col[0] = 0
            q = deque([0])
            while q:
                u = q.popleft()
                for v in adj[u]:
                    if col[v] == -1:
                        col[v] = col[u] ^ 1
                        q.append(v)
            return col

        col1 = color(edges1)
        col2 = color(edges2)

        cnt1 = [col1.count(0), col1.count(1)]
        cnt2 = [col2.count(0), col2.count(1)]
        best2 = max(cnt2)

        return [cnt1[c] + best2 for c in col1]
