from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n
        ans = 0
        prefix = 0
        for i, m in enumerate(machines):
            left = prefix - i * avg
            right = (total - prefix - m) - (n - 1 - i) * avg
            if left < 0 and right < 0:
                cost = -left - right
            else:
                cost = max(abs(left), abs(right))
            ans = max(ans, cost)
            prefix += m
        return ans
