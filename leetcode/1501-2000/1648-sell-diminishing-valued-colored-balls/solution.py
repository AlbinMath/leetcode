from typing import List

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        MOD = 10**9 + 7

        def cnt(T: int) -> int:
            return sum(x - T for x in inventory if x > T)

        lo, hi = 0, max(inventory)
        while lo < hi:
            mid = (lo + hi) // 2
            if cnt(mid) <= orders:
                hi = mid
            else:
                lo = mid + 1

        T = lo
        total = 0
        sold = 0
        for x in inventory:
            if x > T:
                k = x - T
                total += (x + T + 1) * k // 2
                sold += k

        total += (orders - sold) * T
        return total % MOD
