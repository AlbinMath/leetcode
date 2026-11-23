from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        def dist(r: int, t: int) -> int:
            d = (r - t) % k
            return min(d, k - d)

        ce = [0] * k
        co = [0] * k
        for i, v in enumerate(nums):
            r = v % k
            arr = ce if i % 2 == 0 else co
            for t in range(k):
                arr[t] += dist(r, t)

        ans = float('inf')
        for x in range(k):
            for y in range(k):
                if x != y:
                    ans = min(ans, ce[x] + co[y])
        return ans
