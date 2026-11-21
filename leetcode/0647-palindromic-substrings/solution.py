class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def expand(l: int, r: int) -> int:
            c = 0
            while l >= 0 and r < n and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
            return c

        for center in range(n):
            count += expand(center, center)      # odd length
            count += expand(center, center + 1)  # even length

        return count
