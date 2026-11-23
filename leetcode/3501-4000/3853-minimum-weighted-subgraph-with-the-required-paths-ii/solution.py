class Solution(object):
    def minimumWeight(self, edges, queries):
        n = len(edges) + 1
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        parent = [-1] * n
        depth = [0] * n
        D = [0] * n
        tin = [0] * n
        order = []
        stack = [0]
        seen = [False] * n
        seen[0] = True
        while stack:
            u = stack.pop()
            tin[u] = len(order)
            order.append(u)
            for v, w in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    D[v] = D[u] + w
                    stack.append(v)

        # sparse table over DFS order; table[0][i] = (depth of parent, parent) of order[i]
        # LCA(a, b) for a != b, tin[a] < tin[b]: the parent with min depth in (tin[a], tin[b]]
        m = n
        base = [(depth[parent[order[i]]], parent[order[i]]) if i > 0 else (0, 0)
                for i in range(m)]
        table = [base]
        k = 1
        while (1 << k) <= m:
            prev = table[-1]
            half = 1 << (k - 1)
            table.append([min(prev[i], prev[i + half]) for i in range(m - (1 << k) + 1)])
            k += 1

        def lca(a, b):
            if a == b:
                return a
            l, r = tin[a], tin[b]
            if l > r:
                l, r = r, l
            l += 1  # range (tin[a], tin[b]]
            j = (r - l + 1).bit_length() - 1
            row = table[j]
            x = row[l]
            y = row[r - (1 << j) + 1]
            return min(x, y)[1]

        def dist(a, b):
            return D[a] + D[b] - 2 * D[lca(a, b)]

        ans = []
        for a, b, c in queries:
            ans.append((dist(a, b) + dist(b, c) + dist(a, c)) // 2)
        return ans
