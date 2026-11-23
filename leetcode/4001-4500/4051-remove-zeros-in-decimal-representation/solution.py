class Solution:
    def removeZeros(self, n: int) -> int:
        res, mul = 0, 1
        while n:
            d = n % 10
            if d:
                res += d * mul
                mul *= 10
            n //= 10
        return res
