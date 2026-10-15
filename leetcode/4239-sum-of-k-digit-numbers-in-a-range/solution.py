class Solution:
    def sumOfNumbers(self, l, r, k):
        MOD = 10**9 + 7
        c = r - l + 1
        S = (l + r) * c // 2
        rep = (pow(10, k, MOD) - 1) * pow(9, MOD - 2, MOD) % MOD
        return S % MOD * pow(c, k - 1, MOD) % MOD * rep % MOD
