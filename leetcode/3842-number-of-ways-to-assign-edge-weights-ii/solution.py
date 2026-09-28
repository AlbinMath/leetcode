class Solution:

    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """

        MOD = 1000000007

        # Number of nodes
        n = len(edges) + 1

        # Build tree
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Binary lifting
        LOG = (n).bit_length()

        up = [[0] * (n + 1) for _ in range(LOG)]
        depth = [0] * (n + 1)

        # Iterative DFS/BFS
        stack = [1]
        parent = [0] * (n + 1)
        parent[1] = 0

        while stack:
            u = stack.pop()

            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                up[0][v] = u
                stack.append(v)

        # Build binary lifting table
        for j in range(1, LOG):
            prev = up[j - 1]
            cur = up[j]

            for v in range(1, n + 1):
                cur[v] = prev[prev[v]]

        def lca(a, b):
            # Make a the deeper node
            if depth[a] < depth[b]:
                a, b = b, a

            # Bring a to the same depth as b
            diff = depth[a] - depth[b]

            bit = 0
            while diff:
                if diff & 1:
                    a = up[bit][a]
                diff >>= 1
                bit += 1

            if a == b:
                return a

            # Lift both nodes
            for j in range(LOG - 1, -1, -1):
                if up[j][a] != up[j][b]:
                    a = up[j][a]
                    b = up[j][b]

            return up[0][a]

        # Precompute powers of 2.
        #
        # Maximum distance is n-1.
        pow2 = [1] * (n + 1)

        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        answer = []

        for u, v in queries:

            # Same node -> path has 0 edges.
            # Cost is always 0 (even), so answer is 0.
            if u == v:
                answer.append(0)
                continue

            w = lca(u, v)

            distance = depth[u] + depth[v] - 2 * depth[w]

            # Exactly half of 2^distance assignments
            # have an odd total weight.
            answer.append(pow2[distance - 1])

        return answer
