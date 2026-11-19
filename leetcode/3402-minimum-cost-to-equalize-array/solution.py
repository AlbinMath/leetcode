from typing import List

class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        S = sum(nums)
        lo = min(nums)
        hi = max(nums)

        if n == 1:
            return 0

        # pairing is useless
        if cost2 >= 2 * cost1:
            return (n * hi - S) * cost1 % MOD

        best = None
        for T in range(hi, 2 * hi + 1):
            total = n * T - S
            mx = T - lo
            if mx <= total - mx:
                cost = (total // 2) * cost2 + (total % 2) * cost1
            else:
                pairs = total - mx
                cost = pairs * cost2 + (mx - pairs) * cost1
            if best is None or cost < best:
                best = cost
        return best % MOD
