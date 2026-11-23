from typing import List

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        n = len(nums)
        deletions = 0
        
        for i in range(n - 1):
            if (i - deletions) % 2 == 0 and nums[i] == nums[i + 1]:
                deletions += 1
                
        if (n - deletions) % 2 != 0:
            deletions += 1
            
        return deletions
