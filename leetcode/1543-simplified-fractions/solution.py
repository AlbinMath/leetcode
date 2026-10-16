from math import gcd

class Solution(object):
    def simplifiedFractions(self, n):
        result = []

        for denominator in range(2, n + 1):
            for numerator in range(1, denominator):
                if gcd(numerator, denominator) == 1:
                    result.append(str(numerator) + "/" + str(denominator))

        return result
