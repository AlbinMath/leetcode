from typing import List

class Solution:
    def canTransform(self, source: List[int], target: List[int]) -> bool:
        return sum(source) == sum(target)
