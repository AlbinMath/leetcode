from functools import lru_cache

class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 10**9 + 7
        m = len(evil)

        # KMP failure function
        fail = [0] * m
        j = 0
        for i in range(1, m):
            while j > 0 and evil[i] != evil[j]:
                j = fail[j - 1]
            if evil[i] == evil[j]:
                j += 1
            fail[i] = j

        # nxt[k][c]: matched length after appending letter c in state k (k < m)
        nxt = [[0] * 26 for _ in range(m)]
        for k in range(m):
            for c in range(26):
                ch = chr(97 + c)
                j = k
                while j > 0 and evil[j] != ch:
                    j = fail[j - 1]
                if evil[j] == ch:
                    j += 1
                nxt[k][c] = j

        @lru_cache(maxsize=None)
        def dp(pos: int, k: int, low: bool, high: bool) -> int:
            if pos == n:
                return 1
            lo = ord(s1[pos]) - 97 if low else 0
            hi = ord(s2[pos]) - 97 if high else 25
            total = 0
            for c in range(lo, hi + 1):
                nk = nxt[k][c]
                if nk == m:
                    continue
                total += dp(pos + 1, nk,
                            low and c == lo,
                            high and c == hi)
            return total % MOD

        return dp(0, 0, True, True)
