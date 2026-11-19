from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = defaultdict(int)
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            L = j - i
            for ln in range(1, L + 1):
                cnt[(s[i], ln)] += L - ln + 1
            i = j

        ans = -1
        for (ch, ln), c in cnt.items():
            if c >= 3 and ln > ans:
                ans = ln
        return ans
