class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        orig = n
        p = 10
        while digit_sum(n) > target:
            n = (n // p + 1) * p
            p *= 10
        return n - orig
