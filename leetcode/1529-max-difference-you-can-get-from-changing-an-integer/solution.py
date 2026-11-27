class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)

        # maximize
        a = s
        for c in s:
            if c != '9':
                a = s.replace(c, '9')
                break

        # minimize
        b = s
        if s[0] != '1':
            b = s.replace(s[0], '1')
        else:
            for c in s[1:]:
                if c != '0' and c != '1':
                    b = s.replace(c, '0')
                    break

        return int(a) - int(b)
