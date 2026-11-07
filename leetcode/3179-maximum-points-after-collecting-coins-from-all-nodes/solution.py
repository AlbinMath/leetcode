from typing import List

class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(coins)
        T = 15  # t in 0..14, with t capped at 14
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        parent = [-1] * n
        order = []
        stack = [0]
        seen = [False] * n
        seen[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    stack.append(v)

        # sums[u][t] = sum of dp[child][t] over children of u
        sums = [[0] * T for _ in range(n)]

        for u in reversed(order):
            dp = [0] * T
            su = sums[u]
            for t in range(T):
                c = coins[u] >> t
                nt = min(t + 1, T - 1)
                dp[t] = max(c - k + su[t], c // 2 + su[nt])
            p = parent[u]
            if p != -1:
                sp = sums[p]
                for t in range(T):
                    sp[t] += dp[t]
            else:
                return dp[0]
        return 0
