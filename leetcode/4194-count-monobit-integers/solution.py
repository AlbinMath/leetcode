class Solution(object):
    def countMonobit(self, n):
        count = 1  # the number 0
        v = 1
        while v <= n:
            count += 1
            v = v * 2 + 1
        return count
