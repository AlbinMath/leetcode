from typing import List

class Solution:
    def maxBalancedShipments(self, weight: List[int]) -> int:
        mx = 0
        count = 0
        for w in weight:
            if w < mx:
                count += 1
                mx = 0
            else:
                mx = w if w > mx else mx
        return count
