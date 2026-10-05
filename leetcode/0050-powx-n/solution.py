class Solution:
    def myPow(self, x, n):
        negative = n < 0

        if n < 0:
            n = -n

        result = 1.0

        while n > 0:
            if n % 2 == 1:
                result *= x

            x *= x
            n //= 2

        if negative:
            return 1.0 / result

        return result
