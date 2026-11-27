class Solution:
    def numSubarrayBoundedMax(self, nums: list[int], left: int, right: int) -> int:
        ans = 0
        last_invalid = -1
        last_valid = -1
        
        for i, num in enumerate(nums):
            if num > right:
                last_invalid = i
                last_valid = i
            elif num >= left:
                last_valid = i
                
            ans += last_valid - last_invalid
            
        return ans
