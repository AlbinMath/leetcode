class Solution:
    def partitionDisjoint(self, nums: list[int]) -> int:
        partition_idx = 0
        left_max = nums[0]
        curr_max = nums[0]
        
        for i in range(1, len(nums)):
            curr_max = max(curr_max, nums[i])
            if nums[i] < left_max:
                partition_idx = i
                left_max = curr_max
                
        return partition_idx + 1
