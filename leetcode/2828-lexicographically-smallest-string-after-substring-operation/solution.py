class Solution:
    def smallestString(self, s: str) -> str:
        a = list(s)
        n = len(a)
        i = 0
        while i < n and a[i] == 'a':
            i += 1
        if i == n:
            a[-1] = 'z'
            return ''.join(a)
        while i < n and a[i] != 'a':
            a[i] = chr(ord(a[i]) - 1)
            i += 1
        return ''.join(a)
