class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        ans = 0
        for v in nums:
            w = v % 10
            d = str(v // 10)
            x = int(d[:w])
            y = int(d[w:])
            ans = (ans + pow(x, y, MOD)) % MOD
        return ans
