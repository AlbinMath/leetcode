from collections import defaultdict
from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx


class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)
        dsu = DSU(n)

        for u, v in swaps:
            dsu.union(u, v)

        # Group indices by connected component root
        comp_indices = defaultdict(list)
        for i in range(n):
            root = dsu.find(i)
            comp_indices[root].append(i)

        total_sum = 0

        for indices in comp_indices.values():
            # Count available even positions
            even_count = sum(1 for idx in indices if idx % 2 == 0)

            # Extract and sort values belonging to this component in descending order
            vals = sorted((nums[idx] for idx in indices), reverse=True)

            # Assign largest values to even indices (+) and remaining to odd indices (-)
            for i, val in enumerate(vals):
                if i < even_count:
                    total_sum += val
                else:
                    total_sum -= val

        return total_sum
