class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        a = list(s)
        i, j = 0, len(a) - 1
        while i < j:
            if a[i] != a[j]:
                m = min(a[i], a[j])
                a[i] = a[j] = m
            i += 1
            j -= 1
        return ''.join(a)
