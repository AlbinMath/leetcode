from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        s = []
        for x in nums:
            while s and gcd(s[-1], x) > 1:
                g = gcd(s[-1], x)
                x = s.pop() // g * x
            s.append(x)
        return s
