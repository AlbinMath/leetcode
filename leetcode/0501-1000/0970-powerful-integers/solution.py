class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        ans = set()
        a = 1
        while a < bound:
            b = 1
            while a + b <= bound:
                ans.add(a + b)
                if y == 1:
                    break
                b *= y
            if x == 1:
                break
            a *= x
        return list(ans)
