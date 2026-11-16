from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        digits = s[1:-1]

        def make(t: str) -> List[str]:
            res = []
            n = len(t)
            # integer form
            if t == "0" or t[0] != "0":
                res.append(t)
            # decimal forms
            for k in range(1, n):
                whole, frac = t[:k], t[k:]
                if (whole == "0" or whole[0] != "0") and frac[-1] != "0":
                    res.append(whole + "." + frac)
            return res

        ans = []
        for i in range(1, len(digits)):
            lefts = make(digits[:i])
            if not lefts:
                continue
            rights = make(digits[i:])
            for a in lefts:
                for b in rights:
                    ans.append(f"({a}, {b})")
        return ans
