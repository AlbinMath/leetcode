from typing import List

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr)
        if total % 3 != 0:
            return False
        target = total // 3
        cur = 0
        parts = 0
        for x in arr:
            cur += x
            if cur == target:
                parts += 1
                cur = 0
        return parts >= 3
