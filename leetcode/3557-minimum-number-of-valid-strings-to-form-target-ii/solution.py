from typing import List
import random

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        MOD = (1 << 61) - 1
        B = random.randrange(10**6, 10**9)
        m = len(target)

        seen = set()
        maxlen = 0
        for w in words:
            h = 0
            for k, ch in enumerate(w, 1):
                h = (h * B + ord(ch)) % MOD
                seen.add(h * 100003 + k)
            maxlen = max(maxlen, len(w))

        H = [0] * (m + 1)
        P = [1] * (m + 1)
        for i, ch in enumerate(target):
            H[i + 1] = (H[i] * B + ord(ch)) % MOD
            P[i + 1] = P[i] * B % MOD

        L = [0] * m
        for i in range(m):
            lo, hi = 0, min(m - i, maxlen)
            while lo < hi:
                mid = (lo + hi + 1) // 2
                h = (H[i + mid] - H[i] * P[mid]) % MOD
                if h * 100003 + mid in seen:
                    lo = mid
                else:
                    hi = mid - 1
            L[i] = lo

        jumps = 0
        cur = 0
        far = 0
        i = 0
        while cur < m:
            while i <= cur:
                far = max(far, i + L[i])
                i += 1
            if far <= cur:
                return -1
            jumps += 1
            cur = far
        return jumps
