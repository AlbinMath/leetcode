class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 7
        p = primeFactors
        if p <= 3:
            return p
        r = p % 3
        if r == 0:
            return pow(3, p // 3, MOD)
        if r == 1:
            return 4 * pow(3, (p - 4) // 3, MOD) % MOD
        return 2 * pow(3, p // 3, MOD) % MOD
