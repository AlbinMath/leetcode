class Solution:
    def minSteps(self, n: int) -> int:
        ops = 0
        f = 2
        while n > 1:
            while n % f == 0:
                ops += f
                n //= f
            f += 1
        return ops
