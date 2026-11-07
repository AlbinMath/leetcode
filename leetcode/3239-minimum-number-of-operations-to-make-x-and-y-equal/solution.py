from functools import lru_cache

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @lru_cache(maxsize=None)
        def f(x):
            if x <= y:
                return y - x
            best = x - y
            for d in (11, 5):
                q, r = divmod(x, d)
                best = min(best, r + 1 + f(q))
                best = min(best, (d - r) + 1 + f(q + 1))
            return best

        return f(x)
