class Solution(object):
    def componentValue(self, nums, edges):
        n = len(nums)
        if n == 1:
            return 0

        total = sum(nums)
        max_val = max(nums)

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Build BFS parent and topological order for iterative bottom-up accumulation
        parent = [-1] * n
        order = [0]
        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        rev_order = order[::-1]

        def can_partition(target):
            sub = list(nums)
            for u in rev_order:
                if sub[u] > target:
                    return False
                if sub[u] == target:
                    sub[u] = 0
                elif parent[u] != -1:
                    sub[parent[u]] += sub[u]
            return sub[0] == 0

        # Test largest number of components c first to maximize deleted edges (c - 1)
        for c in range(total // max_val, 1, -1):
            if total % c == 0 and can_partition(total // c):
                return c - 1

        return 0
