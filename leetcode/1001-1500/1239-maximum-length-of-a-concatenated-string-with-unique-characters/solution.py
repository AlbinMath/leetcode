from typing import List

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = [0]  # reachable letter sets, starting with the empty concatenation
        best = 0
        for s in arr:
            m = 0
            ok = True
            for ch in s:
                b = 1 << (ord(ch) - 97)
                if m & b:
                    ok = False
                    break
                m |= b
            if not ok:
                continue  # repeats a letter internally, can never be used
            for old in masks[:]:  # iterate a copy, since masks grows
                if old & m == 0:
                    new = old | m
                    masks.append(new)
                    best = max(best, new.bit_count())
        return best
