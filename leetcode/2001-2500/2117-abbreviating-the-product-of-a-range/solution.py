import sys
from math import prod

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)  # Python 3.11+ caps int->str at 4300 digits

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        p = prod(range(left, right + 1))
        s = str(p)
        t = s.rstrip('0')
        c = len(s) - len(t)
        if len(t) > 10:
            return f"{t[:5]}...{t[-5:]}e{c}"
        return f"{t}e{c}"
