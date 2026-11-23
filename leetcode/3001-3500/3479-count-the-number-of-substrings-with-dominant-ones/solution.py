class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        nxt = [n] * (n + 2)
        for i in range(n - 1, -1, -1):
            nxt[i] = i if s[i] == '0' else nxt[i + 1]

        ans = 0
        for i in range(n):
            # substrings with zero zeros
            p = nxt[i]
            ans += p - i
            z = 1
            while p < n and z * z + z <= n - i:
                q = nxt[p + 1]          # next zero (or n)
                lo = max(p, i + z * z + z - 1)
                hi = q - 1
                if hi >= lo:
                    ans += hi - lo + 1
                p = q
                z += 1
        return ans
