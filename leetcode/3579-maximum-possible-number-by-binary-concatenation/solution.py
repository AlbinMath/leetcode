from itertools import permutations

class Solution(object):
    def maxGoodNumber(self, nums):
        best = 0
        for p in permutations(nums):
            s = ''.join(bin(x)[2:] for x in p)
            best = max(best, int(s, 2))
        return best
