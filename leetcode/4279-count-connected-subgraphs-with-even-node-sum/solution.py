from typing import List

class Solution:
    def evenSumSubgraphs(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = [0] * n
        for u, v in edges:
            adj[u] |= (1 << v)
            adj[v] |= (1 << u)

        ans = 0

        # Iterate over all non-empty subsets of vertices
        for mask in range(1, 1 << n):
            # 1. Check even sum condition
            node_sum = 0
            for i in range(n):
                if (mask >> i) & 1:
                    node_sum += nums[i]
            if node_sum % 2 != 0:
                continue

            # 2. Check connectivity of the induced subgraph
            # Pick the lowest set bit as the start vertex
            start = (mask & -mask).bit_length() - 1
            visited = 1 << start
            queue = [start]

            for u in queue:
                neighbors = adj[u] & mask & ~visited
                while neighbors:
                    v = (neighbors & -neighbors).bit_length() - 1
                    visited |= (1 << v)
                    queue.append(v)
                    neighbors &= neighbors - 1

            if visited == mask:
                ans += 1

        return ans
