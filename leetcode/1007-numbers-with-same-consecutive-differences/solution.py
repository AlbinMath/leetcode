from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = list(range(1, 10))
        for _ in range(n - 1):
            nxt = []
            for num in res:
                last = num % 10
                nxt_digits = {last + k, last - k}  # a set dedups when k == 0
                for d in nxt_digits:
                    if 0 <= d <= 9:
                        nxt.append(num * 10 + d)
            res = nxt
        return res
