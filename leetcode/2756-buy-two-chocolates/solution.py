from typing import List

class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        a = b = float('inf')  # smallest and second smallest
        for p in prices:
            if p < a:
                a, b = p, a
            elif p < b:
                b = p
        cost = a + b
        return money - cost if cost <= money else money
