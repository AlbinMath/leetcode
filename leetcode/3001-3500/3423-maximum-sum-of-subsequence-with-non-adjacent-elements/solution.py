from typing import List

class Solution:
    def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        size = 1
        while size < n:
            size *= 2

        # tree[i] = (f00, f01, f10, f11); padding leaves are value 0 -> all zeros
        tree = [(0, 0, 0, 0)] * (2 * size)

        def merge(L, R):
            return (
                max(L[0] + R[2], L[1] + R[0]),
                max(L[0] + R[3], L[1] + R[1]),
                max(L[2] + R[2], L[3] + R[0]),
                max(L[2] + R[3], L[3] + R[1]),
            )

        for i in range(n):
            tree[size + i] = (0, 0, 0, max(nums[i], 0))
        for i in range(size - 1, 0, -1):
            tree[i] = merge(tree[2 * i], tree[2 * i + 1])

        ans = 0
        for pos, x in queries:
            i = size + pos
            tree[i] = (0, 0, 0, max(x, 0))
            i >>= 1
            while i:
                tree[i] = merge(tree[2 * i], tree[2 * i + 1])
                i >>= 1
            ans += tree[1][3]

        return ans % MOD
