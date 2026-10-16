from math import gcd
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return sum(gcd(a,b)%i==0 for i in range(1,gcd(a,b)+1))
