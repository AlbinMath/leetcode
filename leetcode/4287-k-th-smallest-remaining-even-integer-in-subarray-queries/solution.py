from typing import List

class Solution:
    def kthRemainingInteger(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        ev = []
        cnt = [0] * (n + 1)
        for i, x in enumerate(nums):
            cnt[i + 1] = cnt[i]
            if x % 2 == 0:
                ev.append(x // 2)
                cnt[i + 1] += 1

        ans = []
        for l, r, k in queries:
            a, b = cnt[l], cnt[r + 1]
            lo, hi = 0, b - a          # c in [0, b-a]
            while lo < hi:
                mid = (lo + hi) // 2
                if ev[a + mid] - (mid + 1) < k:
                    lo = mid + 1
                else:
                    hi = mid
            ans.append(2 * (k + lo))
        return ans
