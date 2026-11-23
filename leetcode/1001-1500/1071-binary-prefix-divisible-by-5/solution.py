
from typing import List

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = []
        remainder = 0

        for num in nums:
            remainder = (remainder * 2 + num) % 5
            result.append(remainder == 0)

        return result

