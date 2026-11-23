class Solution:
    def longestBalanced(self, nums):
        n = len(nums)
        ans = 0
        for l in range(n):
            evens = set()
            odds = set()
            for r in range(l, n):
                v = nums[r]
                if v % 2 == 0:
                    evens.add(v)
                else:
                    odds.add(v)
                if len(evens) == len(odds):
                    ans = max(ans, r - l + 1)
        return ans
