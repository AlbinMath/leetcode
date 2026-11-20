from typing import List

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        parent = [-1] * n
        parent[0] = 0  # sentinel so the root is never seen as unvisited
        order = []
        stack = [0]
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if parent[v] == -1:
                    parent[v] = u
                    stack.append(v)

        cnt = [[0] * 26 for _ in range(n)]
        ans = [0] * n
        for u in reversed(order):
            c = ord(labels[u]) - 97
            cnt[u][c] += 1
            ans[u] = cnt[u][c]
            if u != 0:
                p = cnt[parent[u]]
                cu = cnt[u]
                for i in range(26):
                    p[i] += cu[i]
        return ans
