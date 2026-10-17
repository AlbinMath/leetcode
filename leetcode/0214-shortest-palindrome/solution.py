class Solution:
    def shortestPalindrome(self, s: str) -> str:
        t = s + "#" + s[::-1]
        pi = [0] * len(t)
        for i in range(1, len(t)):
            k = pi[i - 1]
            while k and t[i] != t[k]:
                k = pi[k - 1]
            if t[i] == t[k]:
                k += 1
            pi[i] = k
        return s[pi[-1]:][::-1] + s
