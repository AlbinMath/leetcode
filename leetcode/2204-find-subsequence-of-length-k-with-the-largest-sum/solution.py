class Solution:
    def maxSubsequence(self, nums, k):
        return [x for _, x in sorted(sorted(enumerate(nums), key=lambda p: -p[1])[:k])]
