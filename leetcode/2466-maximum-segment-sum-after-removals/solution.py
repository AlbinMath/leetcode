from typing import List

class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.seg_sum = [0] * n

    def find(self, x: int) -> int:
        root = x
        while self.parent[root] != root:
            root = self.parent[root]
        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, x: int, y: int) -> int:
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx
            self.seg_sum[rx] += self.seg_sum[ry]
        return self.seg_sum[rx]


class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        n = len(nums)
        dsu = DSU(n)
        active = [False] * n
        ans = [0] * n
        max_sum = 0

        # Process queries in reverse
        for i in range(n - 1, 0, -1):
            idx = removeQueries[i]
            active[idx] = True
            dsu.seg_sum[idx] = nums[idx]
            curr_sum = nums[idx]

            # Merge with left neighbor if active
            if idx > 0 and active[idx - 1]:
                curr_sum = dsu.union(idx, idx - 1)

            # Merge with right neighbor if active
            if idx + 1 < n and active[idx + 1]:
                curr_sum = dsu.union(idx, idx + 1)

            max_sum = max(max_sum, curr_sum)
            ans[i - 1] = max_sum

        return ans
