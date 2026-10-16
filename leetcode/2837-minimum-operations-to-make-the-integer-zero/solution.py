class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            t = num1 - k * num2
            if t < k:
                continue
            if bin(t).count('1') <= k:
                return k
        return -1
