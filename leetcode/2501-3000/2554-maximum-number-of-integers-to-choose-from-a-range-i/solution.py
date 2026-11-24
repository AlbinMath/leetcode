class Solution:
    def maxCount(self, banned, n, maxSum):
        ban = set(banned)
        allowed = [i for i in range(1, n + 1) if i not in ban]
        pre = [0] + list(accumulate(allowed))
        return bisect_right(pre, maxSum) - 1
