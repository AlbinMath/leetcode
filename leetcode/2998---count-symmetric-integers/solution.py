class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        ans = 0
        for x in range(low, high + 1):
            s = str(x)
            n = len(s)
            if n % 2:
                continue
            h = n // 2
            if sum(map(int, s[:h])) == sum(map(int, s[h:])):
                ans += 1
        return ans
