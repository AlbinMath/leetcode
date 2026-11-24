from math import gcd
class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        return gcd(targetX, targetY) & (gcd(targetX, targetY) - 1) == 0
