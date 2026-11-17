class Solution(object):
    def minOperations(self, nums, k):
        seen = set()
        for ops, x in enumerate(reversed(nums), 1):
            if x <= k:
                seen.add(x)
            if len(seen) == k:
                return ops
        return len(nums)
