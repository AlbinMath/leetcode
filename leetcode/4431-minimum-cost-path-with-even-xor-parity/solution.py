class Solution(object):
    def minActivationCost(self, edges, values):
        n = len(values)
        INF = float('inf')
        p = [bin(v).count('1') & 1 for v in values]

        adj = [[] for _ in range(n)]
        for u, v, c in edges:
            adj[u].append((v, c))
            adj[v].append((u, c))

        # Iterative DFS to get parent array and a processing order
        parent = [-1] * n
        pcost = [0] * n
        order = []
        stack = [0]
        seen = [False] * n
        seen[0] = True
        while stack:
            u = stack.pop()
            order.append(u)
            for v, c in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    pcost[v] = c
                    stack.append(v)

        # cur[v][b] = min cost of a downward path starting at v with parity b
        cur = [[INF, INF] for _ in range(n)]
        for v in range(n):
            cur[v][p[v]] = 0

        ans = INF
        # Children are processed before parents (reverse of DFS order)
        for v in reversed(order):
            par = parent[v]
            if par == -1:
                continue
            w = pcost[v]
            cp = cur[par]
            pp = p[par]
            dv = cur[v]

            # 1) Join this branch with branches already merged into par
            for bc in (0, 1):
                if dv[bc] != INF and cp[bc] != INF:
                    total = cp[bc] + dv[bc] + w
                    if total < ans:
                        ans = total

            # 2) Only then merge this branch into par's best values
            for bc in (0, 1):
                if dv[bc] != INF:
                    nb = bc ^ pp
                    cost = dv[bc] + w
                    if cost < cp[nb]:
                        cp[nb] = cost

        return -1 if ans == INF else ans
