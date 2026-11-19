from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(limit: int) -> int:
            if limit <= 0:
                return 0
            freq = [0] * (len(nums) + 1)
            distinct = count = left = 0
            
            for right, val in enumerate(nums):
                if freq[val] == 0:
                    distinct += 1
                freq[val] += 1
                
                while distinct > limit:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                    
                count += right - left + 1
            return count
            
        return at_most(k) - at_most(k - 1)
