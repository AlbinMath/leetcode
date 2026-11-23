class Solution:
    def countDigitOne(self, n: int) -> int:
        ans, i = 0, 1
        while i <= n:
            high = n // (i * 10)
            cur = (n // i) % 10
            low = n % i
            if cur == 0:
                ans += high * i
            elif cur == 1:
                ans += high * i + low + 1
            else:
                ans += (high + 1) * i
            i *= 10
        return ans
