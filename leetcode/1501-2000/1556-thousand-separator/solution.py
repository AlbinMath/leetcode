class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        result = []

        while s:
            result.append(s[-3:])
            s = s[:-3]

        return ".".join(result[::-1])
