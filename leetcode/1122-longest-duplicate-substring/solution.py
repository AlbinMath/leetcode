class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        nums = [ord(c) - 97 for c in s]
        BASE = 26
        MOD1, MOD2 = (1 << 61) - 1, 10**9 + 7  # two moduli to make collisions negligible

        def search(L: int) -> int:
            """Return start index of a duplicate of length L, or -1."""
            pow1 = pow(BASE, L, MOD1)
            pow2 = pow(BASE, L, MOD2)
            h1 = h2 = 0
            for i in range(L):
                h1 = (h1 * BASE + nums[i]) % MOD1
                h2 = (h2 * BASE + nums[i]) % MOD2
            seen = {(h1, h2): [0]}
            for i in range(1, n - L + 1):
                h1 = (h1 * BASE - nums[i - 1] * pow1 + nums[i + L - 1]) % MOD1
                h2 = (h2 * BASE - nums[i - 1] * pow2 + nums[i + L - 1]) % MOD2
                key = (h1, h2)
                if key in seen:
                    # verify to rule out any collision
                    for j in seen[key]:
                        if s[j:j + L] == s[i:i + L]:
                            return i
                    seen[key].append(i)
                else:
                    seen[key] = [i]
            return -1

        lo, hi = 1, n - 1
        start, best = -1, 0
        while lo <= hi:
            mid = (lo + hi) // 2
            idx = search(mid)
            if idx != -1:
                start, best = idx, mid
                lo = mid + 1
            else:
                hi = mid - 1
        return s[start:start + best] if start != -1 else ""
