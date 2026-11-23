class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        run = 0
        total = 0

        for ch in s:
            if ch == '1':
                run += 1
                total += run
            else:
                run = 0

        return total % MOD
