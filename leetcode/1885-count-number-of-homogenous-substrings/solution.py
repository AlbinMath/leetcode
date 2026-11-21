class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = 10**9 + 7
        run = 0
        total = 0

        for i, ch in enumerate(s):
            if i > 0 and ch == s[i - 1]:
                run += 1
            else:
                run = 1
            total += run

        return total % MOD
