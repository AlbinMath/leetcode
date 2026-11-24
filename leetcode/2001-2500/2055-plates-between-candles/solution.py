from bisect import bisect_left, bisect_right

class Solution:
    def platesBetweenCandles(self, s, queries):
        c = [i for i, ch in enumerate(s) if ch == '|']
        ans = []
        for l, r in queries:
            i = bisect_left(c, l)
            j = bisect_right(c, r) - 1
            ans.append(c[j] - c[i] - (j - i) if i < j else 0)
        return ans
