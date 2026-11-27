class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        hi = s
        for c in s:
            if c != '9':
                hi = s.replace(c, '9')
                break

        lo = s.replace(s[0], '0')

        return int(hi) - int(lo)
