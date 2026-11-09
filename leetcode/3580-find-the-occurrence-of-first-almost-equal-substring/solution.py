class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:
        def z_function(t: str) -> list:
            n = len(t)
            z = [0] * n
            l = r = 0
            for i in range(1, n):
                if i < r:
                    z[i] = min(r - i, z[i - l])
                while i + z[i] < n and t[z[i]] == t[i + z[i]]:
                    z[i] += 1
                if i + z[i] > r:
                    l, r = i, i + z[i]
            return z

        n, m = len(s), len(pattern)
        z1 = z_function(pattern + '#' + s)
        z2 = z_function(pattern[::-1] + '#' + s[::-1])

        for i in range(n - m + 1):
            pre = z1[m + 1 + i]
            suf = z2[n + 1 - i]
            if pre + suf >= m - 1:
                return i
        return -1
