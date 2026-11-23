class Solution:
    def findIntegers(self, n: int) -> int:
        f = [0] * 32
        f[0], f[1] = 1, 2
        for i in range(2, 32):
            f[i] = f[i-1] + f[i-2]
        s = bin(n)[2:]
        ans, prev = 0, 0
        for i, b in enumerate(s):
            if b == '1':
                ans += f[len(s)-i-1]
                if prev:
                    return ans
                prev = 1
            else:
                prev = 0
        return ans + 1
