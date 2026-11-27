from typing import List

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        suffix = 0
        total = 0
        for s in satisfaction:
            suffix += s
            if suffix <= 0:
                break
            total += suffix
        return total
