class Solution:
    def beautifulArray(self, n):
        res = [1]
        while len(res) < n:
            res = [2*x-1 for x in res if 2*x-1 <= n] + [2*x for x in res if 2*x <= n]
        return res
