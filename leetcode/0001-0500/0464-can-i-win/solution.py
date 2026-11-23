from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
            return False

        @lru_cache(None)
        def win(used, remain):
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if not used & bit:
                    if i >= remain or not win(used | bit, remain - i):
                        return True
            return False

        return win(0, desiredTotal)
