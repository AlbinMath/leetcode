from typing import List

class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        n = len(price)

        def can(d: int) -> bool:
            count, last = 1, price[0]
            for i in range(1, n):
                if price[i] - last >= d:
                    count += 1
                    last = price[i]
                    if count == k:
                        return True
            return False

        lo, hi = 0, (price[-1] - price[0]) // (k - 1)
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo
