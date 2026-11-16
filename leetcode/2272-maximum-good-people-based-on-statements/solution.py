from typing import List

class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)

        # For each person: bits they claim are good, and bits they claim are bad
        says_good = [0] * n
        says_bad = [0] * n
        for i in range(n):
            for j in range(n):
                if statements[i][j] == 1:
                    says_good[i] |= 1 << j
                elif statements[i][j] == 0:
                    says_bad[i] |= 1 << j

        best = 0
        for mask in range(1 << n):
            cnt = mask.bit_count()
            if cnt <= best:
                continue
            ok = True
            for i in range(n):
                if mask >> i & 1:
                    # good person i: all "good" claims must be in mask,
                    # all "bad" claims must be outside mask
                    if says_good[i] & ~mask or says_bad[i] & mask:
                        ok = False
                        break
            if ok:
                best = cnt
        return best
