from typing import List

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int,
                          composition: List[List[int]],
                          stock: List[int], cost: List[int]) -> int:
        hi_bound = budget + max(stock)
        best = 0

        for comp in composition:
            def ok(m: int) -> bool:
                total = 0
                for j in range(n):
                    need = m * comp[j] - stock[j]
                    if need > 0:
                        total += need * cost[j]
                        if total > budget:
                            return False
                return True

            lo, hi = 0, hi_bound
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if ok(mid):
                    lo = mid
                else:
                    hi = mid - 1

            best = max(best, lo)

        return best
