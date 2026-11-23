class Solution:
    def canJump(self, nums):
        farthest = 0

        for i in range(len(nums)):
            # Current index cannot be reached
            if i > farthest:
                return False

            # Update the farthest position we can reach
            farthest = max(farthest, i + nums[i])

            # We can already reach the last index
            if farthest >= len(nums) - 1:
                return True

        return True
