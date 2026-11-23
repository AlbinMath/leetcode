class Solution:
    def jump(self, nums):
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            # Farthest position reachable from the current range
            farthest = max(farthest, i + nums[i])

            # We have reached the end of the current jump's range
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps
