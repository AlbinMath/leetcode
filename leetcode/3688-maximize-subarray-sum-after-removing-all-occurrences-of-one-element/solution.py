from typing import List
from collections import defaultdict

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        mx = max(nums)
        if mx <= 0:
            return mx

        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        tree = [(0, 0, 0, 0)] * (2 * size)

        def merge(a, b):
            return (
                a[0] + b[0],
                max(a[1], a[0] + b[1]),
                max(b[2], b[0] + a[2]),
                max(a[3], b[3], a[2] + b[1]),
            )

        for i, v in enumerate(nums):
            tree[size + i] = (v, v, v, v)
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        def update(pos, v):
            i = size + pos
            tree[i] = (v, v, v, v)
            i >>= 1
            while i:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i >>= 1

        positions = defaultdict(list)
        for i, v in enumerate(nums):
            if v < 0:
                positions[v].append(i)

        ans = tree[1][3]
        for x, idxs in positions.items():
            for p in idxs:
                update(p, 0)
            ans = max(ans, tree[1][3])
            for p in idxs:
                update(p, x)

        return ans
