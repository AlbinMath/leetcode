import re
from math import gcd

class Solution:
    def fractionAddition(self, expression: str) -> str:
        num, den = 0, 1
        for a, b in re.findall(r'([+-]?\d+)/(\d+)', expression):
            a, b = int(a), int(b)
            num = num * b + a * den
            den *= b
            g = gcd(abs(num), den)
            num //= g
            den //= g
        return "%d/%d" % (num, den)
