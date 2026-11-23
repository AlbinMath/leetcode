class Solution(object):
    def minOperationsQueries(self, n, edges, queries):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        LOG = max(1, (n - 1).bit_length())
        parent = [0] * n
        depth = [0] * n
        cnt = [None] * n
        cnt[0] = [0] * 27
        seen = [False] * n
        seen[0] = True
        order = [0]
        for u in order:  # BFS; appending while iterating is fine
            for v, w in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    c = cnt[u][:]
                    c[w] += 1
                    cnt[v] = c
                    order.append(v)

        up = [parent]
        for k in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a
            diff = depth[a] - depth[b]
            for k in range(LOG):
                if (diff >> k) & 1:
                    a = up[k][a]
            if a == b:
                return a
            for k in range(LOG - 1, -1, -1):
                if up[k][a] != up[k][b]:
                    a = up[k][a]
                    b = up[k][b]
            return parent[a]

        ans = []
        for a, b in queries:
            l = lca(a, b)
            length = depth[a] + depth[b] - 2 * depth[l]
            ca, cb, cl = cnt[a], cnt[b], cnt[l]
            best = 0
            for w in range(1, 27):
                c = ca[w] + cb[w] - 2 * cl[w]
                if c > best:
                    best = c
            ans.append(length - best)
        return ans
