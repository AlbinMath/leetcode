class Solution(object):
    def minimumRemoval(self, beans):
        beans.sort()
        n = len(beans)
        max_kept = max(b * (n - i) for i, b in enumerate(beans))
        return sum(beans) - max_kept
