class Solution:
    def minCost(self, s, encCost, flatCost):
        n = len(s)
        pre = [0] * (n + 1)
        for i, ch in enumerate(s):
            pre[i + 1] = pre[i] + (ch == '1')

        def solve(l, r):
            L = r - l
            X = pre[r] - pre[l]
            whole = flatCost if X == 0 else L * X * encCost
            if L % 2 == 0:
                mid = (l + r) // 2
                split = solve(l, mid) + solve(mid, r)
                return min(whole, split)
            return whole

        return solve(0, n)
