class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        fail = [0] * n
        j = 0
        for i in range(1, n):
            while j and s[i] != s[j]:
                j = fail[j - 1]
            if s[i] == s[j]:
                j += 1
            fail[i] = j
        return s[:fail[-1]]
