class Solution:
    def maximumLength(self, s: str) -> int:
        top = [[0, 0, 0] for _ in range(26)]  # three longest runs per letter
        n = len(s)
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            L = j - i
            t = top[ord(s[i]) - 97]
            if L > t[0]:
                t[0], t[1], t[2] = L, t[0], t[1]
            elif L > t[1]:
                t[1], t[2] = L, t[1]
            elif L > t[2]:
                t[2] = L
            i = j

        ans = 0
        for a, b, c in top:
            ans = max(ans, a - 2, min(a - 1, b), c)
        return ans if ans >= 1 else -1
