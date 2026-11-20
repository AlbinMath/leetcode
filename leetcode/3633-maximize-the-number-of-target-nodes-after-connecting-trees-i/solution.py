from collections import deque
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def build(edges):
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for a, b in edges:
                adj[a].append(b)
                adj[b].append(a)
            return adj

        def counts(adj, limit):
            # for every node, how many nodes are within `limit` edges
            n = len(adj)
            res = [0] * n
            if limit < 0:
                return res
            for s in range(n):
                seen = [False] * n
                seen[s] = True
                q = deque([(s, 0)])
                cnt = 0
                while q:
                    u, d = q.popleft()
                    cnt += 1
                    if d == limit:
                        continue
                    for v in adj[u]:
                        if not seen[v]:
                            seen[v] = True
                            q.append((v, d + 1))
                res[s] = cnt
            return res

        adj1, adj2 = build(edges1), build(edges2)
        c1 = counts(adj1, k)
        best2 = max(counts(adj2, k - 1))
        return [c + best2 for c in c1]
