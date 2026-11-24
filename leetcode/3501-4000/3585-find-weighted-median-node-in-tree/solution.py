class Solution(object):
    def findMedian(self, n, edges, queries):
        LOG = max(1, (n - 1).bit_length())
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [0] * n
        depth = [0] * n
        D = [0] * n
        seen = [False] * n
        seen[0] = True
        order = [0]
        for u in order:  # BFS; appending while iterating is fine
            for v, w in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    D[v] = D[u] + w
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
        for u, v in queries:
            if u == v:
                ans.append(u)
                continue
            l = lca(u, v)
            du = D[u] - D[l]
            dv = D[v] - D[l]
            total = du + dv
            if du >= dv:
                cur = u
                Du = D[u]
                for k in range(LOG - 1, -1, -1):
                    a = up[k][cur]
                    if 2 * (Du - D[a]) < total:
                        cur = a
                ans.append(parent[cur])
            else:
                cur = v
                Dl = D[l]
                for k in range(LOG - 1, -1, -1):
                    a = up[k][cur]
                    if 2 * (du + D[a] - Dl) >= total:
                        cur = a
                ans.append(cur)
        return ans
