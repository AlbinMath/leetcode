class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)

        # Manacher, odd palindromes: d[i] = radius (palindrome length = 2*d[i]-1)
        d = [1] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # pre[e]: longest odd palindrome ending exactly at e (then prefix-max)
        pre = [1] * n
        c = 0
        for e in range(n):
            while c + d[c] - 1 < e:      # center c can no longer reach e
                c += 1
            pre[e] = 2 * (e - c) + 1
        for i in range(1, n):
            pre[i] = max(pre[i], pre[i - 1])

        # suf[b]: longest odd palindrome starting exactly at b (then suffix-max)
        suf = [1] * n
        c = n - 1
        for b in range(n - 1, -1, -1):
            while c - d[c] + 1 > b:
                c -= 1
            suf[b] = 2 * (c - b) + 1
        for i in range(n - 2, -1, -1):
            suf[i] = max(suf[i], suf[i + 1])

        return max(pre[i] * suf[i + 1] for i in range(n - 1))
