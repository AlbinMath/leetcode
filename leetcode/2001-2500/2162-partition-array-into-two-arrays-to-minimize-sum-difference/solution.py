from typing import List
from bisect import bisect_left

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)

        def build(arr):
            m = len(arr)
            groups = [[] for _ in range(m + 1)]
            for mask in range(1 << m):
                s = 0
                cnt = 0
                for i in range(m):
                    if mask >> i & 1:
                        s += arr[i]
                        cnt += 1
                groups[cnt].append(s)
            return groups

        left = build(nums[:n])
        right = build(nums[n:])
        for g in right:
            g.sort()

        ans = float('inf')
        for k in range(n + 1):
            r = right[n - k]
            for a in left[k]:
                # want a + b close to total / 2, i.e. minimize |total - 2(a + b)|
                target = total / 2 - a
                idx = bisect_left(r, target)
                for j in (idx - 1, idx):
                    if 0 <= j < len(r):
                        ans = min(ans, abs(total - 2 * (a + r[j])))
        return ans
