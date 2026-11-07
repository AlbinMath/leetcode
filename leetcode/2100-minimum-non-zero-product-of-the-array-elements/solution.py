class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        top = (1 << p) - 1
        return top % MOD * pow(top - 1, (1 << (p - 1)) - 1, MOD) % MOD
