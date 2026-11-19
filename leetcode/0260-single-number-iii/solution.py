from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for x in nums:
            xor ^= x

        diff = xor & -xor  # lowest set bit of a ^ b

        a = 0
        for x in nums:
            if x & diff:
                a ^= x

        return [a, xor ^ a]
