class Solution:
    def longestPalindrome(self, s: str, t: str) -> int:
        subs_s = {s[i:j] for i in range(len(s) + 1) for j in range(i, len(s) + 1)}
        subs_t = {t[i:j] for i in range(len(t) + 1) for j in range(i, len(t) + 1)}

        ans = 0
        for a in subs_s:
            for b in subs_t:
                if len(a) + len(b) > ans:
                    w = a + b
                    if w == w[::-1]:
                        ans = len(w)
        return ans
