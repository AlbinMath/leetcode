class Solution:
    def modifyString(self, s: str) -> str:
        chars = list(s)
        n = len(chars)

        for i in range(n):
            if chars[i] != '?':
                continue
            left = chars[i - 1] if i > 0 else ''
            right = chars[i + 1] if i + 1 < n else ''
            for c in 'abc':
                if c != left and c != right:
                    chars[i] = c
                    break

        return ''.join(chars)
